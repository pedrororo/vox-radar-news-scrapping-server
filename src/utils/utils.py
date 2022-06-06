import re
from src.config.constants import Constants
import requests
from urllib.parse import urlparse
import pytz
from dateutil.tz.tz import tzoffset
from datetime import datetime, timedelta
import pandas
import os.path
import unicodedata
import regex

class Utils:

  @classmethod
  def remove_accent_chars_regex(self, text: str):
    return regex.sub(r'\p{Mn}', '', unicodedata.normalize('NFKD', text))
  
  @classmethod
  def get_extension(self, file_name:str):
    return os.path.splitext(file_name)[1]

  @classmethod
  def remove_extension(self, file_name:str):
    extension = os.path.splitext(file_name)[1]
    return file_name.replace(extension,'')

  @classmethod
  def get_datetime_now(self):
    return datetime.now(pytz.timezone(Constants.TIMEZONE[0]['SAO_PAULO']['TIMEZONE']))

  @classmethod
  def has_numbers(self, input_string):
    return any(char.isdigit() for char in input_string)

  @classmethod
  def only_numbers(self, input_string):
    return re.sub(r"\D", '', input_string)

  @classmethod
  def transform_number(self, number_text:str) -> int:
    only_text = re.sub(r"[^A-Za-z]+", '', number_text).strip().lower()
    only_number = re.sub(r"\D", '', number_text)
    if(only_text == "mil"):
      return int(only_number) * 1000
    else:
      return int(only_number)

  @classmethod
  def format_date_br_to_universal(self, date:str) -> str:
    if not date:
      return None

    try:
      date_parsed = datetime.strptime(date, '%d/%m/%Y').date()
      if date_parsed.year > 1900:
        return date_parsed.strftime('%Y-%m-%d')
      else:
        print(f'This is the incorrect date string format | {date}')
        return None

    except Exception:
      print(f'This is the incorrect date string format | {date}')
      return None

  @classmethod
  def format_date_universal_to_br(self, date:str) -> str:
    try:
      date_parsed = datetime.strptime(date, '%Y-%m-%d').date()
      if date_parsed.year > 1900:
        return date_parsed.strftime('%d/%m/%Y')
      else:
        print(f'This is the incorrect date string format | {date}')
        return None

    except Exception:
      print(f'This is the incorrect date string format | {date}')
      return None

  @classmethod
  def getQueueSuffixByEnvironment(self, environment: str) -> str:
    if environment == Constants.ENVIRONMENT['LOCAL']:
      return '_LOCAL'
    if environment == Constants.ENVIRONMENT['DEVELOP']:
      return '_DEVELOP'
    else:
      return ''

  @classmethod
  def remove_duplicate(self, list:list, key:str) -> list:
    memo = set()
    res = []
    for sub in list:
      if sub[key] not in memo:
        res.append(sub)
        memo.add(sub[key])

    return res

  @classmethod
  def to_int(self, value) -> int:
    if not value:
      return None
    else:
      return int(value)

  @classmethod
  def to_float(self, value) -> float:
    if not value:
      return None
    else:
      return float(str(value).replace(',','.'))

  @classmethod
  def check_int(self, value):
    if value:
      return re.match(r"[-+]?\d+(\.0*)?$", str(value)) is not None
    return None

  @classmethod
  def truncate_text(self, text:str, size:int):
    if(len(text) > size):
      return text[0:size] + '...'
    else:
      return text

  @classmethod
  def remove_links(self, text:str):
    return re.sub(r'http\S+', '', text)

  @classmethod
  def get_datetime_now(self):
    return datetime.now(pytz.timezone(Constants.TIMEZONE[0]['SAO_PAULO']['TIMEZONE']))

  @classmethod
  def normalize_url(self, url:str):
    decoded = self.decode_url(url)
    return decoded.rstrip("/")

  @classmethod
  def decode_url(self, url:str):
    parsed = urlparse(url)
    return parsed.scheme + '://' + parsed.netloc + parsed.path
  
  @classmethod
  def get_domain_url(self, url:str):
    parsed = urlparse(url)
    return parsed.netloc

  @classmethod
  def get_long_url(self, short_url):
    try:
        r = requests.get(short_url)
    except requests.exceptions.RequestException:
        return (short_url, None)

    if r.status_code != 200:
        long_url = None
    else:
        long_url = r.url

    return long_url

  @classmethod
  def get_urls_from_text(self, text):    
    links = re.findall(r'(https?://\S+)', text)
    long_links = [self.get_long_url(link) for link in links]
    return long_links

  @classmethod
  def has_numbers(self, input_string):
    return any(char.isdigit() for char in input_string)

  @classmethod
  def only_numbers(self, input_string):
    return re.sub(r"\D", '', input_string)

  @classmethod
  def get_queue_suffix_by_environment(self, environment: str) -> str:
    if environment == Constants.ENVIRONMENT['LOCAL']:
      return '_LOCAL'
    if environment == Constants.ENVIRONMENT['DEVELOP']:
      return '_DEVELOP'
    else:
      return ''

  @classmethod
  def transform_number(self, number_text:str) -> int:
    only_text = re.sub(r"[^A-Za-z]+", '', number_text).strip().lower()
    only_number = re.sub(r"\D", '', number_text)
    if(only_text == "mil"):
      return int(only_number) * 1000
    else:
      return int(only_number)

  @classmethod
  def subtract_day_from_datetime(datetime:datetime, days:int) -> datetime:
    _days = timedelta(days)
    return datetime - _days
