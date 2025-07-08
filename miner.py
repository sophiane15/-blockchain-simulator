from blockchain import Blockchain

def main():
    blockchain = Blockchain()
    
    # Miner les transactions en attente
    if blockchain.pending_transactions:
        blockchain.mine_pending_transactions()
        print("Dernier bloc miné :", blockchain.chain[-1].__dict__)
    else:
        print("Aucune transaction à miner !")

if __name__ == "__main__":
    main()
