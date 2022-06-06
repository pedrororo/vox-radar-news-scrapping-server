import os
import json

from ..utils.utils import Utils
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()
 
file = open('src/config/queues.json')
data = json.load(file)

sigarp_saude_scrapping = data['SIGARP_SAUDE_SCRAPPING'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))
sigarp_cidadania_scrapping = data['SIGARP_CIDADANIA_SCRAPPING'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))
sigarp_educacao_scrapping = data['SIGARP_EDUCACAO_SCRAPPING'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))
sigarp_economia_scrapping = data['SIGARP_ECONOMIA_SCRAPPING'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))

sigarp_save_data_saude = data['SIGARP_SAVE_DATA_SAUDE'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))
sigarp_save_data_cidadania = data['SIGARP_SAVE_DATA_CIDADANIA'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))
sigarp_save_data_educacao = data['SIGARP_SAVE_DATA_EDUCACAO'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))
sigarp_save_data_economia = data['SIGARP_SAVE_DATA_ECONOMIA'] + Utils.get_queue_suffix_by_environment(os.environ.get('ENVIRONMENT'))

file.close()

class Envs:
  ENVIRONMENT = os.environ.get('ENVIRONMENT'),
  DATABASE = {
    "LOGGING": os.environ.get('DATABASE_LOGGING'),
    "READ": {
      "NAME": os.environ.get('DATABASE_READ_NAME'),
      "USER": os.environ.get('DATABASE_READ_USER'),
      "PASSWORD": os.environ.get('DATABASE_READ_PASSWORD'),
      "HOST": os.environ.get('DATABASE_READ_HOST'),
      "PORT": os.environ.get('DATABASE_READ_PORT'),
    },
    "WRITE": {
      "NAME": os.environ.get('DATABASE_WRITE_NAME'),
      "USER": os.environ.get('DATABASE_WRITE_USER'),
      "PASSWORD": os.environ.get('DATABASE_WRITE_PASSWORD'),
      "HOST": os.environ.get('DATABASE_WRITE_HOST'),
      "PORT": os.environ.get('DATABASE_WRITE_PORT'),
    }
  }
  ROLLBAR = {
    "KEY": os.environ.get('ROLLBAR_KEY')
  }
  AWS = {
    "ACCOUNT_ID": os.environ.get('AWS_ACCOUNT_ID'),
    "SQS": {
      "KEY": os.environ.get('AWS_SQS_KEY'),
      "SECRET": os.environ.get('AWS_SQS_SECRET'),
      "REGION": os.environ.get('AWS_SQS_REGION'),
      "URL": os.environ.get('AWS_SQS_URL'),
      "QUEUE": {
        "SIGARP_SAUDE_SCRAPPING": sigarp_saude_scrapping,
        "SIGARP_CIDADANIA_SCRAPPING": sigarp_cidadania_scrapping,
        "SIGARP_EDUCACAO_SCRAPPING": sigarp_educacao_scrapping,
        "SIGARP_ECONOMIA_SCRAPPING": sigarp_economia_scrapping,
        "SIGARP_SAVE_DATA_SAUDE": sigarp_save_data_saude,
        "SIGARP_SAVE_DATA_CIDADANIA": sigarp_save_data_cidadania,
        "SIGARP_SAVE_DATA_EDUCACAO": sigarp_save_data_educacao,
        "SIGARP_SAVE_DATA_ECONOMIA": sigarp_save_data_economia
      }
    },
    "S3": {
      "KEY": os.environ.get('AWS_S3_KEY'),
      "SECRET": os.environ.get('AWS_S3_SECRET')
    }
  }
  REDIS = {
    "HOST": os.environ.get('REDIS_HOST'),
    "PORT": os.environ.get('REDIS_PORT'),
    "HAS_AUTHENTICATION": os.environ.get('REDIS_HAS_AUTHENTICATION'),
    "PASSWORD": os.environ.get('REDIS_PASSWORD')
  }
