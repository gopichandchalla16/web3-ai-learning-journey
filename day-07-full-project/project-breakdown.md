# Project Breakdown — AI Wallet Analyser
**Gopichand Challa | Day 07**

---

## What It Does

Input any Ethereum wallet address → get a full AI-generated report:

```
AI WALLET REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wallet   : 0xd8dA...6045
Network  : Ethereum Sepolia Testnet
Block    : 10420100 | 2026-03-10 09:42 UTC
──────────────────────────────────────────────────
💰 Balance  : 43.001343 ETH
📤 Tx Count : 1,842 transactions sent
📊 Activity : highly active
──────────────────────────────────────────────────
🤖 AI Summary:
This wallet holds 43.001343 ETH — a significant balance.
This wallet has sent 1,842 transactions and is highly active.
```

---

## How It Works

```
User gives wallet address
        ↓
Web3.py calls Alchemy RPC
        ↓
Alchemy queries Ethereum node
        ↓
Returns: balance, tx count, block data
        ↓
Python classifies and formats the data
        ↓
AI-style plain English report printed
```

---

## How to Run

```bash
# 1. Install
pip install web3

# 2. Set your Alchemy URL as environment variable
export ALCHEMY_URL="https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY"

# 3. Run
python wallet_analyser.py
```

**In Google Colab:**
```python
import os
os.environ["ALCHEMY_URL"] = "https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY"
# then run the script
```

---

## Security
- All API keys loaded via `os.environ` — never hardcoded
- `.env` file blocked by `.gitignore`
- Only `.env.example` committed (safe placeholders only)
