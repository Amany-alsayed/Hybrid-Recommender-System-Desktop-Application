# Hybrid Recommender System Desktop Application

This desktop-based application delivers personalized movie recommendations by leveraging a hybrid recommender system. Built using Python and PyQt5, the system combines the strengths of multiple recommendation techniques—content-based filtering, collaborative filtering, and matrix factorization—to provide users with accurate and diverse movie suggestions in an interactive graphical interface.

The goal is to overcome the limitations of individual methods, such as the cold start problem, sparsity, and limited personalization, by blending them into a complementary hybrid model.


## 🛠️ Tech Stack:

- PyQt5 for building a user-friendly graphical interface.

- NumPy, pandas, and scikit-learn for data processing and machine learning.

- matplotlib and seaborn for data visualization.

- Surprise library for implementing collaborative filtering algorithms and matrix factorization models.


## Table of Contents
- [Project Overview](#project-overview)
- [Environment Preparation](#environment-preparation)
  - [Using Python Virtual Environment (venv)](#using-python-virtual-environment-venv)
  - [Using Conda](#using-conda)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
  

## Project Overview

A Python-based desktop application that combines PyQt5 for GUI with a hybrid recommender system integrating content-based filtering, collaborative filtering, and matrix factorization. Designed for personalized movie recommendations through an interactive and user-friendly interface.

### **How the Hybrid Approach Works**

Recommender systems are crucial in many real-world applications—from Netflix to Spotify—where suggesting the right content improves user satisfaction and engagement. Our system combines the following strategies:


  **1. Content-Based Filtering:**
  
  
  - **Core Idea:** Recommends items based on features of items the user has previously liked.
  
  - **Features Used:** Genres, writers, directors, production countries, spoken languages, etc.
  
  - **Use Case:** Works well for new users with little interaction history (cold start on user side).

    

  **2. Collaborative Filtering:**
  

  **Core Idea:** Focuses on leveraging user-item interactions rather than item metadata.

  - **User-Based Collaborative Filtering:**
    
    - Finds users with similar preferences and recommends items those users liked.
        
    - Assumes “similar users like similar items.”
    
  - **Item-Based Collaborative Filtering:**
    
    - Finds items similar to those the user has rated highly.
        
    - Assumes “users like items similar to ones they’ve liked.”
    

  **3. Matrix Factorization (SVD - Singular Value Decomposition)**
  
   -  **Concept:** Decomposes the user-item rating matrix into latent factors.
  
   - **Strengths:**
  
     - Handles large sparse datasets efficiently.
  
     - Captures underlying patterns beyond surface-level similarities.
  
  **Why It Matters:** It's a powerful baseline in many industrial recommender systems like those used in Netflix Prize competitions.


### Why a Hybrid Approach?

**Each individual method has limitations:**

- Content-based filtering may become too narrow (over-specialization).

- Collaborative filtering suffers in sparse datasets or when new users/items are introduced.

- Matrix factorization assumes sufficient data for effective training.
- 

**By combining them:**

- We increase diversity and serendipity of recommendations.

- We mitigate weaknesses like cold-start or overspecialization.

- We enhance prediction accuracy across different user types (new vs. active).




## Environment Preparation

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

## Dependencies

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


## Usage

After setting up your environment, you can run your main application script. For example:
```bash
python main.py
```
Replace `main.py` with the entry point of your project.


## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and open a pull request. For significant changes, please open an issue first to discuss your ideas.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
