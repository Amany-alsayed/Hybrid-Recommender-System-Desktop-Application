import pandas as pd

def load_user_movie_matrix(path: str) -> pd.DataFrame:
        """
        Loads the precomputed user-movie prediction matrix from a CSV file.

        The matrix should have:
                - Rows as user IDs (index).
                - Columns as movie titles.
                - Values as predicted ratings (0 for already rated or unrated/unseen).

        Parameters:
        -----------
        path : str
                Path to the CSV file containing the user-movie prediction matrix.

        Returns:
        --------
        pd.DataFrame
                A pandas DataFrame with user IDs as index and movie titles as columns.
        """
        matrix = pd.read_csv(path, index_col=0)
        matrix.index = matrix.index.astype(str)  # Convert index to str for compatibility
        return matrix


def recommend_top_k_for_specific_user(matrix: pd.DataFrame, user_id: str = "1", k: int = 5) -> list:
        """
        Recommends the top-k highest-rated movies for a specific user.

        Parameters:
        -----------
        matrix : pd.DataFrame
                The user-movie prediction matrix.

        user_id : str, default="1"
                The user ID to generate recommendations for.

        k : int, default=10
                The number of top recommendations to return.

        Returns:
        --------
        list
                List of movie titles recommended for the user.
        """
        
        if user_id not in matrix.index:
                raise ValueError(f"User {user_id} not found in matrix.")

        user_scores = matrix.loc[user_id]
        sorted_movies = user_scores.sort_values(ascending=False)
        top_movies = sorted_movies.head(k)
        return top_movies.index.tolist()