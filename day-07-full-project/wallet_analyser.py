# Day 07 — Full AI x Web3 Mini Project
# Complete Wallet Analyser: Web3.py + AI plain-English report
# Gopichand Challa | @GopichandAI | Mar 10, 2026
#
# ⚠️  SECURITY: Never hardcode API keys.
#     Set environment variable before running:
#     In Colab: os.environ["ALCHEMY_URL"] = "your_key"
#     Locally:  create a .env file (see .env.example)

import os
from web3 import Web3
from datetime import datetime

# ── CONFIG ──────────────────────────────────────────────
# Load from environment — never hardcode!
ALCHEMY_URL = os.environ.get("ALCHEMY_URL", "https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY_HERE")

w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

# ── CONNECTION CHECK ──────────────────────────────────────
if not w3.is_connected():
    print("❌ Not connected. Check your ALCHEMY_URL environment variable.")
    exit()

latest_block = w3.eth.block_number
print(f"✅ Connected to Ethereum Sepolia | Block: {latest_block}")

# ── CORE FUNCTIONS ────────────────────────────────────────
def get_eth_balance(address: str) -> dict:
    """Returns ETH balance in both Wei and Ether."""
    checksum = Web3.to_checksum_address(address)
    balance_wei = w3.eth.get_balance(checksum)
    balance_eth = float(w3.from_wei(balance_wei, 'ether'))
    return {"address": checksum, "wei": balance_wei, "eth": balance_eth}

def get_tx_count(address: str) -> int:
    """Returns total number of transactions sent from this wallet."""
    checksum = Web3.to_checksum_address(address)
    return w3.eth.get_transaction_count(checksum)

def get_block_info() -> dict:
    """Returns latest block metadata."""
    block = w3.eth.get_block('latest')
    ts = datetime.utcfromtimestamp(block['timestamp']).strftime('%Y-%m-%d %H:%M UTC')
    return {
        "number": block['number'],
        "transactions": len(block['transactions']),
        "timestamp": ts,
        "gas_used": block['gasUsed'],
    }

def ai_wallet_report(address: str) -> str:
    """Generates a plain-English AI-style wallet report."""
    bal   = get_eth_balance(address)
    txs   = get_tx_count(address)
    block = get_block_info()
    short = address[:6] + "..." + address[-4:]

    # Classify wallet activity
    if txs == 0:
        activity = "brand new or never used"
    elif txs < 10:
        activity = "lightly active"
    elif txs < 100:
        activity = "moderately active"
    else:
        activity = "highly active"

    # Classify balance
    if bal['eth'] == 0:
        bal_note = "This wallet has no ETH. It may be empty or on a different network."
    elif bal['eth'] < 0.01:
        bal_note = f"This wallet holds a very small amount: {bal['eth']:.6f} ETH."
    elif bal['eth'] < 1:
        bal_note = f"This wallet holds {bal['eth']:.4f} ETH — a modest amount."
    else:
        bal_note = f"This wallet holds {bal['eth']:.4f} ETH — a significant balance."

    report = f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI WALLET REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Wallet   : {short}
Network  : Ethereum Sepolia Testnet
Block    : {block['number']} | {block['timestamp']}
──────────────────────────────────────────────────
💰 Balance  : {bal['eth']:.6f} ETH ({bal['wei']} Wei)
📤 Tx Count : {txs} transactions sent
📊 Activity : {activity}
──────────────────────────────────────────────────
🤖 AI Summary:
{bal_note}
This wallet has sent {txs} transaction(s) and is {activity}.
Latest Ethereum block has {block['transactions']} transactions.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    return report

# ── RUN ANALYSIS ───────────────────────────────────────────
wallets = {
    "My Wallet" : "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4",
    "Vitalik"   : "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045",
}

for label, addr in wallets.items():
    print(f"\n🔍 Analysing: {label}")
    print(ai_wallet_report(addr))

print("✅ Day 07 complete — Full AI x Web3 project done!")
print("   7 days. 7 builds. From zero to AI x Web3 builder.")
