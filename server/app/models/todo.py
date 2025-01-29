from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import uuid

class Todo(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: Optional[str]
    completed: bool = Field(default=False)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
