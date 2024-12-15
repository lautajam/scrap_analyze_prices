#crud_store/Dockerfile
FROM python:3.11

WORKDIR /app_crud_store/

# Copiar el archivo de requisitos desde el contexto
COPY requirements.txt /app_crud_store/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo del microservicio
COPY crud_store/crud_store.py /app_crud_store/
COPY ../models/ /app_crud_store/models/

EXPOSE 8082

CMD ["python", "crud_store.py"]
