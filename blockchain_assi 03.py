import hashlib
import datetime
# BLOCK CLASS (Structure of each block)
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        # Block position in chain
        self.index = index
        # Time when block is created
        self.timestamp = timestamp
        # Data stored in block
        self.data = data
        # Hash of previous block (links the chain)
        self.previous_hash = previous_hash
        # Current block hash (unique ID)
        self.hash = self.calculate_hash()
    # Function to calculate hash using SHA256
    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode()).hexdigest()
# BLOCKCHAIN CLASS (Manages all blocks)
class Blockchain:
    def __init__(self):
        # Create first block (Genesis Block)
        self.chain = [self.create_genesis_block()]
    # First block in blockchain
    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")
    # Get last block in chain
    def get_last_block(self):
        return self.chain[-1]
    # Add new block to chain
    def add_block(self, data):
        last_block = self.get_last_block()
        # Create new block using previous hash
        new_block = Block(
            last_block.index + 1,
            datetime.datetime.now(),
            data,
            last_block.hash
        )
        self.chain.append(new_block)
    # Display entire blockchain
    def display_chain(self):
        for block in self.chain:
            print("\n======================")
            print("Block Index:", block.index)
            print("Timestamp:", block.timestamp)
            print("Data:", block.data)
            print("Previous Hash:", block.previous_hash)
            print("Current Hash:", block.hash)
# MAIN PROGRAM
if __name__ == "__main__":
    # Create blockchain object
    my_blockchain = Blockchain()
    # Add blocks to blockchain
    my_blockchain.add_block("Block 1 Data")
    my_blockchain.add_block("Block 2 Data")
    my_blockchain.add_block("Block 3 Data")
    my_blockchain.add_block("Block 4 Data")
    # Show original blockchain
    print("🔷 ORIGINAL BLOCKCHAIN")
    my_blockchain.display_chain()
    # Tampering demonstration
    print("\n🔴 MODIFYING BLOCK 2 DATA...\n")
    # Change data of block 2
    my_blockchain.chain[2].data = "Hacked Data"
    # Recalculate hash after modification
    my_blockchain.chain[2].hash = my_blockchain.chain[2].calculate_hash()
    # Show modified blockchain
    print("🔷 BLOCKCHAIN AFTER MODIFICATION")
    my_blockchain.display_chain()