from blockchain import Blockchain

def validate_block(blockchain):
    for i in range(1, len(blockchain.chain)):
        current_block = blockchain.chain[i]
        previous_block = blockchain.chain[i-1]
        
        if current_block.hash != current_block.calculate_hash():
            return False
        if current_block.previous_hash != previous_block.hash:
            return False
    
    return True

def main():
    blockchain = Blockchain()
    blockchain.mine_pending_transactions()  # Simule un mineur
    
    print("Blockchain valide ?", validate_block(blockchain))

if __name__ == "__main__":
    main()
