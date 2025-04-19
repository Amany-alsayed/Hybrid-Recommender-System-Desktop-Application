# Hybrid Recommender System Desktop Application

This desktop-based application delivers personalized movie recommendations by leveraging a hybrid recommender system. Built using Python and PyQt5, the system combines the strengths of multiple recommendation techniques—content-based filtering, collaborative filtering, and matrix factorization—to provide users with accurate and diverse movie suggestions in an interactive graphical interface.

The goal is to overcome the limitations of individual methods, such as the cold start problem, sparsity, and limited personalization, by blending them into a complementary hybrid model.


## 🛠️ Tech Stack:

- PyQt5 for building a user-friendly graphical interface.

- NumPy, pandas, and scikit-learn for data processing and machine learning.

- matplotlib and seaborn for data visualization.

- Surprise library for implementing collaborative filtering algorithms and matrix factorization models.

  
## 🎯 Project Overview

A Python-based desktop application that combines PyQt5 for GUI with a hybrid recommender system integrating content-based filtering, collaborative filtering, and matrix factorization. Designed for personalized movie recommendations through an interactive and user-friendly interface.


## 🔀 How the Hybrid Approach Works

Recommender systems are used in many real-world applications (e.g., Netflix, Spotify) to improve user satisfaction by suggesting the right content. Our system combines the following strategies:



### 1. Content-Based Filtering

- **Core Idea**: Recommends items based on features of items the user has previously liked.  
- **Features Used**: Genres, writers, directors, production countries, spoken languages, etc.  
- **Use Case**: Ideal for new users with little interaction history (cold start on the user side).



### 2. Collaborative Filtering

Collaborative filtering relies on user-item interactions. It has two approaches:

#### 📌 User-Based Collaborative Filtering

- **How it works**: Finds users with similar preferences and recommends items those users liked.  
- **Assumption**: "Users who liked the same items in the past will like similar items."

#### 📌 Item-Based Collaborative Filtering

- **How it works**: Finds items similar to those the user has rated highly.  
- **Assumption**: "Users like items similar to ones they’ve liked before."



### 3. Matrix Factorization (SVD - Singular Value Decomposition)

- **Core Idea**: Decomposes the user-item rating matrix into latent factors (features).

#### ✅ Strengths:

- Handles large, sparse datasets efficiently.  
- Captures hidden patterns beyond surface-level similarities.

- **Why It Matters**: Used widely in industrial recommender systems, including Netflix's recommendation engine.



## 🤝 Why a Hybrid Approach?

Each individual method has limitations:

- **Content-Based Filtering**: Can lead to over-specialization (narrow recommendations).  
- **Collaborative Filtering**: Struggles with sparse datasets and new users/items.  
- **Matrix Factorization**: Needs a sufficient amount of data to train effectively.

### ✅ By combining these methods:

- **Increased Diversity**: The hybrid model generates a wider variety of recommendations.  
- **Mitigated Weaknesses**: Combines strengths of each model to overcome issues like cold-start and overspecialization.  
- **Better Prediction Accuracy**: Works well for different user types, including both new and active users.

## 🤖 Model Weights

Each model contributes **0.25** to the final prediction:

- **User-Based Collaborative Filtering**: Finds similarity based on user ratings.
- **Item-Based Collaborative Filtering**: Finds similarity based on item ratings.
- **Content-Based Filtering**: Uses metadata like genre, year, and description.
- **Matrix Factorization (SVD)**: Leverages matrix factorization for better recommendation.


## 🌍 Environment Preparation

To ensure that all dependencies are installed correctly, follow one of the methods below to set up your environment.

### Using Python Virtual Environment (venv)

1. **Create a virtual environment:**
  ```bash
  python3 -m venv myenv
  ```
2. **Activate the virtual environment:**
  - **macOS/Linux:**
    ```bash
    source myenv/bin/activate
    ```
  - **Windows:**
    ```bash
    myenv\Scripts\activate
    ```
3. **Upgrade pip and install dependencies:**
  ```bash
  pip install --upgrade pip
  pip install -r requirements.txt
  ```

### Using Conda

1. **Create a Conda environment:**
  ```bash
  conda create --name myenv python=3.10
  ```
2. **Activate the environment:**
  ```bash
  conda activate myenv
  ```
3. **Install packages:**
  ```bash
  conda install numpy pandas scikit-learn matplotlib seaborn
  conda install -c conda-forge pyqt
  pip install scikit-surprise fastapi uvicorn pydantic requests
  ```
## 🕹️ Usage

 After setting up your environment, you can run your application as follows:
```bash
python server.py
 ```
 ```bash
 python client.py
 ```

## 📦 Dependencies

The primary dependencies for this project are:
- **PyQt5:** For building graphical user interfaces.
- **scikit-surprise:** A library for building and analyzing recommender systems.
- **numpy:** For numerical computing.
- **pandas:** For data manipulation and analysis.
- **scikit-learn:** For machine learning algorithms.
- **FastAPI:** For building high-performance web APIs.
- **Uvicorn:** ASGI server for running FastAPI applications.
- **Pydantic:** For data validation and settings management.
- **Requests:** For making HTTP requests.

## 🙋‍♂️ Contributing

Fork the repo, make improvements, and submit a pull request.  
For major changes, please open an issue first to discuss what you would like to change.
