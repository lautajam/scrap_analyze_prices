from fastapi import FastAPI #type: ignore
from models.Product import Product

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI! This is a Product endpoint!"}

#CRUD PRODUCT
@app.get("crud-product/all-products")
async def get_all_products():
    return {"message": "All products"}

@app.get("crud-product/product/{product_id}")
async def get_product(product_id: int):
    return {"message": f"Product {product_id}"}

@app.post("crud-product/product-create")
async def create_product(product: Product):
    return {"message": "Create product: {product}"}

@app.put("crud-product/product-update/{product_id}")
async def update_product(product_id: int, product: Product):
    return {"message": f"Update product {product_id}, {product}"}

@app.delete("crud-product/product-delete/{product_id}")
async def delete_product(product_id: int):
    return {"message": f"Delete product {product_id}"}