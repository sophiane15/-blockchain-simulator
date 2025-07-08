from flask import Flask, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    # À implémenter : réception des données POST
    return "Transaction ajoutée", 201

@app.route('/chain', methods=['GET'])
def full_chain():
    return jsonify({
        "length": len(blockchain.chain),
        "chain": [block.__dict__ for block in blockchain.chain]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
