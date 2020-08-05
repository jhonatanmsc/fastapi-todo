from fastapi import HTTPException
from sqlalchemy import Column, String, Integer, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from settings import Base


class CrudOptions:

    @classmethod
    def get(cls, session, id):
        instance = session.query(cls.__tablename__).filter(cls.id == id).first()
        if not instance:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return instance

    @classmethod
    def all(cls, session):
        instances = session.query(cls.__name__).offset(0).limit(100).all()
        if not instances:
            raise HTTPException(status_code=404, detail="User not found")
        else:
            return instances

    def save(self, session):
        session.add(self)
        session.commit()

    def delete(self, session):
        session.delete(self)
        session.commit()


class TaskList(Base, CrudOptions):
    __tablename__ = 'task_lists'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    tasks = relationship('Task')

    def __init__(self, name):
        self.name = name


class Task(Base, CrudOptions):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    is_active = Column(Boolean, default=True)
    task_list_id = Column(Integer, ForeignKey('task_lists.id'))

    def __int__(self, name, due_date, task_list_id):
        self.name = name
        self.due_date = due_date
        self.task_list_id = task_list_id
