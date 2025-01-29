from datetime import datetime
from bson import ObjectId
from fastapi import HTTPException
from app.models.todo import Todo
from typing import List
import motor.motor_asyncio
from app.services.connection_manager import manager

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
db = client.todo_db
todos_collection = db.todos



class TodoService:
    async def get_all_todos(self) -> List[Todo]:
        todos = await todos_collection.find().to_list(100)
        return [serialize_todo_data(todo) for todo in todos] 

    async def create_todo(self, todo: Todo):
        result = await todos_collection.insert_one(todo.dict())
        todo.id = str(result.inserted_id)
        todos = await self.get_all_todos()

        todos = [serialize_todo_data(todo) for todo in todos]

        await manager.broadcast({"action": "update", "todos": todos})

    async def update_todo(self, id: str, todo: Todo) -> Todo:
        result = await todos_collection.update_one({"id": id}, {"$set": todo.dict()})
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

        todos = await self.get_all_todos()
        await manager.broadcast({"action": "update", "todos": todos})

        return todo

    async def delete_todo(self, id: str):
        print("id - ", id);
        result = await todos_collection.delete_one({"id": id})
        print("result called()")
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Todo not found")

        todos = await self.get_all_todos()
        await manager.broadcast({"action": "update", "todos": todos})


def serialize_todo_data(todo):
    if isinstance(todo, dict):
        for key, value in todo.items():
            if isinstance(value, ObjectId):
                todo[key] = str(value)
            elif isinstance(value, datetime):
                todo[key] = value.isoformat()
    return todo



