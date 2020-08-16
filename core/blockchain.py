from hashlib import sha256
from datetime import datetime

MAX_PROOF = 2 ** 16
TARGET_HASH = 2 ** 240 # digest with 4 leading zeros

def compute_hash(body):
  return sha256(str(body).encode()).hexdigest()

def is_valid_hash(digest):
  return int(digest, 16) < TARGET_HASH

class Blockchain:
  def __init__(self):
    self.chain = []
    self.create_block(proof = 1, previous_hash = '0')
  
  def create_block(self, proof, previous_hash):
    block = {
      'index': len(self.chain) + 1,
      'timestamp': str(datetime.now()),
      'proof': proof,
      'previous_hash': previous_hash
    }

    self.chain.append(block)
    return block

  def get_previous_block(self):
    return self.chain[-1]
  
  def proof_of_work(self, previous_proof):
    new_proof = 1
    while new_proof < MAX_PROOF:
      new_hash = compute_hash(new_proof**2 - previous_proof**2)
      if is_valid_hash(new_hash):
        return new_proof
      new_proof += 1
    return None
    