# EVM — Ethereum Virtual Machine Explained Simply

**Day 03 Deep Dive**

---

## What is the EVM?

The EVM is the runtime environment for smart contracts on Ethereum.
Think of it as a global computer that:
- Is run by thousands of nodes simultaneously
- Executes the same code and gets the same result every time
- Is completely isolated from the internet (sandboxed)

```
Your Solidity Code
      ↓
  Compiler (solc)
      ↓
  EVM Bytecode
      ↓
  Every Ethereum Node Runs It
      ↓
  Consensus = Same Result Everywhere
```

---

## EVM Key Properties

| Property | Description |
|---|---|
| **Deterministic** | Same input → same output, always |
| **Sandboxed** | No internet access from inside contract |
| **Turing Complete** | Can run any computation |
| **Stack-based** | Uses a 256-bit stack machine |

---

## Gas — Why It Exists

- Without gas, a bad actor could run infinite loops and crash all nodes
- Gas makes computation have a real cost
- Each EVM operation (opcode) has a fixed gas cost
- If you run out of gas → transaction fails, gas is NOT refunded

### Common Gas Costs
```
ADD operation      →  3 gas
Storage write      →  20,000 gas
Storage read       →  800 gas
Contract deploy    →  32,000+ gas
```

---

## msg.sender — The Most Important Variable

```solidity
// msg.sender = the wallet address that called this function
function doSomething() public {
    address caller = msg.sender; // always available
}
```

- In every function call, Ethereum knows WHO called it
- `msg.sender` is cryptographically verified via signature
- This is how access control works in DeFi, NFTs, DAOs

---

## The Big Picture

```
User (MetaMask Wallet)
    ↓ signs transaction
Ethereum Network
    ↓ broadcasts to all nodes
EVM on every node
    ↓ executes bytecode
State Change (stored on blockchain)
    ↓
Immutable Forever
```
