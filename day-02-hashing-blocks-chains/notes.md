# Day 2 — Hashing, Blocks & Chains
**Date:** March 05, 2026

## What I Learned

### 1. SHA-256 Hashing
- Any data in → fixed 64-character string out
- Change 1 letter → completely different hash
- One-way: you cannot reverse a hash to get the data
- Used in: Bitcoin, Ethereum, file verification

```python
import hashlib
print(hashlib.sha256(b"Gopichand").hexdigest())
# completely different from:
print(hashlib.sha256(b"gopichand").hexdigest())
```

### 2. How Blocks Chain Together
```
Block 1: data + prev_hash(0000) → hash_A
Block 2: data + prev_hash(hash_A) → hash_B
Block 3: data + prev_hash(hash_B) → hash_C

Change Block 1 data → hash_A changes
→ Block 2's prev_hash is now WRONG
→ Block 3's prev_hash is now WRONG
→ Entire chain is invalid
```

### 3. What is a Nonce?
- A random number miners keep changing
- Until the block hash starts with 0000...
- Finding that number = mining a block
- This costs computational energy = Proof of Work

### 4. Proof of Work vs Proof of Stake
| | Proof of Work | Proof of Stake |
|---|---|---|
| Used by | Bitcoin | Ethereum (post-Merge) |
| Mechanism | Compete with computing power | Lock up ETH as collateral |
| Energy | High | Low |
| Penalty | Wasted electricity | Lose staked ETH |

### 5. The Merge (2022)
- Ethereum switched from PoW to PoS
- Reduced energy consumption by ~99.95%
- Validators replaced miners

## Key Takeaway
> Immutability isn't magic. It's math. Change one block, and the entire chain screams "tampered."

## Visual Demo Used
https://andersbrownworth.com/blockchain
