from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel
import datetime

class ViewProponenteLog(BaseModel):
    id = PrimaryKeyField()
    log = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField()
    deleted_at = DateTimeField()

    class Meta:
        db_table = 'view_proponente_log'
