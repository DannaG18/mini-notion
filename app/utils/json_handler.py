import json
from typing import List, Dict
from datetime import datetime
from models.database import get_db
from models.task_model import Task

def export_to_json(file_path: str) -> None:
    with get_db() as db:
        tasks = db.query(Task).all()
        data = [{
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "created_at": t.created_at.isoformat() if t.created_at else None,
            "updated_at": t.updated_at.isoformat() if t.updated_at else None
        } for t in tasks]
        
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

def import_from_json(file_path: str) -> None:
    with get_db() as db:
        with open(file_path, "r") as f:
            data = json.load(f)
        
        for task_data in data:
           
            task_data.pop('created_at', None)
            task_data.pop('updated_at', None)
            task_data.pop('id', None)
            
            new_task = Task(**task_data)
            db.add(new_task)