# Credit Card Fraud Detection & Analytics System

## Project Overview

Financial fraud is one of the most critical challenges faced by fintech companies and payment processors. Fraudulent transactions can cause severe financial losses and damage customer trust.

This project builds an **end-to-end fraud analytics and machine learning system** that detects fraudulent credit card transactions using **SQL, Python, and Machine Learning**.

The project demonstrates the **complete data analytics pipeline**, starting from data ingestion into a relational database, performing SQL-based exploratory analysis, building machine learning models, optimizing fraud detection thresholds based on business costs, and deploying an interactive analytics dashboard.

The goal of this project is to simulate a **real-world fintech fraud detection workflow** used by data analysts and data scientists in financial institutions.

---

# Dataset

The dataset used in this project is the **Credit Card Fraud Detection Dataset**, which contains transactions made by European cardholders.

Credit Card Fraud Detection Dataset

### Dataset Characteristics

* **Total Transactions:** 284,807
* **Fraud Transactions:** 492
* **Fraud Rate:** ~0.17% (Highly Imbalanced)

### Features

| Column   | Description                                         |
| -------- | --------------------------------------------------- |
| Time     | Seconds elapsed between transactions                |
| Amount   | Transaction amount                                  |
| V1 – V28 | PCA transformed features to protect confidentiality |
| Class    | Target variable (0 = Normal, 1 = Fraud)             |

Due to confidentiality requirements, original variables were transformed using **Principal Component Analysis (PCA)**.

---

# Project Architecture

The project follows a **complete analytics pipeline** similar to real-world data workflows.

```
Data Source (CSV Dataset)
        │
        ▼
Python Data Ingestion Script
(load_dataset.py)
        │
        ▼
MySQL Database
(fintech_analytics)
        │
        ▼
SQL Based Exploratory Data Analysis
        │
        ▼
Python EDA & Feature Analysis
        │
        ▼
Machine Learning Model Training
(Logistic Regression & Random Forest)
        │
        ▼
Threshold Optimization (Cost-Based)
        │
        ▼
Fraud Detection Dashboard
(Streamlit)
```

---

# Technology Stack

| Component        | Tool          |
| ---------------- | ------------- |
| Database         | MySQL         |
| Data Processing  | Python        |
| Data Analysis    | Pandas, NumPy |
| Visualization    | Matplotlib    |
| Machine Learning | Scikit-learn  |
| Model Storage    | Pickle        |
| Dashboard        | Streamlit     |
| Version Control  | Git & GitHub  |

---

# Project Structure

```
credit-card-fraud-detection
│
├── app.py
│   Streamlit dashboard for fraud detection
│
├── python_pipeline
│   └── load_dataset.py
│        Script to load dataset into MySQL database
│
├── creditcard.csv (Kaggle dataset)
│   Transaction dataset
│
├── notebooks
│   ├──  fraud_detection_analysis.ipynb
│   └── model
│       ├── logistic_model.pkl
│       └── scaler.pkl
│
├── sql analysis
│   ├── total_fraud_count.sql
│   ├── risk_amount_bucket.sql
│   ├── transaction_trend.sql
│   └── fraud_comparison.sql
│
├── requirements.txt
│
└── README.md
```

---

# Data Pipeline

## 1 Data Loading

The dataset is loaded into **MySQL** using a Python script.

**load_dataset.py**

Responsibilities:

* Read dataset using Pandas
* Connect to MySQL using SQLAlchemy
* Insert transaction records into database table

This simulates a **data ingestion pipeline** commonly used in production systems.

---

# SQL Exploratory Data Analysis

Initial fraud analysis was performed directly in **MySQL**.

Key SQL analyses include:

### Total Fraud Count

Calculate total number of fraud transactions.

### Risk Amount Bucket

Transactions grouped by amount ranges to analyze fraud distribution.

### Transaction Volume Trend

Daily transaction volume trend.

### Fraud vs Normal Comparison

Comparison of fraud vs normal transaction patterns.

These queries help analysts understand **patterns before building machine learning models**.

---

# Python Exploratory Data Analysis

Further analysis was performed using **Python and Pandas**.

### Effect Size Calculation

Effect size was used to measure how strongly each feature differentiates fraud vs normal transactions.

Formula:

```
Effect Size = |Mean_Fraud - Mean_Normal| / Standard Deviation
```

This identifies the most influential features.

---

### Feature Importance Visualization

Top features were visualized using bar charts.

Example output:

* Top 10 fraud distinguishing features
* Distribution comparisons between fraud and normal transactions

---

### Distribution Analysis

Histograms were used to compare the distribution of features for:

* Fraud transactions
* Normal transactions

This helps identify **separation patterns between classes**.

---

### Box Plot Analysis

Boxplots were used to identify:

* Median differences
* Outliers
* Distribution spread

This provides further insight into transaction behavior.

---

# Machine Learning Models

Two models were tested:

### Logistic Regression

Advantages:

* Interpretable
* Efficient for large datasets
* Good baseline model

Steps performed:

1. Train-Test Split
2. Data Standardization
3. Model Training
4. Probability Prediction
5. Threshold Optimization

---

### Random Forest

Advantages:

* Non-linear relationships
* Handles feature interactions
* Robust to noise

However, logistic regression performed better in this case for **business cost optimization**.

---

# Model Evaluation

Metrics used:

| Metric    | Purpose                                      |
| --------- | -------------------------------------------- |
| Precision | How many predicted frauds are actually fraud |
| Recall    | How many frauds were detected                |
| ROC-AUC   | Overall model discrimination ability         |

---

### Logistic Regression Performance

ROC-AUC Score:

```
0.97
```

This indicates strong model performance.

---

# Threshold Optimization

Fraud detection is not just about accuracy — it is about **business cost optimization**.

Two costs were defined:

```
Fraud Miss Cost = $50,000
False Positive Cost = $50
```

A loop was used to test thresholds from **0.01 to 0.99** and compute total cost.

The threshold with **lowest financial loss** was selected.

This simulates real-world fraud detection strategies used in banks.

---

# Fraud Detection Dashboard

An interactive dashboard was built using **Streamlit**.

Dashboard capabilities:

* Fraud prediction using trained model
* Probability-based classification
* Real-time fraud detection output

The dashboard loads:

```
logistic_model.pkl
scaler.pkl
```

and performs live prediction.

---

# Key Insights

Important insights discovered during analysis:

* Fraud transactions are extremely rare (~0.17%)
* Certain PCA features strongly differentiate fraud patterns
* Logistic Regression achieved high ROC-AUC (0.97)
* Cost-based threshold optimization significantly improves business outcomes

---

# How to Run the Project

### 1 Clone the Repository

```
git clone https://github.com/yourusername/credit-card-fraud-detection.git
```

---

### 2 Install Dependencies

```
pip install -r requirements.txt
```

---

### 3 Run the Dashboard

```
streamlit run app.py
```

---

# Future Improvements

Possible enhancements:

* Real-time fraud detection API
* Feature importance explanation using SHAP
* Model monitoring dashboard
* Advanced ensemble models (XGBoost / LightGBM)

---

# Author

Data Analyst & Machine Learning Enthusiast

Skills Demonstrated:

* SQL Analytics
* Data Pipeline Development
* Machine Learning Modeling
* Fraud Risk Analysis
* Dashboard Development

---

# License

This project is for **educational and portfolio purposes**.
