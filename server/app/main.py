from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.routers import todos
from app.services.connection_manager import manager

app = FastAPI()

origins = [
    "http://localhost:4200",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router, prefix="/api")

@app.websocket("/ws/todos")
async def websocket_todos(websocket: WebSocket):
    await websocket.accept()
