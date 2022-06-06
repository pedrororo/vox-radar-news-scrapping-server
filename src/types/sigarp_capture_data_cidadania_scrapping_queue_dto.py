import json

class SigarpCaptureDataCidadaniaScrappingQueueDTO:
  state: str
  city: str
  year: int

  def __init__(self, state: str, city:str, year:int):
    self.state = state
    self.city = city
    self.year = year

  def to_json(self):
    return json.dumps(self.__dict__)

  @classmethod
  def from_json(cls, json_str):
    json_dict = json.loads(json_str)
    return cls(**json_dict)