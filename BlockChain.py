import hashlib
import json
from time import time
from uuid import  uuid4
from flask import Flask


class Blockchain(object):

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        #Generate genesis block, block with no previous blocks before hand
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        block = {
            'index': len(self.chain) +1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self):


        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        pass


    @property
    def last_block(self):
        pass


app = Flask(__name__)

node_identifier = str(uuid4()).replace('-',''))