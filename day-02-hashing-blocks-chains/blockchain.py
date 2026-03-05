import hashlib
import time

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.data = data
        self.timestamp = str(time.time())
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = str(self.index) + self.data + self.timestamp + self.prev_hash
        return hashlib.sha256(content.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis()]

    def create_genesis(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.prev_hash != prev.hash:
                return False
        return True

    def print_chain(self):
        for block in self.chain:
            print(f"Block    : {block.index}")
            print(f"Data     : {block.data}")
            print(f"Hash     : {block.hash[:20]}...")
            print(f"Prev Hash: {block.prev_hash[:20]}...")
            print("-" * 40)


# Build the chain
bc = Blockchain()
bc.add_block("Gopichand - Day 2 Web3 Learning")
bc.add_block("Building AI Agents On-Chain")
bc.add_block("Block 3 - Future Smart Contracts")

print("=== MY BLOCKCHAIN ===")
bc.print_chain()
print("Chain Valid:", bc.is_valid())

# Tamper with block 1
print("\n=== AFTER TAMPERING BLOCK 1 ===")
bc.chain[1].data = "hacked"
print("Chain Valid:", bc.is_valid())
print("Immutability proven.")
