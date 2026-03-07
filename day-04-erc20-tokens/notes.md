# Day 04 — ERC-20 Tokens 🪙

> **Date:** March 07, 2026  
> **Builder:** Gopichand Challa  
> **X:** [@GopichandAI](https://x.com/GopichandAI)

---

## 🧠 What I Learned Today

### What is ERC-20?
- ERC = Ethereum Request for Comment
- ERC-20 is a **standard interface** for fungible tokens on Ethereum
- Every token (USDC, UNI, SHIB) follows these exact same rules
- "Fungible" = each token is identical, like a rupee coin

### The Core Mental Model
```
token balances = mapping(address => uint256)
```
That's it. A token is just a **spreadsheet** tracking:
- Who owns how many
- Who is allowed to spend whose tokens

### ERC-20 Standard Functions
| Function | What it does |
|---|---|
| `totalSupply()` | How many tokens exist |
| `balanceOf(addr)` | How many tokens an address holds |
| `transfer(to, amt)` | Send tokens directly |
| `approve(spender, amt)` | Allow someone else to spend your tokens |
| `transferFrom(from, to, amt)` | Spend approved tokens |
| `allowance(owner, spender)` | Check approved spending limit |

### Events (Important!)
- `Transfer` — logged every time tokens move
- `Approval` — logged every time spending is approved
- Events are **permanent**, **searchable** on-chain
- Tools like Etherscan read these to show token history

---

## 🔨 What I Built

**GopichandToken ($GOPI)**
- Name: GopichandToken
- Symbol: GOPI
- Decimals: 18 (like ETH — 1 token = 10^18 units)
- Total Supply: 1,000,000 GOPI
- Features: transfer, approve, transferFrom, mint, burn

---

## 💡 Key Insights

1. **Decimals explained** — 1 GOPI token is stored as `1000000000000000000` (18 zeros). This allows fractional ownership without floats.

2. **Approve + TransferFrom pattern** — This is how DeFi works. You approve Uniswap to spend your tokens, then Uniswap calls transferFrom. Your tokens never leave your control until the swap.

3. **Mint vs Transfer** — Mint creates tokens from nothing (address(0) → you). Transfer moves existing tokens. Only owner can mint.

4. **Burn = send to address(0)** — Burning permanently removes tokens from supply. Used by many DeFi protocols to increase scarcity.

5. **Events are logs** — Not stored in contract state. Cheaper than storage. Block explorers index them to show transaction history.

---

## 🔗 Resources
- [EIP-20 Official Standard](https://eips.ethereum.org/EIPS/eip-20)
- [Remix IDE](https://remix.ethereum.org)
- [Sepolia Testnet Faucet](https://sepoliafaucet.com)

---

## ✅ Day 04 Checklist
- [x] Understand ERC-20 standard
- [x] Write GopichandToken from scratch
- [x] Compile + deploy on Remix VM
- [x] Test: transfer, approve, mint, burn
- [x] Push to GitHub
- [ ] Deploy on Sepolia testnet (Day 05 stretch goal)
