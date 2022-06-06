from peewee import *
from src.repository.adapters.postgres.models.base import BaseModel

class ViewParlamentar(BaseModel):
    id = IntegerField(primary_key=True)
    parlamentar_id = IntegerField()
    nome = CharField()
    partido = CharField()
    uf = CharField()
    email = CharField()
    foto = CharField()
    conta_facebook = CharField()
    conta_instagram = CharField()
    conta_twitter = CharField()
    cargo = CharField()
    active = BooleanField()
    json = CharField()

    class Meta:
        db_table = 'view_parlamentar'
        indexes = (
            (('parlamentar_id', 'nome'), True),  # Note the trailing comma!
        )
