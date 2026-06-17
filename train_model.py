import pickle
import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

data = pd.DataFrame({
    "Amount": np.random.uniform(10, 5000, n),
    "Hour": np.random.randint(0, 24, n),
    "LocationRisk": np.random.uniform(0, 1, n),
    "Device": np.random.randint(0, 2, n),
    "Txn24h": np.random.randint(1, 20, n)
})

# Fraud logic
data["Fraud"] = (
    (data["Amount"] > 3000) &
    (data["LocationRisk"] > 0.7) &
    (data["Device"] == 1)
).astype(int)

X = data.drop("Fraud", axis=1)
y = data["Fraud"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.utils import compute_sample_weight

weights = compute_sample_weight(class_weight="balanced", y=y_train)

model = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train, sample_weight=weights)

# SAVE MODEL + COLUMNS
import os
os.makedirs("model", exist_ok=True)

pickle.dump(model, open("model/fraud_model.pkl", "wb"))
pickle.dump(X.columns, open("model/columns.pkl", "wb"))

print("Model + columns saved")