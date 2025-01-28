from fastapi import APIRouter, HTTPException
from app.models.todo import Todo
from app.services.todo_service import TodoService

router = APIRouter()
todo_service = TodoService()

@router.get("/todos", response_model=list[Todo])
async def get_todos():
    return await todo_service.get_all_todos()

@router.post("/todos", response_model=Todo)
async def create_todo(todo: Todo):
    return await todo_service.create_todo(todo)

@router.put("/todos/{id}", response_model=Todo)
async def update_todo(id: str, todo: Todo):
    return await todo_service.update_todo(id, todo)

@router.delete("/todos/{id}")
async def delete_todo(id: str):
    await todo_service.delete_todo(id)
    
    return {"message": "Todo deleted successfully"}
