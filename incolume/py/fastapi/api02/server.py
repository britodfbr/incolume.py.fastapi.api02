from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"hello": "world"}

@app.get("/items/{item}")
async def subpage(item: str):
    return {"item": item}