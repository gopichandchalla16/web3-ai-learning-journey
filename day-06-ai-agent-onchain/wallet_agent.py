# Day 06 — AI Agent on-chain
# LangChain + Web3.py: AI that reads Ethereum wallets
# Gopichand Challa | @GopichandAI | Mar 09, 2026
# ⚠️  Never hardcode API keys. Use environment variables.

from web3 import Web3
import os

# ── CONFIG (safe — loads from environment) ─────────────────────
ALCHEMY_URL = os.environ.get("ALCHEMY_URL", "https://eth-sepolia.g.alchemy.com/v2/YOUR_KEY_HERE")

w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
print("Connected:", w3.is_connected())
print(f"Latest Block: {w3.eth.block_number}")

# ── WEB3 TOOL ──────────────────────────────────────────────
def get_wallet_balance(address: str) -> str:
    """Reads ETH balance of any wallet from Ethereum."""
    try:
        checksum = Web3.to_checksum_address(address)
        balance_wei = w3.eth.get_balance(checksum)
        balance_eth = w3.from_wei(balance_wei, 'ether')
        block = w3.eth.block_number
        return (
            f"Address : {checksum}\n"
            f"Balance : {balance_eth:.6f} ETH\n"
            f"Block   : {block}"
        )
    except Exception as e:
        return f"Error: {str(e)}"

# ── AI EXPLAIN ──────────────────────────────────────────
def ai_explain(address: str):
    result = get_wallet_balance(address)
    lines = result.split("\n")
    balance = lines[1].replace("Balance : ", "").strip()
    short = address[:6] + "..." + address[-4:]
    print(f"\n🤖 AI Agent: Wallet {short} holds {balance}")
    print("   Read live from Ethereum — no database, pure blockchain.")

print("\n── Reading wallets live from Ethereum ──")
ai_explain("0x5B38Da6a701c568545dCfcB03FcB875f56beddC4")
ai_explain("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")

print("\n✅ Day 06 complete — AI is reading blockchain data.")
