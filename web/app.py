from flask import Flask, jsonify
from core.blockchain import (
  Blockchain,
  compute_proof_of_work,
  compute_block_hash)

app = Flask(__name__)

# initialize blockchain
blockchain = Blockchain()

def start_server():
  print('Starting server...')
  app.run()

@app.route('/mine_block', methods=['POST'])
def mine_block():
  last_block = blockchain.get_last_block()
  proof = compute_proof_of_work(last_block.proof)
  previous_hash = compute_block_hash(last_block)
  block = blockchain.create_block(proof, previous_hash)
  response = {
    'message': 'Congratulations, you just mined a block!',
    'block': block.__dict__
  }
  return jsonify(response), 201
