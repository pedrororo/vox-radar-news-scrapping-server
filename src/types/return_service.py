import json

class ReturnService:
  status:bool
  message:str
  body:any

  def __init__(self, status:bool, message:str, body:any=None):
    self.status = status
    self.message = message
    self.body = body

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)
