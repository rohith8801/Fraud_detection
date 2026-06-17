from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import shap

app = Flask(__name__)

model = pickle.load(open("model/fraud_model.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

explainer = shap.TreeExplainer(model)


def build_features(form):
    final_input = dict.fromkeys(columns, 0)

    final_input["Amount"] = float(form["amount"])
    final_input["Hour"] = int(form["hour"])
    final_input["LocationRisk"] = float(form["location_risk"])
    final_input["Device"] = int(form["device"])
    final_input["Txn24h"] = int(form["txn24h"])

    return pd.DataFrame([final_input])


def get_shap_explanation(input_df):
    shap_values = explainer.shap_values(input_df)

    values = shap_values[1][0] if isinstance(shap_values, list) else shap_values[0]

    features = input_df.columns
    idx = np.argsort(np.abs(values))[-3:][::-1]

    results = []
    for i in idx:
        direction = "⬆️ Risk" if values[i] > 0 else "⬇️ Risk"
        results.append(f"{features[i]} {direction}")

    return results


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        X = build_features(request.form)

        prob = model.predict_proba(X)[0][1]
        label = "🚨 FRAUD" if prob > 0.5 else "✅ LEGIT"

        shap_results = get_shap_explanation(X)

        return render_template(
            "index.html",
            prediction_text=f"{label} (Risk: {prob:.2f})",
            shap_results=shap_results
        )

    except Exception as e:
        return render_template("index.html", prediction_text=str(e))


if __name__ == "__main__":
    app.run(debug=True)