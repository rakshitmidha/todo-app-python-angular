from datetime import datetime
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.todo_service import TodoService
from app.models.todo import Todo
from app.services.connection_manager import manager

router = APIRouter()
todo_service = TodoService()

@router.websocket("/ws/todos")
async def websocket_todos(websocket: WebSocket):
    await manager.connect(websocket)
    
    try:
        await send_todos(websocket)

        while True:
            data = await websocket.receive_json()
            
            if "action" not in data:
                await websocket.send_json({"type": "error", "message": "Invalid message format"})
                continue

            
            action_handlers = {
                "add": handle_add,
                "update": handle_update,
                "delete": handle_delete
            }

            action = data.get("action")
            handler = action_handlers.get(action)

            if handler:
                await handler(data, websocket)
            else:
                await websocket.send_json({"type": "error", "message": f"Unknown action: {action}"})

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        print("Client disconnected")



async def handle_add(data, websocket):
    if "todo" in data:
        todo = Todo(**data["todo"])
        await todo_service.create_todo(todo)
        await send_todos(websocket)

async def handle_update(data, websocket):
    if "todo" in data and "id" in data:
        todo = Todo(**data["todo"])
        await todo_service.update_todo(data["id"], todo)
        await send_todos(websocket)

async def handle_delete(data, websocket):
    if "id" in data:
        await todo_service.delete_todo(data["id"])
        await send_todos(websocket)

async def send_todos(websocket):
    todos = await todo_service.get_all_todos()
    todos = [serialize_todo_data(todo) for todo in todos]
    await websocket.send_json({"action": "update", "todos": todos})


# Helper function to handle datetime and ObjectId serialization
def serialize_todo_data(todo):
    if "_id" in todo:
        todo["_id"] = str(todo["_id"])

    # Convert datetime fields to ISO 8601 string format
    for key, value in todo.items():
        if isinstance(value, datetime):
            todo[key] = value.isoformat()
    return todo
