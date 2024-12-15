#crud_product/Dockerfile
FROM python:3.11

WORKDIR /app_crud_product/

# Copiar el archivo de requisitos desde el contexto
COPY requirements.txt /app_crud_product/

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el archivo del microservicio
COPY crud_product/crud_product.py /app_crud_product/
COPY ../models/ /app_crud_product/models/

EXPOSE 8081

CMD ["python", "crud_product.py"]
