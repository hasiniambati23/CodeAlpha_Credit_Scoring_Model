<img width="1920" height="1140" alt="prediction_goodrisk" src="https://github.com/user-attachments/assets/3e0e2dfd-b53e-4965-9042-2301dccff6c9" /># Credit Scoring Model

## Overview

The Credit Scoring Model is a Machine Learning project that predicts whether a loan applicant is a good credit risk or a bad credit risk based on demographic and financial information.

This project uses the German Credit Risk Dataset and implements data preprocessing, feature engineering, machine learning model training, evaluation, and deployment through a Streamlit web application.

---

## Features

* Data preprocessing and cleaning
* Missing value handling
* Categorical feature encoding
* Logistic Regression model
* Random Forest model
* Performance evaluation using multiple metrics
* Model persistence using Joblib
* Interactive Streamlit web application
* GitHub project deployment

---

## Dataset

Dataset: German Credit Risk Dataset

Features include:

* Age
* Sex
* Job
* Housing
* Saving Accounts
* Checking Account
* Credit Amount
* Duration
* Purpose

Target Variable:

* Risk (Good / Bad)

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Joblib
* Matplotlib
* Seaborn
* Git & GitHub

---

## Project Structure

```text
Credit-Scoring-Model/
│
├── data/
│   └── german_credit_data_with_risk.csv
│
├── models/
│   ├── credit_model.pkl
│   └── scaler.pkl
│
├── screenshots/
│   ├── home.png
│   ├── prediction_goodrisk.png
│   └── prediction_badrisk.png
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Model Performance

### Logistic Regression

* Accuracy: 71.0%
* Precision: 72.4%
* Recall: 95.0%
* F1 Score: 82.2%
* ROC-AUC: 59.6%

### Random Forest

* Accuracy: 69.5%
* Precision: 73.0%
* Recall: 90.1%
* F1 Score: 80.6%
* ROC-AUC: 66.7%

Logistic Regression was selected as the final model.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/hasiniambati23/CodeAlpha_Credit_Scoring_Model.git
cd CodeAlpha_Credit_Scoring_Model
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Screenshots

### Home Page

"C:\Users\hasin\OneDrive\Documents\credit_scoring_project\screenshots\HOME.png"

### Good Credit Prediction

"C:\Users\hasin\OneDrive\Documents\credit_scoring_project\screenshots\prediction_goodrisk.png"

### Bad Credit Prediction

"C:\Users\hasin\OneDrive\Documents\credit_scoring_project\screenshots\prediction_badrisk.png"

---

## Future Improvements

* Hyperparameter tuning
* Advanced feature engineering
* Model explainability using SHAP
* Deployment on Streamlit Cloud
* Integration with banking workflows

---

## Author

Hasini Reddy

Machine Learning and AI Student
