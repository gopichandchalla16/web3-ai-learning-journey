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

## Connect to Ethereum (Safe Way)
```python
from web3 import Web3
import os

# Load from environment variable — never hardcode API keys!
ALCHEMY_URL = os.environ.get("ALCHEMY_URL")

w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
print(w3.is_connected())    # True
print(w3.eth.block_number)  # latest block number
```

---

## Get ETH Balance of Any Wallet
```python
address = "0xYourWalletAddress"
balance_wei = w3.eth.get_balance(Web3.to_checksum_address(address))
balance_eth = w3.from_wei(balance_wei, 'ether')
print(f"Balance: {balance_eth:.4f} ETH")
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

## ⚠️ Security Rules

```
NEVER do this:
ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/abc123"  ❌

ALWAYS do this:
ALCHEMY_URL = os.environ.get("ALCHEMY_URL")  ✅
```

1. Create a `.env` file locally with your real key
2. Add `.env` to your `.gitignore`
3. Only commit `.env.example` with placeholder values
4. Never paste real keys in code you push to GitHub

---

## What's Next (Day 06)
Combine Web3.py with LangChain to build an AI agent that reads wallet balances and explains them in plain English.
