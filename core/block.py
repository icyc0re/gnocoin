import json

class Block:
  def __init__(self, index, timestamp, proof, previous_hash):
    self.index = index
    self.timestamp = timestamp
    self.proof = proof
    self.previous_hash = previous_hash

  def as_dict(self):
    return self.__dict__

  def as_json(self):
    return json.dumps(self.as_dict(), sort_keys=True, separators=(',', ':'))
