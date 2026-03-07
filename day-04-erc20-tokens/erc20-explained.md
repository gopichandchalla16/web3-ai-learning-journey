# ERC-20 Explained Simply 🪙

> A beginner-friendly breakdown by Gopichand Challa  
> Day 04 of AI × Web3 Learning Journey

---

## The Simplest Mental Model

Imagine a Google Sheet with 2 columns:

| Address | Balance |
|---|---|
| 0xYourWallet | 1,000,000 |
| 0xFriend | 0 |
| 0xUniswap | 0 |

When you **transfer 100 GOPI** to a friend:
- Your balance: 1,000,000 → 999,900
- Friend's balance: 0 → 100

That's it. An ERC-20 token is just this spreadsheet, stored on-chain.

---

## The Approve → TransferFrom Pattern

This is how DeFi protocols (Uniswap, Aave, etc.) work:

```
Step 1: You → approve(Uniswap, 100)
        "Hey blockchain, Uniswap can spend 100 of my tokens"

Step 2: Uniswap → transferFrom(You, Uniswap, 100)
        "Taking the 100 tokens you approved"

Result: You gave Uniswap permission. Uniswap took them.
        You never sent to Uniswap directly.
```

Why this pattern?
- Your tokens stay in YOUR wallet until used
- You can set spending limits
- You can revoke approval anytime

---

## Real World Token Examples

| Token | What it is | Standard |
|---|---|---|
| USDC | USD stablecoin | ERC-20 |
| UNI | Uniswap governance | ERC-20 |
| LINK | Chainlink oracle | ERC-20 |
| SHIB | Meme token | ERC-20 |
| $GOPI | My learning token | ERC-20 |

All of them use the EXACT same 6 functions. The standard is the power.

---

## Why Decimals = 18?

Solidity has no floats. So instead of `0.5 GOPI`, we store `500000000000000000` (18 zeros).

```solidity
1 GOPI = 1 * 10^18 = 1000000000000000000
0.5 GOPI = 5 * 10^17 = 500000000000000000
```

Your wallet (MetaMask) divides by 10^18 automatically to show you `0.5 GOPI`.

---

## Gas Costs

| Operation | Approx Gas |
|---|---|
| transfer | ~21,000 |
| approve | ~45,000 |
| transferFrom | ~50,000 |
| mint | ~50,000 |
| burn | ~35,000 |

---

*Built during AI × Web3 Learning Journey — March 2026*  
*[@GopichandAI](https://x.com/GopichandAI) | [GitHub](https://github.com/gopichandchalla16)*
