from fastapi import FastAPI
from app.routers import todos

app = FastAPI()

app.include_router(todos.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Todo API"}
