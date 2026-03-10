# Day 06 — AI Agent on-chain
**Date:** March 09, 2026  
**Gopichand Challa | @GopichandAI**

---

## What I Built Today

An AI agent that reads any Ethereum wallet balance live from the blockchain and explains it in plain English.

**Input:** any ETH wallet address  
**Output:** balance + plain English explanation from AI

---

## What is a LangChain Agent?

A regular LLM just chats. It can't DO anything outside its training data.

A LangChain agent has TOOLS — Python functions it can call to interact with the real world.

```
User asks → Agent thinks → Agent calls tool → Tool returns data → Agent explains
```

Today's tool = Web3.py function that reads Ethereum.

---

## The Key Insight

The bridge between AI and blockchain is just a Python function:

```python
def get_wallet_balance(address):
    balance = w3.eth.get_balance(address)
    return w3.from_wei(balance, 'ether')
```

Wrap that in a LangChain @tool → you have an AI agent that understands blockchain.

---

## What's Next

- Connect real LLM (Groq free tier)
- Read ERC-20 token balances too
- Build full AI × Web3 project on Day 07

---

## Key Takeaway

> AI that can only chat is a toy.  
> AI that can read the blockchain is a tool.  
> The difference is one Python function.
