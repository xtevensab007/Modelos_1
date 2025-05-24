import sys
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def main():
    input_path = sys.argv[1]  # Ruta al archivo CSV
    df = pd.read_csv(input_path)

    # Filtrar datos inválidos
    df = df[(df['budget'] > 0) & (df['revenue'] > 0) & (df['popularity'].notnull())]
    
    # Crear etiqueta binaria de rentabilidad
    df['rentable'] = (df['revenue'] > df['budget']).astype(int)

    # Seleccionar características
    features = ['budget', 'popularity']
    df = df.dropna(subset=features)

    X = df[features]
    y = df['rentable']

    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar modelo
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("Precisión:", accuracy_score(y_test, y_pred))

    # Guardar modelo
    joblib.dump(model, "modelo_tmdb.joblib")

if __name__ == "__main__":
    main()
