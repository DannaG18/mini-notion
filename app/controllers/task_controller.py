from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.database import get_db
from models.task_model import Task
from loguru import logger

def create_task(title: str, description: Optional[str] = None) -> Optional[Task]:

    try:
        with get_db() as db:
            new_task = Task(
                title=title,
                description=description
            )
            db.add(new_task)
            db.flush()  # Validate the object before committing
            return new_task
    except ValueError as ve:
        # Validation errors
        logger.error(f"Validation error creating task: {ve}")
        return None
    except SQLAlchemyError as e:
        logger.error(f"Database error creating task: {e}")
        return None

def get_tasks(status: Optional[str] = None) -> List[Task]:

    try:
        with get_db() as db:
            query = db.query(Task)
            if status:
                query = query.filter(Task.status == status)
            return query.order_by(Task.id.desc()).all()
    except SQLAlchemyError as e:
        logger.error(f"Error fetching tasks: {e}")
        return []

def update_task_status(task_id: int, status: str) -> bool:

    try:
        with get_db() as db:
            task = db.query(Task).filter(Task.id == task_id).first()
            if task:
                task.status = status
                db.flush()  # Validate before committing
                return True
            return False
    except ValueError as ve:
        logger.error(f"Validation error updating task: {ve}")
        return False
    except SQLAlchemyError as e:
        logger.error(f"Database error updating task status: {e}")
        return False

def delete_task(task_id: int) -> bool:

    try:
        with get_db() as db:
            task = db.query(Task).filter(Task.id == task_id).first()
            if task:
                db.delete(task)
                return True
            return False
    except SQLAlchemyError as e:
        logger.error(f"Error deleting task: {e}")
        return False