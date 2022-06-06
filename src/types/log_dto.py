import json

class LogDTO:
  log:str

  def __init__(self, id:int, log:str):
    if id:
      self.id = id
      
    self.log = log

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)
