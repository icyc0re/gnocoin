from flask import Flask
from core.blockchain import Blockchain

app = Flask(__name__)

# initialize blockchain
blockchain = Blockchain()

def start_server():
  print('Starting server...')
  app.run()
