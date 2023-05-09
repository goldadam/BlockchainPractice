from flask import Flask, request, jsonify, render_template, send_from_directory

from blockchain import Blockchain
import hashlib
from uuid import uuid4
import requests
import sys
import json

app = Flask(__name__)
bitcoin = Blockchain()

node_address = str(uuid4()).replace('-', '')


@app.route('/blockchain', methods=['GET']) #전체 블록을 보여줌
def get_blockchain():
    list = []
    for i in bitcoin.chain:
        list.append(i)
    return jsonify(list)


@app.route('/transaction', methods=['POST']) # pending_transactions에 transaction 추가
def create_transaction():
    new_transaction = request.get_json()
    #blcok_index 정의하시오  blockchain.py의 def add_transaction_to_pending_transactions 사용
    print(new_transaction)
    bitcoin.add_transaction_to_pending_transactions(new_transaction)
    return jsonify({'note': f'Transaction will be added in block {bitcoin.get_last_block()["index"]}.'})


@app.route('/mine', methods=['GET']) # 작업증명
def mine():
    last_block = bitcoin.get_last_block()
    #모든 transaction -> String으로 변환 -> 해시
    k = ""
    for dict in bitcoin.pending_transactions:
        s = ""
        for k, v in dict.items():
            s += str(v)
        k += s
    previous_block_hash = last_block['hash']
    current_block_data = {
        'transactions': last_block.get('transaction'),
        'index': last_block.get('index')
    }
    bitcoin.create_new_transaction(12.5, "00", node_address)
    nonce = bitcoin.proof_of_work(previous_block_hash, current_block_data)
    block_hash = last_block.get('hash')
    new_block = bitcoin.create_new_block(nonce, previous_block_hash, block_hash)
    return jsonify({
        'note': "New block mined successfully",
        'block': new_block
    })

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8000  # 기본 포트 번호를 설정하십시오.
    
    if len(sys.argv) > 2:
        current_node_url = sys.argv[2]
    else:
        current_node_url = f"http://localhost:{port}"
    bitcoin = Blockchain(current_node_url)  # 현재 노드 URL 전달
    app.run(host="0.0.0.0", port=port)