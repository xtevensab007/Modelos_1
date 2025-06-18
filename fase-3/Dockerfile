# Usa la imagen oficial de Python 3.10 como base para el contenedor
FROM python:3.10

# Establece el directorio de trabajo dentro del contenedor como /app
WORKDIR /app

# Copia todos los archivos del proyecto actual (desde el host) al directorio /app del contenedor
COPY . .

# Instala las dependencias del proyecto listadas en requirements.txt, sin guardar archivos de caché
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 para permitir conexiones externas (usado por Flask por defecto)
EXPOSE 5000

# Comando que se ejecutará cuando se inicie el contenedor: ejecuta Flask indicando el archivo app
# y configurando Flask para escuchar en todas las interfaces (0.0.0.0)
CMD ["flask", "--app", "apirest", "run", "--host=0.0.0.0"]
