# 🔗 AI × Web3 Learning Journey

> **Gopichand Challa** — Building in public. One day, one concept, one commit.

[![X](https://img.shields.io/badge/X-@GopichandAI-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/GopichandAI)
[![GitHub](https://img.shields.io/badge/GitHub-gopichandchalla16-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gopichandchalla16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Gopichand%20Challa-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gopichandchalla)
[![Gmail](https://img.shields.io/badge/Gmail-gopichandchalla516-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:gopichandchalla516@gmail.com)

---

## 🎯 Mission

Learn AI × Web3 from zero to builder — publicly, daily, with real code as proof.

No tutorials without code. No learning without shipping. Every day has a commit.

---

## 📂 Repository Structure

```
web3-ai-learning-journey/
├── day-01-wallets-transactions/
│   ├── notes.md
│   └── metamask-setup.md
├── day-02-hashing-blocks-chains/
│   ├── blockchain.py
│   ├── notes.md
│   └── sha256-demo.md
├── day-03-smart-contracts/
│   ├── HelloWorld.sol
│   ├── SimpleStorage.sol
│   ├── notes.md
│   └── evm-explained.md
├── day-04-erc20-tokens/
│   ├── GopichandToken.sol
│   ├── notes.md
│   └── erc20-explained.md
├── day-05-web3py-onchain-reads/
│   ├── query_gopi_token.py
│   ├── notes.md
│   └── web3py-explained.md
├── day-06-ai-agent-onchain/      ← TODAY ✅
│   ├── wallet_agent.py
│   ├── notes.md
│   └── langchain-web3-explained.md
├── day-07-full-project/          ← coming tomorrow
└── README.md
```

---

## 📊 Daily Learning Log

| Day | Date | Topic | Build | Status |
|:---:|:---|:---|:---|:---:|
| ✅ 01 | Mar 04, 2026 | Wallets, Transactions, MetaMask | MetaMask setup + first test ETH | Done |
| ✅ 02 | Mar 05, 2026 | Hashing, Blocks, Chains, PoW vs PoS | [Mini Blockchain in Python](./day-02-hashing-blocks-chains/blockchain.py) | Done |
| ✅ 03 | Mar 06, 2026 | Smart Contracts, Solidity, EVM | [HelloWorld.sol](./day-03-smart-contracts/HelloWorld.sol) + [SimpleStorage.sol](./day-03-smart-contracts/SimpleStorage.sol) | Done |
| ✅ 04 | Mar 07, 2026 | ERC-20 Tokens, Standards, DeFi patterns | [GopichandToken.sol](./day-04-erc20-tokens/GopichandToken.sol) — $GOPI token | Done |
| ✅ 05 | Mar 08, 2026 | Web3.py — Reading live on-chain data | [query_gopi_token.py](./day-05-web3py-onchain-reads/query_gopi_token.py) — Python reads wallets live | Done |
| ✅ 06 | Mar 09, 2026 | AI Agent on-chain — LangChain + Web3.py | [wallet_agent.py](./day-06-ai-agent-onchain/wallet_agent.py) — AI reads blockchain | Done |
| ⏳ 07 | Mar 10, 2026 | Full AI × Web3 mini project | Coming | Upcoming |

---

## 🔥 Key Concepts Covered So Far

### Day 1 — Wallets & Transactions
- What is a crypto wallet (EOA)
- Public key vs private key
- How transactions are signed and broadcast
- MetaMask setup on Ethereum Sepolia testnet

### Day 2 — Hashing, Blocks & Chains
- SHA-256 hashing — deterministic, one-way
- How blocks chain together via prev_hash
- What is a nonce and Proof of Work
- Proof of Work vs Proof of Stake (The Merge)
- Built a working blockchain in 60 lines of Python
- Proved immutability by tampering and breaking the chain

### Day 3 — Smart Contracts & Solidity
- What is a Smart Contract and how EVM executes it
- Solidity syntax: pragma, contract, constructor, functions
- State variables vs memory vs storage
- msg.sender — the caller's wallet address
- Gas — why every state change costs ETH
- View functions — free read-only calls
- Deployed HelloWorld.sol + SimpleStorage.sol on Sepolia

### Day 4 — ERC-20 Tokens 🪙
- What is ERC-20 and why standards matter
- Core token functions: transfer, approve, transferFrom, mint, burn
- The approve → transferFrom pattern (how DeFi works)
- Why decimals = 18 (no floats in Solidity)
- Events: Transfer and Approval logged permanently on-chain
- Built GopichandToken ($GOPI) — 1,000,000 supply ERC-20 from scratch

### Day 5 — Web3.py + On-Chain Reads 🐍
- What is Web3.py and why Python devs need it for Web3
- How to connect to Ethereum via Alchemy RPC endpoint
- What an ABI is and why Web3.py needs it
- Reading on-chain state: balanceOf, totalSupply, decimals
- Read Vitalik's live wallet balance — 42.98 ETH on Sepolia

### Day 6 — AI Agent on-chain 🤖
- What is a LangChain agent and how tools work
- How to give an LLM a Web3.py tool
- Agent reads any wallet address on Ethereum
- LLM explains the balance in plain English
- The bridge between AI and blockchain is just a Python function

---

## 🛠️ Tech Stack

```
Languages  : Python, Solidity
AI Stack   : LLMs, LangChain, OpenAI, Groq (Llama 3)
Web3 Stack : Ethereum, Web3.py, MetaMask, Remix IDE, Etherscan, Alchemy
Tools      : VS Code, Git, GitHub, Google Colab
```

---

## 🪙 Tokens Built

| Token | Symbol | Supply | Day | File |
|---|---|---|---|---|
| GopichandToken | $GOPI | 1,000,000 | Day 04 | [GopichandToken.sol](./day-04-erc20-tokens/GopichandToken.sol) |

---

## 📌 How to Follow This Journey

1. **Star this repo** — get notified on every new day
2. **Follow on X** — [@GopichandAI](https://x.com/GopichandAI) for daily tweets
3. **Connect on LinkedIn** — [Gopichand Challa](https://www.linkedin.com/in/gopichandchalla)

> *Every commit here is proof of work. Not just a concept — a practice.*
