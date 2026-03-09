# Day 05 — Web3.py: Reading $GOPI ERC-20 Token On-Chain
# Gopichand Challa | @GopichandAI
# Connected Python directly to my own ERC-20 token on Ethereum Sepolia

from web3 import Web3

# ── CONFIG ──────────────────────────────────────────────
# Get your free Alchemy URL: https://alchemy.com → Create App → Ethereum → Sepolia
ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/YOUR_API_KEY"

# Your deployed $GOPI contract address on Sepolia
CONTRACT_ADDRESS = "0x5B38Da6a701c568545dCfcB03FcB875f56beddC4"  # replace with yours

# Minimal ERC-20 ABI — only the read functions we need
ERC20_ABI = [
    {"inputs": [], "name": "name",        "outputs": [{"type": "string"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "symbol",      "outputs": [{"type": "string"}], "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "decimals",    "outputs": [{"type": "uint8"}],  "stateMutability": "view", "type": "function"},
    {"inputs": [], "name": "totalSupply", "outputs": [{"type": "uint256"}],"stateMutability": "view", "type": "function"},
    {"inputs": [{"name": "account", "type": "address"}],
     "name": "balanceOf", "outputs": [{"type": "uint256"}], "stateMutability": "view", "type": "function"},
]

# ── CONNECT ─────────────────────────────────────────────
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

if not w3.is_connected():
    print("❌ Connection failed. Check your Alchemy URL.")
    exit()

print("✅ Connected to Ethereum Sepolia via Alchemy")
print(f"   Latest block: {w3.eth.block_number}\n")

# ── READ CONTRACT ────────────────────────────────────────
contract = w3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=ERC20_ABI
)

name        = contract.functions.name().call()
symbol      = contract.functions.symbol().call()
decimals    = contract.functions.decimals().call()
total_raw   = contract.functions.totalSupply().call()
total_human = total_raw / (10 ** decimals)

# ── OUTPUT ───────────────────────────────────────────────
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"  Token Name   : {name}")
print(f"  Symbol       : ${symbol}")
print(f"  Decimals     : {decimals}")
print(f"  Total Supply : {total_human:,.0f} {symbol}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print()
print("✅ Day 05 complete — Python is talking to Ethereum.")
print("   The blockchain IS the database. No backend needed.")
