from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

app = Flask(__name__)
model_path = "modelo_tmdb.joblib"
modelo_cargado = False  # Evitar múltiples entrenamientos

def entrenar_modelo():
    df = pd.read_csv("train.csv")
    df = df[(df['budget'] > 0) & (df['revenue'] > 0) & (df['popularity'].notnull())]
    df['rentable'] = (df['revenue'] > df['budget']).astype(int)
    df = df.dropna(subset=['budget', 'popularity'])

    X = df[['budget', 'popularity']]
    y = df['rentable']

    X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, model_path)
    print("✅ Modelo entrenado y guardado.")

@app.before_request
def cargar_o_entrenar_si_falta():
    global modelo_cargado
    if not modelo_cargado and not os.path.exists(model_path):
        print("⚠️ Modelo no encontrado. Entrenando automáticamente...")
        entrenar_modelo()
        modelo_cargado = True

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "budget" not in data or "popularity" not in data:
        return jsonify({"error": "Debes enviar 'budget' y 'popularity' en el cuerpo JSON"}), 400

    model = joblib.load(model_path)
    df = pd.DataFrame([{
        "budget": data["budget"],
        "popularity": data["popularity"]
    }])

    prediction = model.predict(df)[0]
    return jsonify({"rentable_pred": int(prediction)})

@app.route("/train", methods=["GET"])
def train():
    entrenar_modelo()
    return jsonify({"status": "Modelo reentrenado correctamente"})

@app.route("/", methods=["GET"])
def root():
    return jsonify({"API": "Funciona correctamente"})

if __name__ == "__main__":
    app.run(debug=True)
