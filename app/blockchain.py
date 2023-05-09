import time
import hashlib
import json
import datetime as dt
from uuid import uuid4

class Blockchain:
    def __init__(self, current_node_url=None):
        self.chain = []
        self.pending_transactions = []
        self.create_new_block(50,'0','0') # 제네시스 블럭

    def create_new_block(self, nonce, previous_block_hash, hash_):  #새로운 block 만드는 메서드
        new_block = {
            'index': len(self.chain) ,
            'timestamp': str(dt.datetime.now()),
            'transactions': self.pending_transactions,
            'nonce': nonce,
            'hash': hash_,
            'previous_block_hash': previous_block_hash
        }
        self.pending_transactions = [] #pending_transaction 초기화
        self.chain.append(new_block)
        return new_block
    
    def get_last_block(self): #마지막 블럭 가져오는 메서드
        return self.chain[-1]
    
    def create_new_transaction(self,amount,sender,recipient): #새로운 transaction 만드는 메서드
        new_transaction = {
            'amount' : amount,
            'sender' : sender,
            'recipient' : recipient
        }
        return new_transaction

    def hash_block(self, previous_block_hash, current_block_data, nonce): #hash 값으로는 편의를 위해 전 블럭의 해쉬값, nonce값, current_block_data가 들어갑니다
        data_as_string = json.dumps(current_block_data, sort_keys=True) + str(nonce) + previous_block_hash                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        hash_object = hashlib.sha256(data_as_string.encode())
        hash_ = hash_object.hexdigest()
        return hash_
    
    def proof_of_work(self,previous_block_hash, current_block_data):
        nonce = 0
        current_block_data = json.dumps(current_block_data, sort_keys=True)
        hash_ = self.hash_block(previous_block_hash, current_block_data, nonce)
        #nonce 값 조정하면서 반복문 만드시오
        while(str(hash_[0:4]) != '0000'):
            nonce += 1
            hash_ = self.hash_block(previous_block_hash, current_block_data, nonce)
        return nonce
    
    def add_transaction_to_pending_transactions(self,transaction_obj):
        # pending_transaction에 추가하시오
        self.pending_transactions.append(transaction_obj)
        return self.get_last_block()['index'] + 1
    