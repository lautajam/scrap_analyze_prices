from fastapi import FastAPI #type: ignore

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI! This is a main endpoint!"}

@app.get("/meli_scrap")
async def meli_scrap():
    return {"message": "This is a Meli_Scrap endpoint!"}