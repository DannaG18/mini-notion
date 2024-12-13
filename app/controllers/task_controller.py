from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.database import get_db
from models.task_model import Task
from loguru import logger

def create_task(title: str, description: Optional[str] = None) -> Optional[Task]:
    """
    Create a new task with validation
    
    Args:
        title (str): Task title
        description (Optional[str]): Task description
    
    Returns:
        Optional[Task]: Created task or None if creation failed
    """
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
    """
    Retrieve tasks, optionally filtered by status
    
    Args:
        status (Optional[str]): Filter tasks by status
    
    Returns:
        List[Task]: List of tasks
    """
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
    """
    Update task status
    
    Args:
        task_id (int): ID of the task to update
        status (str): New status
    
    Returns:
        bool: Whether update was successful
    """
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
    """
    Delete a task by its ID
    
    Args:
        task_id (int): ID of the task to delete
    
    Returns:
        bool: Whether deletion was successful
    """
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