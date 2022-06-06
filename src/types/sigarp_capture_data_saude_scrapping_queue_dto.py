import json

class SigarpCaptureDataSaudeScrappingQueueDTO:
  state:str
  year:int

  def __init__(self, state:str, year:int):
    self.state = state
    self.year = year

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)