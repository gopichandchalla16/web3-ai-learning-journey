# Day 05 — Web3.py: Reading On-Chain Data
# Gopichand Challa | @GopichandAI
# ⚠️  Never hardcode API keys. Use environment variables.

from web3 import Web3
import os

# ── LOAD FROM ENVIRONMENT (safe) ─────────────────────────
# Create a .env file locally with: ALCHEMY_URL=https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY
# Never commit your .env file to GitHub!
ALCHEMY_URL = os.environ.get("ALCHEMY_URL", "https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY_HERE")

w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
print("Connected:", w3.is_connected())
print(f"Latest Block: {w3.eth.block_number}")

# ── READ WALLET BALANCE ──────────────────────────────────
my_wallet = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
vitalik   = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"

for label, addr in [("My Wallet", my_wallet), ("Vitalik", vitalik)]:
    bal_wei = w3.eth.get_balance(Web3.to_checksum_address(addr))
    bal_eth = w3.from_wei(bal_wei, 'ether')
    print(f"  {label}: {bal_eth:.6f} ETH")

print("\n✅ Web3.py reading live Ethereum data!")
