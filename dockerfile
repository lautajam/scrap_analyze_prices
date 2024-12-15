#main/Dockerfile
FROM python:3.11

WORKDIR /app

# Copiar el archivo de requisitos
COPY requirements.txt /app/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar los archivos del servicio principal
COPY src/ /app/src/
COPY models/ /app/models/

EXPOSE 8080

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]


