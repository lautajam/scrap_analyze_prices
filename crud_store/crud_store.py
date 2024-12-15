from fastapi import FastAPI #type: ignore
from models.Store import Store

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI! This is a Store endpoint!"}

#CRUD STORE
@app.get("crud-store/all-stores")
async def get_all_stores():
    return {"message": "All stores"}

@app.get("crud-store/store/{store_id}")
async def get_store(store_id: int):
    return {"message": f"Store {store_id}"}

@app.post("crud-store/store-create")
async def create_store(store: Store):
    return {"message": "Create store: {store}"}

@app.put("crud-store/store-update/{store_id}")
async def update_store(store_id: int, store: Store):
    return {"message": f"Update store {store_id}, {store}"}

@app.delete("crud-store/store-delete/{store_id}")
async def delete_store(store_id: int):
    return {"message": f"Delete store {store_id}"}