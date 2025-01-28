from fastapi import HTTPException
from app.models.todo import Todo
from typing import List
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.todo_db
todos_collection = db.todos

class TodoService:
    async def get_all_todos(self) -> List[Todo]:
        todos = await todos_collection.find().to_list(100)
        
        return todos

    async def create_todo(self, todo: Todo) -> Todo:
        result = await todos_collection.insert_one(todo.dict())
        todo.id = str(result.inserted_id)
        
        return todo

    async def update_todo(self, id: str, todo: Todo) -> Todo:
        result = await todos_collection.update_one({"_id": id}, {"$set": todo.dict()})
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")
        
        return todo

    async def delete_todo(self, id: str):
        result = await todos_collection.delete_one({"_id": id})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")
