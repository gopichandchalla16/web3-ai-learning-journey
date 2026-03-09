# Day 05 — Web3.py + On-Chain Reads
**Date:** March 08, 2026  
**Gopichand Challa | @GopichandAI**

---

## What I Learned Today

### 1. What is Web3.py?
Web3.py is a Python library that lets you interact with the Ethereum blockchain directly from Python code — no browser, no MetaMask, no frontend. It's the Python equivalent of ethers.js (JavaScript).

### 2. What is an RPC Endpoint?
A Remote Procedure Call (RPC) endpoint is the URL your Python script uses to talk to the Ethereum network. Instead of running your own Ethereum node (which takes days and 2TB of storage), you use a provider like Alchemy that runs the node for you and gives you a URL.

```
Your Python Script → Alchemy RPC URL → Ethereum Node → Blockchain
```

### 3. What is an ABI?
ABI = Application Binary Interface. It's a JSON description of all the functions in a smart contract — their names, inputs, and outputs. Web3.py needs the ABI to know how to call the right function on the contract.

Without ABI → Python can't decode what the contract is saying  
With ABI → Python can call any contract function by name

### 4. Read vs Write calls
| Type | Cost | What it does |
|---|---|---|
| Read (view/pure) | **Free** | Returns data from chain — no transaction |
| Write (state change) | **Gas** | Changes blockchain state — needs wallet signature |

Today we only did **reads** — totalSupply, name, symbol, decimals, balanceOf.  
All free. No gas needed.

### 5. Why decimals = 18?
Solidity has no float type. So `1 GOPI token` is stored as `1000000000000000000` (1 × 10¹⁸) on-chain. When reading totalSupply, you divide by `10 ** decimals` to get the human-readable number.

---

## What I Built
- Connected Python to Ethereum Sepolia via Alchemy
- Read live on-chain data from my own $GOPI ERC-20 contract
- Printed: name, symbol, decimals, totalSupply in human-readable form

## Key Takeaway
> The blockchain is a database. Web3.py is how Python talks to it.  
> No backend server needed. The data lives on-chain, forever.

---

## Resources
- [Web3.py Docs](https://web3py.readthedocs.io)
- [Alchemy Free RPC](https://alchemy.com)
- [Ethereum JSON-RPC spec](https://ethereum.org/en/developers/docs/apis/json-rpc/)
