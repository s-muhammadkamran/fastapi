from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello, World!"}

@app.get("/about")
async def about():
    return {"message": "This is a sample FastAPI application."}

