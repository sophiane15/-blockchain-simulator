from blockchain import Blockchain

def main():
    blockchain = Blockchain()
    
    # Exemple de transactions
    blockchain.add_transaction("Alice", "Bob", 5)
    blockchain.add_transaction("Bob", "Charlie", 3)
    
    print("Transactions en attente :", blockchain.pending_transactions)

if __name__ == "__main__":
    main()
