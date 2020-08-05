import pdb

from fastapi import HTTPException, Depends

from settings import app, SessionLocal
from models.models import TaskList, Task
from sqlalchemy.orm import Session

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def dashboard(db: Session = Depends(get_db)):
    tl = db.query(TaskList).all()
    return {"dashboard": tl.name}


@app.post("/task-list")
def create_task_list(db: Session = Depends(get_db)):
    tl = TaskList('todo')
    tl.save(db)
    return {'item': tl.name}


@app.delete("/task-list/{task_list_id}")
def create_task_list(task_list_id, db: Session = Depends(get_db)):
    tl = TaskList.get(db, task_list_id)
    return {'item': tl}


@app.post("/stock")
def create_stock():
    return {
        "code": "success",
        "message": "stock created"
    }
