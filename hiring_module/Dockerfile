FROM python:3.10

WORKDIR /app

COPY requirements.txt .

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto de los archivos al contenedor
COPY . .

# Define las variables de entorno
ENV SECRET_KEY=django-insecure-4ht3kx09p6eqjx1&(l#d8h5qsmg(3jdgthb2aw#gz!7un41*mr
ENV DEBUG=True
ENV DATABASE_NAME=defaultdb
ENV DATABASE_USER=doadmin
ENV DATABASE_PASSWORD=
ENV DATABASE_HOST=db-postgres-proyecto-t5-do-user-16438607-0.c.db.ondigitalocean.com
ENV DATABASE_PORT=25060
ENV EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
ENV EMAIL_HOST=mail.sebastiandiazdev.com
ENV EMAIL_PORT=465
ENV EMAIL_USE_SSL=True
ENV EMAIL_HOST_USER=no-reply@sebastiandiazdev.com
ENV EMAIL_HOST_PASSWORD=w=!56S93oK$h

# Expone el puerto 8000 para la aplicación web
EXPOSE 8000

# Ejecuta el comando para iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
