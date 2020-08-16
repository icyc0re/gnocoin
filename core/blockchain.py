from hashlib import sha256
from datetime import datetime
from .block import Block
import json

MAX_PROOF = 2 ** 16
TARGET_HASH = 2 ** 240 # digest with 4 leading zeros

def compute_hash(body: str):
  """ Compute hash of any string body """
  return sha256(str(body).encode()).hexdigest()

def compute_block_hash(block):
  return sha256(block.as_json().encode()).hexdigest()

def is_valid_hash(hexdigest):
  return int(hexdigest, 16) < TARGET_HASH

def proof_computation(proof, previous_proof):
  return proof**2 - previous_proof**2

def compute_proof_of_work(previous_proof):
  """ Calculate the proof of work (mine) """
  new_proof = 1
  while new_proof < MAX_PROOF:
    new_hash = compute_hash(proof_computation(new_proof, previous_proof))
    if is_valid_hash(new_hash):
      return new_proof
    new_proof += 1
  return None

class Blockchain:
  def __init__(self):
    self.chain = []
    self.create_block(proof = 1, previous_hash = '0')
  
  def create_block(self, proof, previous_hash):
    """ Create a new block and append it at the end of the chain """
    block = Block(
      index = len(self.chain) + 1,
      timestamp = str(datetime.now()),
      proof = proof,
      previous_hash = previous_hash
    )
    self.chain.append(block)
    return block

  def get_last_block(self):
    """ Get the last block """
    return self.chain[-1]
  
  def is_chain_valid(self):
    """
    Check if the blockchain is valid
    
    Checks:
    - block index is sequentially increasing
    - the "previous_hash" entry matches the hash of the previous node
    - the proof of work results in a valid hash
    """
    previous_block = self.chain[0]
    for block in self.chain[1:]:
      if (block.index != previous_block.index + 1 or
          block.previous_hash != compute_block_hash(previous_block) or
          not is_valid_hash(compute_hash(proof_computation(block.proof, previous_block.proof)))):
        return False
      previous_block = block
    return True
