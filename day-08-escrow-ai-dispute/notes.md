# Day 08 — Escrow Contracts + AI Dispute Arbiter

**Date:** March 14, 2026  
**Author:** Gopichand Challa  
**Repo:** [web3-ai-learning-journey](https://github.com/gopichandchalla16/web3-ai-learning-journey)

---

## What I Learned Today

### 1. Escrow Contract Pattern
- An escrow holds ETH between two parties until a condition is met
- Three roles: **depositor** (client), **beneficiary** (worker), **arbiter** (judge)
- `msg.sender` — Solidity global: address that called the function
- `msg.value` — ETH amount sent with the transaction
- `payable(address).transfer(amount)` — sends ETH to an address

### 2. Key Solidity Concepts Used
```solidity
require(msg.sender == depositor, "Only depositor");  // access control
payable(beneficiary).transfer(amount);               // ETH transfer
emit Released(beneficiary, amount);                  // event logging
```

### 3. AI Arbiter Architecture
```
Dispute reason (string)
       ↓
  LangChain + Groq LLM
       ↓
  VERDICT: RELEASE or REFUND
  REASON: [explanation]
       ↓
  (Day 09) → call release() or refund() on-chain
```

### 4. Why This Matters
- Traditional escrow needs lawyers or trusted humans
- AI arbiter = instant, cheap, 24/7 dispute resolution
- This is actually being built by protocols like Kleros + AI overlays
- The AI reads the same dispute string stored in `Escrow.sol`

---

## Files Built Today

| File | What it does |
|---|---|
| `Escrow.sol` | Solidity escrow contract with dispute + release/refund |
| `ai_arbiter.py` | LangChain + Groq reads dispute → decides RELEASE or REFUND |
| `requirements.txt` | Python dependencies |
| `.env.example` | Environment variable template |

---

## What's Next (Day 09)
- Deploy `Escrow.sol` to Ethereum Sepolia via Remix or Web3.py
- Connect `ai_arbiter.py` to call `release()` or `refund()` on-chain
- This makes the AI arbiter actually execute the verdict on-chain

---

## Concepts to Review
- [ ] What is `msg.sender` vs `tx.origin`?
- [ ] Why use `transfer()` over `call{value: amount}()`?
- [ ] What is a reentrancy attack and how does it relate to escrow?
- [ ] How does Kleros handle decentralized dispute resolution?
