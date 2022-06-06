from peewee import *
from src.config.envs import Envs

class Postgres:
  __connection_master = None
  __connection_replica = None

  def __init__(self):
    self.__connection_master = PostgresqlDatabase(Envs.DATABASE['WRITE']['NAME'], user=Envs.DATABASE['WRITE']['USER'], password=Envs.DATABASE['WRITE']['PASSWORD'], host=Envs.DATABASE['WRITE']['HOST'], port=Envs.DATABASE['WRITE']['PORT'], sslmode='require')
    self.__connection_replica = PostgresqlDatabase(Envs.DATABASE['READ']['NAME'], user=Envs.DATABASE['READ']['USER'], password=Envs.DATABASE['READ']['PASSWORD'], host=Envs.DATABASE['READ']['HOST'], port=Envs.DATABASE['READ']['PORT'], sslmode='require')

  def get_connection_master(self):
    return self.__connection_master

  def get_connection_replica(self):
    return self.__connection_replica
