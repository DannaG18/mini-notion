from typing import Optional
from sqlalchemy import Column, Integer, String, Enum, DateTime, event
from sqlalchemy.sql import func
from sqlalchemy.orm import validates
from .database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    status = Column(
        Enum('pending', 'in_progress', 'done', name='task_status'),
        default='pending',
        nullable=False
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @validates('title')
    def validate_title(self, key, title):
       
        if not title or len(title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if len(title) > 255:
            raise ValueError("Title is too long (max 255 characters)")
        return title.strip()

    @validates('description')
    def validate_description(self, key, description):
        
        if description and len(description) > 1000:
            raise ValueError("Description is too long (max 1000 characters)")
        return description.strip() if description else None

    def to_dict(self) -> dict:
        """Convert task to dictionary format"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
