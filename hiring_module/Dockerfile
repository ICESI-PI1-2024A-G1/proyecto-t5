FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto de los archivos al contenedor
COPY . .

# Define las variables de entorno
# Expone el puerto 8000 para la aplicación web
EXPOSE 8000

# Ejecuta el comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
