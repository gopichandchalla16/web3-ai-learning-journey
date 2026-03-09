# Web3.py Explained — For Python Developers Entering Web3
**Gopichand Challa | @GopichandAI | Day 05**

---

## The One-Line Explanation
Web3.py is `requests` + `json` + `crypto` for Ethereum.  
It handles the low-level protocol so you can just call Python functions.

---

## Installation
```bash
pip install web3
```

---

## Connect to Ethereum
```python
from web3 import Web3

# Option 1: Alchemy (recommended, free)
w3 = Web3(Web3.HTTPProvider("https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY"))

# Option 2: Local node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

print(w3.is_connected())    # True
print(w3.eth.block_number)  # latest block number
```

---

## Read From Any ERC-20 Token
```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("YOUR_ALCHEMY_URL"))

abi = [
    {"inputs": [], "name": "name",        "outputs": [{"type": "string"}],  "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "totalSupply", "outputs": [{"type": "uint256"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "decimals",    "outputs": [{"type": "uint8"}],   "stateMutability": "view", "type": "function"},
]

contract = w3.eth.contract(address=Web3.to_checksum_address("CONTRACT_ADDRESS"), abi=abi)

print(contract.functions.name().call())          # GopichandToken
print(contract.functions.totalSupply().call())   # 1000000000000000000000000
print(contract.functions.decimals().call())      # 18
```

---

## Key Web3.py Concepts

| Concept | What it is |
|---|---|
| `Web3.HTTPProvider` | Connects to Ethereum via HTTP RPC |
| `w3.eth.contract()` | Creates a Python object from contract address + ABI |
| `.call()` | Executes a read (no gas, no tx) |
| `.transact()` | Executes a write (costs gas, needs private key) |
| `Web3.to_checksum_address()` | Converts address to EIP-55 checksum format |
| `w3.eth.get_balance()` | Gets ETH balance of any address (in Wei) |
| `w3.from_wei(balance, 'ether')` | Converts Wei to ETH |

---

## Get ETH Balance of Any Wallet
```python
address = "0xYourWalletAddress"
balance_wei = w3.eth.get_balance(Web3.to_checksum_address(address))
balance_eth = w3.from_wei(balance_wei, 'ether')
print(f"Balance: {balance_eth:.4f} ETH")
```

---

## What's Next (Day 06)
Combine Web3.py with LangChain to build an AI agent that:  
→ Takes a wallet address as input  
→ Reads the ETH balance on-chain  
→ Returns a plain-English summary using an LLM

That's the bridge between AI and Web3.
