# Day 08 — Project Breakdown

## Project: Escrow Contract + AI Dispute Resolution

### The Problem It Solves
In freelance/DeFi, disputes happen. Who holds the ETH? Who decides?
Traditional answer: lawyers, banks, human judges. All slow and expensive.
This project: a smart contract holds the ETH + an AI decides who gets it.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                 ESCROW FLOW                         │
├─────────────────────────────────────────────────────┤
│  1. Depositor deploys Escrow.sol                    │
│     (sets beneficiary + arbiter address)            │
│                    ↓                                │
│  2. Depositor calls deposit() → ETH locked          │
│                    ↓                                │
│  3. Dispute? Either party calls raiseDispute()      │
│     → stores reason string on-chain                 │
│                    ↓                                │
│  4. AI reads disputeReason from contract            │
│     → LangChain + Groq decides RELEASE or REFUND   │
│                    ↓                                │
│  5. Arbiter wallet calls release() or refund()      │
│     → ETH moves to winner                          │
└─────────────────────────────────────────────────────┘
```

---

## Code Files

### Escrow.sol
- `deposit()` — locks ETH, only depositor can call
- `raiseDispute(reason)` — either party calls with dispute text
- `release()` — arbiter sends ETH to beneficiary
- `refund()` — arbiter returns ETH to depositor
- `getBalance()` — view current locked amount

### ai_arbiter.py
- Loads `GROQ_API_KEY` from `.env`
- Sends dispute reason to `llama3-8b-8192` via LangChain
- System prompt forces structured output: `VERDICT: RELEASE/REFUND`
- Runs 5 test cases simulating real escrow disputes

---

## Test Results (Expected)

| Case | Scenario | Expected Verdict |
|:---:|---|---|
| 1 | Delivered on time, client refuses | RELEASE |
| 2 | No delivery, developer went silent | REFUND |
| 3 | Critical security bug found | Depends on scope |
| 4 | Client changed requirements | RELEASE |
| 5 | Partial delivery | REFUND or partial |

---

## Day 09 Extension Plan
```python
# Connect ai_arbiter.py to call the contract on-chain
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(os.getenv("ALCHEMY_RPC_URL")))
contract = w3.eth.contract(address=ESCROW_ADDRESS, abi=ESCROW_ABI)

# If AI says RELEASE:
contract.functions.release().transact({"from": arbiter_wallet})

# If AI says REFUND:
contract.functions.refund().transact({"from": arbiter_wallet})
```
