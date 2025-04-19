# server.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import pandas as pd
from typing import List, Dict, Optional
from rec_engine.inference import load_user_movie_matrix, recommend_top_k_for_specific_user


app = FastAPI(title="Movie Recommendation API")

# Data models
class MovieList(BaseModel):
    movies: List[str]

class RecommendationRequest(BaseModel):
    user_id: str
    count: int

# Load Available users
user_df = pd.read_csv("./data/ml-latest-small/ratings.csv")
users_ids = user_df["userId"].unique().tolist()
users_ids = [str(i) for i in users_ids]

# Get all movies names & IDs
movies = pd.read_csv("./data/ml-latest-small/movies.csv")

# Get Final Predictions
try:
    prediction_matrix = load_user_movie_matrix(r"./output_predictions/hybrid_final_no_userid.csv")

except Exception as e:
    print("Failed to load predictions matrix:", e)
    prediction_matrix = None


# Create the user db
user_movies_db = {
                    user_id: 
                    
                    [movies.loc[movies['movieId'] == int(movie_id), 'title'].iloc[0] for movie_id 
                        in user_df[user_df['userId'] == int(user_id)]['movieId'].tolist()] 
                    
                    for user_id in users_ids
                }


# Output of rec.sys for user of interest
recommendation_db = { user_id: 
                     
                        prediction_matrix.loc[user_id].sort_values(ascending=False).to_dict()

                        for user_id in users_ids 
                    }



# API endpoints
@app.get("/")
async def root():
    return {"message": "Movie Recommendation API is running"}


@app.get("/users")
async def get_users():
    """Get list of all available user IDs"""
    # return {"users": list(user_movies_db.keys())}
    return {"users": users_ids}


@app.get("/user/{user_id}/movies", response_model=MovieList)
async def get_user_movies(user_id: str):
    """Get favorite movies for a specific user"""
    print(user_id)
    if user_id not in user_movies_db:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    return {"movies": user_movies_db[str(user_id)]}



@app.post("/recommendations", response_model=MovieList)
async def get_recommendations(request: RecommendationRequest):
    """Get movie recommendations for a user"""

    user_id = request.user_id
    count = request.count
    print(user_id, count)

    # Apply Recommendation Engine
    if user_id not in recommendation_db:
        raise HTTPException(status_code=404, detail=f"No recommendations for user {user_id}")
    
    # Limit recommendations to available count or requested count
    available_recommendations = recommendation_db[user_id]
    k = min(count, len(available_recommendations))
    movies_to_return = recommend_top_k_for_specific_user(prediction_matrix, user_id, k)
    #movies_to_return = available_recommendations[:min(count, len(available_recommendations))]
    
    return {"movies": movies_to_return}

if __name__ == "__main__":
    
    # Run the server
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)