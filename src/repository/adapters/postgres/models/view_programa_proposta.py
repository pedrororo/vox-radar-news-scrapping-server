from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewProgramaProposta(BaseModel):
    id_programa = IntegerField()
    id_proposta = IntegerField()
    json = CharField()

    class Meta:
        primary_key = False
        db_table = 'view_programa_proposta'
        indexes = (
            (('id_programa', 'id_proposta'), True),  # Note the trailing comma!
        )

