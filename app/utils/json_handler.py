import json
from typing import List, Dict
from datetime import datetime
from models.database import get_db
from models.task_model import Task

def export_to_json(file_path: str) -> None:
    try:
        with get_db() as db: 
            tasks = db.query(Task).all()
            
            data = [{
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "status": t.status,
                "created_at": t.created_at.isoformat() if isinstance(t.created_at, datetime) else None,
                "updated_at": t.updated_at.isoformat() if isinstance(t.updated_at, datetime) else None
            } for t in tasks]
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        
        print(f"Datos exportados correctamente a {file_path}")

    except Exception as e:
        print(f"Error al exportar datos a JSON: {e}")
        raise

import json
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

def import_from_json(file_path: str) -> None:
    try:
     
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("El archivo JSON debe contener una lista de tareas.")

        with get_db() as db:
            for task_data in data:
              
                required_fields = {"title", "description", "status"}
                if not required_fields.issubset(task_data.keys()):
                    print(f"Datos incompletos para la tarea: {task_data}. Se omitirá.")
                    continue

                task_data.pop('created_at', None)
                task_data.pop('updated_at', None)
                task_data.pop('id', None)
                
                new_task = Task(**task_data)
                db.add(new_task)
            
            db.commit()
        
        print(f"Tareas importadas exitosamente desde {file_path}")

    except FileNotFoundError:
        print(f"Archivo no encontrado: {file_path}")
    except json.JSONDecodeError:
        print("Error al procesar el archivo JSON. Verifica que tenga un formato válido.")
    except SQLAlchemyError as e:
        print(f"Error al interactuar con la base de datos: {e}")
        raise
    except Exception as e:
        print(f"Error inesperado: {e}")
        raise
