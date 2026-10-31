# 🏡 House Price Prediction

An end-to-end Machine Learning project that predicts median house values using California housing data. The project implements multiple regression algorithms, performs hyperparameter tuning, evaluates model performance, and deploys the optimized model through an interactive Streamlit web application.

## 🚀 Live Demo

**Try the application here:**

[🏠 House Price Prediction – Streamlit App](https://house-price-prediction-hhuksk4tfncdwek7ts9nzb.streamlit.app/)

**GitHub Repository:**  
[House-Price-Prediction](https://github.com/varunrayapatirece-pixel/House-Price-Prediction)

---

## 📌 Project Overview

The objective of this project is to build a Machine Learning regression model capable of estimating median housing values based on demographic, geographic, and housing-related features.

The project follows an end-to-end ML workflow:

- Data loading and preprocessing
- Exploratory Data Analysis (EDA)
- Data visualization and correlation analysis
- Training multiple regression models
- Model evaluation and comparison
- Hyperparameter optimization using RandomizedSearchCV
- Model serialization using Joblib
- Deployment using Streamlit Community Cloud

## 📊 Dataset Description

**Dataset:** California Housing Dataset

- Total records: 20,640
- Input features: 8
- Target variable: `MedHouseVal`
- Problem type: Supervised Machine Learning – Regression

### Features Used

| Feature | Description |
|---|---|
| MedInc | Median income in the district |
| HouseAge | Median house age |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | District population |
| AveOccup | Average household occupancy |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |

**Target Variable:** `MedHouseVal` – Median house value, expressed in units of $100,000.

**Dataset Source:** [Scikit-learn California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html)

> **Note:** The dataset represents median housing values at the California district/block-group level, not the selling price of an individual property. The target values are also capped at approximately $500,000, which is an important limitation when interpreting predictions.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Algorithms | Linear Regression, Decision Tree, Random Forest |
| Hyperparameter Tuning | RandomizedSearchCV |
| Model Serialization | Joblib |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |

## ⚙️ Machine Learning Workflow

### 1. Data Preprocessing
- Loaded and explored the California Housing dataset.
- Checked for missing values and duplicate records.
- Separated independent and dependent variables.
- Split the dataset into 80% training and 20% testing data.
- Applied StandardScaler for Linear Regression.
- Used the original feature values for tree-based models.

### 2. Exploratory Data Analysis
- Analyzed feature distributions.
- Studied correlations between input variables.
- Visualized relationships between housing features and median house values.
- Identified important patterns in the dataset.

### 3. Model Building

Implemented and evaluated four regression models:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Tuned Random Forest Regressor

### 4. Hyperparameter Tuning

Used `RandomizedSearchCV` with 3-fold cross-validation to optimize the Random Forest model.

Parameters tuned:

- `n_estimators`
- `max_depth`
- `min_samples_split`
- `min_samples_leaf`
- `max_features`

**Best Parameters:**

```python
{
    'n_estimators': 300,
    'max_depth': 20,
    'min_samples_split': 2,
    'min_samples_leaf': 1,
    'max_features': 0.7
}
```
### 5. Model Evaluation

Evaluated models using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## 📈 Model Performance

The following results were obtained on the held-out test dataset.

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.5332 | 0.7456 | 0.5758 |
| Decision Tree | 0.4542 | 0.7030 | 0.6228 |
| Random Forest | 0.3277 | 0.5060 | 0.8046 |
| **Tuned Random Forest** | **0.3228** | **0.4980** | **0.8108** |

**Best Model:** Tuned Random Forest Regressor

**Test R² Score:** 81.08%

The tuned Random Forest model achieved the best overall test performance among the evaluated models.

## 🔍 Feature Importance

The Random Forest model identified the following features as important contributors to its predictions:

| Feature | Importance |
|---|---:|
| MedInc | 0.5250 |
| AveOccup | 0.1384 |
| Latitude | 0.0890 |
| Longitude | 0.0885 |
| HouseAge | 0.0546 |
| AveRooms | 0.0442 |
| Population | 0.0307 |
| AveBedrms | 0.0297 |

Median income (`MedInc`) was the most influential feature in the trained model.

## 🌐 Streamlit Application

The trained model is integrated into an interactive Streamlit application.

### Application Features

- User-friendly input interface.
- Input fields for all eight housing features.
- Real-time house value prediction.
- Estimated median house value displayed in USD.
- Deployed and accessible through Streamlit Community Cloud.

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── app.py
│
├── dataset/
│   └── california_housing.csv
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   └── house_price_prediction.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 💻 Installation and Execution

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/varunrayapatirece-pixel/House-Price-Prediction.git
```
### 2. Navigate to the Project Directory

```bash
cd House-Price-Prediction
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Run the Streamlit Application

```bash
streamlit run app.py
```
The application will open in your browser at:

```text
http://localhost:8501
```
## 🔮 Future Improvements

- Experiment with Gradient Boosting, XGBoost and other ensemble models.
- Improve model generalization through additional validation techniques.
- Add interactive visualizations for housing trends.
- Explore explainable AI techniques such as SHAP.
- Enhance the application with location-based visual analytics.
- Experiment with more recent and granular real estate datasets.

## 👨‍💻 Author
**Varun Rayapati**
GitHub: [@varunrayapatirece-pixel](https://github.com/varunrayapatirece-pixel)

