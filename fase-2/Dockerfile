# Imagen base más completa
FROM python:3.10

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos del proyecto
COPY . .

# Instalar dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto
CMD ["python", "train.py", "train.csv"]
