# 🚗 Auto Evaluate – Used Car Price Prediction

## 📌 Overview

**Auto Evaluate** is a machine learning project that predicts the price of used cars using **Linear Regression**. The model is trained on a dataset of **4009 car records** sourced from **Kaggle** and aims to provide accurate price estimates based on various car features.

---

## 🎯 Objective

The goal of this project is to:

* Predict the **resale price of used cars**
* Understand how different features affect car pricing
* Build a complete **ML pipeline** from data preprocessing to deployment

---

## 🧠 Tech Stack

* **Python**
* **Pandas & NumPy** – Data handling
* **Matplotlib & Seaborn** – Data visualization
* **Scikit-learn** – Model building & evaluation
* **Flask** – Backend API
* **HTML/CSS/JS** – Frontend (if applicable)
* **Pickle** – Model serialization

---

## 📂 Dataset

* Source: Kaggle
* Size: **4009 rows**
* 🔗 Dataset Link: **[[Used Car Prices uploaded by: Taeef Najib](https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset)]**
* Contains features like:

  * Car brand/model
  * Year of manufacture
  * Fuel type
  * Transmission
  * Mileage
  * Engine capacity
  * Price (target variable)

---

## ⚙️ Project Workflow

### 1. Data Cleaning

* Removed unwanted characters from columns (e.g., price formatting)
* Converted data types using `pd.to_numeric()`
* Handled missing values

### 2. Feature Engineering

* Applied **encoding techniques**:

  * One-hot encoding for low-cardinality features
  * Target encoding for high-cardinality features (like model)
* Dropped irrelevant columns

### 3. Data Preprocessing

* Feature scaling using **StandardScaler**
* Train-test split

### 4. Model Building

* Used **Linear Regression**
* Trained model on processed data

### 5. Model Evaluation

* Evaluated using:

  * **R² Score** (model performance)
  * **MAE (Mean Absolute Error)** (prediction error)

### 6. Model Deployment

* Saved model using **pickle**
* Built a **Flask API** to serve predictions
* Connected frontend with backend

---

## 📊 Model Performance

* R² Score: *0.7322964983528121*
* MAE: *6700.119108045312*

---

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AutoValuate.git
cd AutoValuate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Flask App

```bash
python app.py
```

### 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 Example Prediction Flow

1. User inputs car details
2. Data is preprocessed
3. Model predicts log(price)
4. Converted back using `exp()` transformation
5. Final price displayed

---

## ⚠️ Challenges Faced

* Handling **skewed price data**
* Dealing with **high cardinality features**
* Avoiding **negative or zero predictions**
* Maintaining consistency between training and deployment pipeline

---

## 🔮 Future Improvements

* Use advanced models (Random Forest, XGBoost)
* Improve feature engineering
* Add more real-time data
* Deploy on cloud (AWS/Render)

---

## 👨‍💻 Author

[Mithlesh Yeole](https://github.com/mithhhilesh)

## 👨‍💻 Collaborator

[Aditi Jogad](https://github.com/AditiJogad)

---

## ⭐ Acknowledgements

* Kaggle for dataset
* Scikit-learn documentation
* Open-source community

---

## 📌 Note

This project is built for learning purposes and demonstrates a complete **end-to-end machine learning pipeline**.
Flow:
AUTO EVALUATE – ML PIPELINE FLOW (USED CAR PRICE PREDICTION)

1. DATA COLLECTION

* Dataset of 4009 used cars taken from Kaggle
* Contains features like model, year, fuel type, transmission, mileage, etc.

2. DATA LOADING

* Load dataset using pandas (read_csv)
* Inspect data using head(), info(), describe()

3. DATA CLEANING

* Remove unwanted characters (e.g., ₹, commas in price/mileage)
* Convert columns to numeric using pd.to_numeric()
* Handle missing values (drop or fill using median/mean)
* Fix column names (remove spaces, lowercase if needed)

4. EXPLORATORY DATA ANALYSIS (EDA)

* Check distribution of price (usually right-skewed)
* Identify outliers
* Analyze relationships between features and price
* Use plots (histogram, scatterplot, heatmap)

5. TARGET TRANSFORMATION

* Apply log transformation on price to handle skewness:
  y = log1p(price)
* Helps improve model performance

6. FEATURE ENGINEERING

* Handle categorical variables:
  a. One-Hot Encoding → for low-cardinality columns
  b. Target Encoding → for high-cardinality columns (e.g., model)
* Drop unnecessary columns

7. FEATURE SCALING

* Apply StandardScaler to normalize feature values
* Ensures all features are on similar scale

8. TRAIN-TEST SPLIT

* Split dataset into training and testing sets
* Typically 80% training, 20% testing

9. MODEL BUILDING

* Use Linear Regression model from sklearn
* Train model on X_train and y_train

10. MODEL PREDICTION

* Predict on X_test
* Predictions are in log scale

11. INVERSE TRANSFORMATION

* Convert predictions back to original price:
  price = expm1(predicted_log_value)

12. MODEL EVALUATION

* R² Score → measures goodness of fit
* MAE (Mean Absolute Error) → average prediction error

13. MODEL SERIALIZATION

* Save trained model using pickle
* Also save scaler and encoders if used

14. DEPLOYMENT (FLASK)

* Create Flask API
* Load model using pickle
* Take user input from frontend
* Apply same preprocessing steps
* Predict price and return result

15. FRONTEND INTEGRATION

* User inputs car details
* Sends request to Flask backend
* Displays predicted price

END OF PIPELINE


---
