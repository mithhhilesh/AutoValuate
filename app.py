from flask import Flask, request, jsonify
import pickle
import pandas as pd
import re
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)
from flask import send_from_directory

@app.route("/")
def home():
    return send_from_directory(".", "autovaluate.html")

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

model_mean = pickle.load(open("model_mean.pkl", "rb"))
ext_mean = pickle.load(open("ext_mean.pkl", "rb"))
int_mean = pickle.load(open("int_mean.pkl", "rb"))

columns = pickle.load(open("columns.pkl", "rb"))

def extract_litres(engine_str):
    match = re.search(r'([\d\.]+)\s*[Ll]', str(engine_str))
    return float(match.group(1)) if match else None

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        df = pd.DataFrame([{
            "brand": data["brand"],
            "model": data["model"],
            "model_year": int(data.get("year") or 0),
            "milage": float(data.get("mileage") or 0),
            "fuel_type": data["fuel_type"],
            "transmission": data["transmission"],
            "ext_col": data["ext_col"],
            "int_col": data["int_col"],
            "accident": data["accident"],
            "clean_title": data["clean_title"],
            "engine_size": extract_litres(data["engine"]) or 2.0
        }])

        df["has_accident"] = df["accident"].str.contains("accident", case=False, na=False).astype(int)
        df["clean_title_flag"] = (df["clean_title"] == "Yes").astype(int)
        df.drop(columns=["accident", "clean_title"], inplace=True)  

        df["model_encoded"] = df["model"].map(model_mean).fillna(model_mean.mean())
        df["ext_col_encoded"] = df["ext_col"].map(ext_mean).fillna(ext_mean.mean())
        df["int_col_encoded"] = df["int_col"].map(int_mean).fillna(int_mean.mean())

        df.drop(['model','ext_col','int_col'], axis=1, inplace=True)

        df = pd.get_dummies(df, drop_first=True)
        df = df.reindex(columns=columns, fill_value=0)

        df = scaler.transform(df)

        pred_log = model.predict(df)

        price = np.expm1(pred_log[0])   
        price = max(0, price)           

        return jsonify({
            "price": round(price, 2)
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)