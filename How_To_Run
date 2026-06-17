# How to Run the Fraud Detection System

## Prerequisites

Ensure the following software is installed:

* Python 3.10+
* pip
* Git (optional)

---

## Clone the Repository

```bash
git clone <repository-url>
cd Fraud-Detection-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Required Dependencies

```bash
pip install -r requirements.txt
```

If the requirements file is unavailable:

```bash
pip install pandas numpy scikit-learn flask shap matplotlib seaborn
```

---

## Train the Model

Run the training script to generate the trained model and feature schema files.

```bash
python train_model.py
```

This creates:

```text
model/
├── fraud_model.pkl
└── columns.pkl
```

---

## Verify Project Structure

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
├── README.md
└── HOW_TO_RUN.md
```

---

## Launch the Application

```bash
python app.py
```

Expected output:

```text
* Running on http://127.0.0.1:5000
```

---

## Open the Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Sample Input

```text
Transaction Amount : 4500
Hour               : 23
Location Risk      : 0.85
Device             : 1
Transactions 24h   : 15
```

### Input Description

| Feature      | Description                                 |
| ------------ | ------------------------------------------- |
| Amount       | Transaction value                           |
| Hour         | Transaction time (0–23)                     |
| LocationRisk | Risk score of transaction location          |
| Device       | Device risk indicator (0 = Safe, 1 = Risky) |
| Txn24h       | Number of transactions within 24 hours      |

---

## Output

The system generates:

* Fraud / Legitimate Prediction
* Fraud Probability Score
* SHAP-Based Explanation
* Top Risk-Contributing Features

Example:

```text
Prediction: FRAUD
Risk Score: 0.93

Top Risk Drivers:
- Amount
- LocationRisk
- Device
```

---

## Model Workflow

```text
Transaction Data
        ↓
Data Preprocessing
        ↓
Feature Engineering
        ↓
Model Training
        ↓
Threshold Optimization
        ↓
SHAP Explainability
        ↓
Flask Deployment
        ↓
Real-Time Fraud Prediction
```

---

## Troubleshooting

### Model File Not Found

Error:

```text
No such file or directory: fraud_model.pkl
```

Solution:

```bash
python train_model.py
```

---

### Missing Dependency

Error:

```text
ModuleNotFoundError
```

Solution:

```bash
pip install -r requirements.txt
```

---

### Port Already In Use

Error:

```text
Address already in use
```

Solution:

Terminate the running Flask process or use another available port.

---

## Performance Summary

| Metric    | Value |
| --------- | ----- |
| Accuracy  | ~95%  |
| Precision | ~70%  |
| Recall    | ~87%  |
| F1 Score  | ~78%  |
| ROC-AUC   | ~0.97 |

---

## Notes

* The project uses Gradient Boosting Classifier as the final model.
* SHAP Explainability is integrated to provide transparent fraud-risk interpretation.
* The system is designed for educational and portfolio purposes and can be extended to real-world financial datasets.

---

## Author

Rohith Visarapu

Machine Learning | Artificial Intelligence | Software Engineering
