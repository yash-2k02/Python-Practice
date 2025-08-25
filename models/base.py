from datetime import datetime, timezone
from sqlmodel import SQLModel, Field
from typing import Optional
from sqlalchemy import event

class AuditBase(SQLModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_by: str
    updated_by: Optional[str] = None
    is_deleted: bool = Field(default=False)


def register_audit_listeners(model_class):
    
    @event.listens_for(model_class, "before_insert")
    def set_updated_by(mapper, connection, target):
        if not target.updated_by:
            target.updated_by = target.created_by

    @event.listens_for(model_class, "before_update")
    def update_timestamp(mapper,connection,target):
        target.updated_at = datetime.now(timezone.utc)