from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Todo(BaseModel):
    id: Optional[str]
    title: str
    description: Optional[str]
    status: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()
