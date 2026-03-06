# Day 03 — Smart Contracts & Solidity Basics

**Date:** March 06, 2026  
**Status:** ✅ Complete  
**Tool:** Remix IDE (remix.ethereum.org)  
**Network:** Ethereum Sepolia Testnet

---

## 🧠 What I Learned Today

### 1. What is a Smart Contract?
- Code that lives ON the blockchain permanently
- Executes automatically — no middleman needed
- Once deployed, it cannot be changed (immutable)
- Anyone can interact with it via its address

### 2. EVM — Ethereum Virtual Machine
- The "computer" that runs all Ethereum smart contracts
- Every Ethereum node runs the EVM
- Contracts compiled to EVM bytecode before deployment
- EVM is deterministic — same input = same output always

### 3. Solidity Key Concepts

| Concept | What it means |
|---|---|
| `pragma solidity` | Specifies compiler version |
| `contract` | Like a class in Python/Java |
| `state variables` | Stored permanently on-chain |
| `constructor` | Runs once at deployment |
| `msg.sender` | The wallet address calling the function |
| `public` | Anyone can read/call |
| `view` | Read-only, costs no gas |
| `memory` | Temporary, exists during function execution only |

### 4. Gas Explained Simply
- Every operation on Ethereum costs gas
- Read operations (view functions) = FREE
- Write operations (state changes) = costs ETH gas
- Gas prevents spam and pays validators

### 5. State vs Memory vs Storage
```
Storage  → Permanent, on-chain, expensive (state variables)
Memory   → Temporary, in-function only, cheap
Stack    → Very temporary, used for small local vars
```

---

## 📝 Contracts Built Today

### 1. HelloWorld.sol
- Basic message storage contract
- Constructor sets initial message + owner
- `updateMessage()` — changes state (gas required)
- `getMessage()` — reads state (free)

### 2. SimpleStorage.sol
- Stores a number on-chain
- Uses `mapping` — key-value store on blockchain
- Each wallet address stores its own number
- Demonstrates `msg.sender` for per-user data

---

## 🛠️ How to Deploy (Remix IDE)

1. Go to **remix.ethereum.org**
2. Create new file → paste contract code
3. Go to **Solidity Compiler** tab → compile
4. Go to **Deploy & Run** tab
5. Environment → **Injected Provider (MetaMask)**
6. Select **Sepolia testnet** in MetaMask
7. Click **Deploy** → confirm in MetaMask
8. Interact with deployed contract in Remix

---

## 🔗 Key Differences from Day 02

| Day 02 (Python Blockchain) | Day 03 (Solidity Smart Contract) |
|---|---|
| Simulated blockchain locally | Real Ethereum testnet |
| Python code | Solidity code |
| Manual tamper detection | Immutability enforced by EVM |
| No gas concept | Every state change costs gas |
| No wallet interaction | msg.sender = real wallet |

---

## 📚 Resources Used
- [Remix IDE](https://remix.ethereum.org)
- [Solidity Docs](https://docs.soliditylang.org)
- [Solidity by Example](https://solidity-by-example.org)
- [Sepolia Faucet](https://sepoliafaucet.com)

---

## ⏭️ Day 04 Preview
- ERC-20 token standard
- Writing a custom token in Solidity
- Transfer, approve, allowance functions
- Querying token data with Web3.py
