from pydantic import BaseModel

from models.models import TaskList


class TaskListIn(BaseModel):
    name: str


class TaskListOut(BaseModel):
    id: int
    name: str


class TaskIn(BaseModel):
    name: str
    task_list_id: int


class TaskOut(BaseModel):
    name: str
    task_list_id: int
