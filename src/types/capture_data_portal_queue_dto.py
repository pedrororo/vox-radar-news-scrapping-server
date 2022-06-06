import json

class CaptureDataPortalQueueDTO:
  url:str

  def __init__(self, url:list):
    self.url = url

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)