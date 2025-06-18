import sys
import pandas as pd
import joblib

def main():
    input_path = sys.argv[1]
    df = pd.read_csv(input_path)

    # Seleccionar las mismas características que en el entrenamiento
    df = df[['budget', 'popularity']]

    # Cargar modelo y predecir
    model = joblib.load("modelo_tmdb.joblib")
    predictions = model.predict(df)

    df['rentable_pred'] = predictions
    df.to_csv("predicciones.csv", index=False)
    print("Predicciones guardadas en 'predicciones.csv'.")

if __name__ == "__main__":
    main()