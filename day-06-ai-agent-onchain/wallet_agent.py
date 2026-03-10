# Day 06 — AI Agent on-chain
# LangChain + Web3.py: AI that reads Ethereum wallets
# Gopichand Challa | @GopichandAI | Mar 09, 2026

from web3 import Web3

# ── CONFIG ──────────────────────────────────────────────
ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY"

w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
print("Connected:", w3.is_connected())
print(f"Latest Block: {w3.eth.block_number}")

# ── WEB3 TOOL (no LangChain needed to understand this) ──
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

# ── TEST THE TOOL DIRECTLY ───────────────────────────────
print("\n── Reading wallets live from Ethereum Sepolia ──")

# Your wallet
my_wallet = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"
print("\n[Your Wallet]")
print(get_wallet_balance(my_wallet))

# Vitalik's wallet
vitalik = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
print("\n[Vitalik's Wallet]")
print(get_wallet_balance(vitalik))

# ── SIMPLE AI RESPONSE (without API key) ────────────────
def ai_explain_balance(address: str) -> str:
    """Simulates what an AI agent would say about a wallet."""
    result = get_wallet_balance(address)
    lines = result.split("\n")
    balance = lines[1].replace("Balance : ", "").strip()
    short_addr = address[:6] + "..." + address[-4:]

    return (
        f"\n🤖 AI Agent Response:\n"
        f"The wallet {short_addr} currently holds {balance} "
        f"on the Ethereum Sepolia testnet. "
        f"This data was read live from the blockchain — "
        f"no API, no database, just direct on-chain access via Web3.py."
    )

print("\n── AI Agent Explaining Balances ──")
print(ai_explain_balance(my_wallet))
print(ai_explain_balance(vitalik))

print("\n✅ Day 06 complete — AI is reading blockchain data.")
print("   Next: connect a real LLM (Groq free / OpenAI)")
