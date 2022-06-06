from peewee import *
from src.repository.adapters.postgres.postgres import Postgres

class BaseModel(Model):
    class Meta:
        database = Postgres().get_connection_master()
        read_slaves = (Postgres().get_connection_replica())
