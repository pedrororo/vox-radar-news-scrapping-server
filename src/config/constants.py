class Constants:
  ENVIRONMENT = {
    'LOCAL': 'local',
    'DEVELOP': 'develop',
    'PRODUCTION': 'production'
  }
  PYTHON= {
    'FORMAT_DATETIMEZONE_DEFAULT_SYSTEM': '%Y-%m-%d %H:%M:%S %z', #Ex: 2021-03-10 10:16:04 -0300
    'FORMAT_DATETIME_DEFAULT_SYSTEM': '%Y-%m-%d %H:%M:%S', #Ex: 2021-03-10 10:16:04
    'FORMAT_DATE_DEFAULT_SYSTEM': '%Y-%m-%d', #Ex: 2021-03-10
    'FORMAT_TIME_DEFAULT_SYSTEM': '%H:%M:%S' #Ex: 10:16:04
  }
  TIMEZONE = {
    'SAO_PAULO': {
      'TIMEZONE': 'America/Sao_Paulo',
      'OFFSET_FORMAT_1': '-0300',
      'OFFSET_FORMAT_2': '-03:00'
    }
  },
  ECONOMIA={
    'CIENTES': 'CIENTES',
    'NAO_CIENTES': 'NAO_CIENTES'
  }
  EDUCACAO={
    'PAR2': 'PAR2',
    'PAR3': 'PAR3',
    'PAR4': 'PAR4',
  }
  SQS= {
    'CACHE_KEY': 'SQS:KEY'
  },
  CHUNK = {
    'JSON': 50000,
    'SAVE_DATABASE': 500
  },
  S3={
    'BUCKET': {
      'SIGARP': 'sigarp'
    },
    'PATHS': {
      'EMENDA_PARLAMENTAR_PROCESSED': 'emenda_parlamentar/processed/',
      'EMENDA_PARLAMENTAR_NOT_PROCESSED': 'emenda_parlamentar/not_processed/'
    }
  }
  FACEBOOK = {
    'CHUNCK_LENGHT_ACCOUNT' : 20
  }
  INSTAGRAM = {
    'CHUNCK_LENGHT_ACCOUNT' : 20
  }