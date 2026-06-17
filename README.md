
# Fraud Detection System using Machine Learning

## Overview

The Fraud Detection System is an end-to-end Machine Learning application designed to identify potentially fraudulent financial transactions in real time. The system leverages ensemble learning techniques, feature engineering, explainable AI, and a web-based deployment interface to assist in risk assessment and transaction monitoring.

The project simulates real-world fraud detection workflows used in fintech and banking environments by analyzing transaction behavior and generating risk predictions with interpretable explanations.

---

## Problem Statement

Financial institutions process millions of transactions daily, making manual fraud detection impractical. Fraudulent transactions often exhibit hidden behavioral patterns that traditional rule-based systems fail to capture effectively.

This project aims to build an intelligent fraud detection system capable of automatically identifying suspicious transactions while minimizing false alarms and improving detection reliability.

---

## Objectives

* Develop a machine learning-based fraud detection pipeline.
* Handle imbalanced classification challenges.
* Engineer meaningful transaction-based features.
* Compare multiple classification algorithms.
* Optimize model performance through threshold tuning.
* Provide explainable predictions using SHAP.
* Deploy the solution as a real-time web application.

---

## Dataset

The project utilizes transaction-based data containing:

* Transaction Amount
* Transaction Time
* Location Risk Indicators
* Device Information
* Transaction Frequency
* Customer Behavioral Patterns

Additional engineered features were created to improve fraud pattern recognition and classification performance.

---

## Machine Learning Workflow

### 1. Data Collection

* Transaction data generation and loading
* Dataset inspection
* Data quality verification

### 2. Data Preprocessing

* Missing value handling
* Feature selection
* Data validation
* Class distribution analysis

### 3. Feature Engineering

Engineered features include:

* Transaction Frequency Indicators
* Behavioral Risk Factors
* Location Risk Score
* Device Risk Indicators
* Historical Activity Patterns

These features improved the model's ability to capture fraudulent behavior.

### 4. Model Development

Implemented and evaluated:

* Logistic Regression
* Random Forest Classifier
* Gradient Boosting Classifier

### 5. Model Evaluation

Evaluation metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

### 6. Threshold Optimization

Optimized decision thresholds to balance:

* Fraud Detection Rate
* False Positive Rate
* Business Risk

### 7. Explainable AI

Integrated SHAP (SHapley Additive Explanations) to provide:

* Transaction-level explanations
* Feature contribution analysis
* Risk transparency
* Explainable fraud decisions

---

## Results

| Model               | ROC-AUC          |
| ------------------- | ---------------- |
| Logistic Regression | Baseline         |
| Random Forest       | Improved         |
| Gradient Boosting   | Best Performance |

### Final Model

Gradient Boosting Classifier

### Performance

* Accuracy: ~95%
* Recall: ~87%
* Precision: ~70%
* ROC-AUC: ~0.97

### Confusion Matrix

```text
TN = 858
FP = 39
FN = 13
TP = 90
```

The model achieved strong fraud detection capability while maintaining a low false-negative rate.

---

## Technologies Used

### Programming Language

* Python

### Machine Learning Libraries

* Scikit-Learn
* Pandas
* NumPy
* SHAP

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Flask
* HTML
* CSS

---

## Project Structure

```text
Fraud-Detection-System/
│
├── model/
│   ├── fraud_model.pkl
│   └── columns.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## Key Learnings

* Feature engineering significantly improves classification performance.
* Imbalanced datasets require metrics beyond accuracy.
* Recall is critical in fraud detection due to the high cost of false negatives.
* Explainable AI increases trust and transparency in predictive systems.
* End-to-end ML systems require both modeling and deployment expertise.

---

## Future Enhancements

* Real-world transaction dataset integration
* Streaming fraud detection
* Advanced anomaly detection techniques
* Automated model retraining
* Cloud deployment and monitoring
* Real-time alerting system

---

## Business Impact

* Early fraud identification
* Reduced financial losses
* Improved transaction monitoring
* Transparent risk assessment
* Scalable fraud detection workflow

---

## Author

Rohith Visarapu

Machine Learning | Artificial Intelligence | Software Engineering
