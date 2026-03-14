"""
Day 08 — AI Escrow Arbiter
Author : Gopichand Challa
Date   : March 14, 2026

What it does:
  Reads a dispute reason string (same as what gets stored
  on-chain in Escrow.sol) and uses a Groq LLM via LangChain
  to decide: RELEASE or REFUND.

How to run:
  python ai_arbiter.py
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()


# ──────────────────────────────────────────────
# 1. AI Decision Engine
# ──────────────────────────────────────────────
def ai_decide(dispute_reason: str) -> str:
    """
    Takes a dispute reason string.
    Returns AI verdict: RELEASE or REFUND + 1-line explanation.
    """
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "ERROR: GROQ_API_KEY not found in .env file"

    llm = ChatGroq(
        model="llama3-8b-8192",
        api_key=api_key,
        temperature=0          # deterministic arbiter
    )

    system_prompt = """You are a neutral, impartial blockchain escrow arbiter.

Your job: read a dispute description and decide who gets the locked ETH.

Rules:
- RELEASE = pay the BENEFICIARY (service/work was delivered)
- REFUND  = return ETH to DEPOSITOR (service/work was NOT delivered)

Respond in EXACTLY this format:
VERDICT: RELEASE
REASON: [one sentence explanation]

or

VERDICT: REFUND
REASON: [one sentence explanation]

Do NOT write anything else."""

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Dispute Description:\n{dispute_reason}")
    ]

    response = llm.invoke(messages)
    return response.content.strip()


# ──────────────────────────────────────────────
# 2. Test Cases (same scenarios a real escrow sees)
# ──────────────────────────────────────────────
TEST_DISPUTES = [
    {
        "id": 1,
        "title": "Freelancer delivered on time, client refuses to pay",
        "dispute": (
            "A freelance developer was hired to build a Solidity escrow "
            "contract. They delivered the full codebase with tests on the "
            "agreed deadline. The client reviewed and confirmed it works, "
            "but is now refusing to release payment claiming the UI is ugly."
        )
    },
    {
        "id": 2,
        "title": "Developer went silent, no delivery after 3 weeks",
        "dispute": (
            "Developer was paid into escrow to build a REST API in 2 weeks. "
            "After 3 weeks there is no code, no communication, and no updates. "
            "The depositor has sent 5 messages with zero replies."
        )
    },
    {
        "id": 3,
        "title": "Work delivered but has a critical security bug",
        "dispute": (
            "Smart contract was delivered and deployed on Sepolia testnet. "
            "However, a security audit found a reentrancy vulnerability in the "
            "withdraw() function that allows an attacker to drain all funds. "
            "The developer claims the original scope did not include a security audit."
        )
    },
    {
        "id": 4,
        "title": "Client kept changing requirements after agreement",
        "dispute": (
            "The developer completed 100% of the originally agreed scope. "
            "The client then demanded 3 additional features not in the original "
            "agreement, and is now withholding payment because those extras "
            "were not built. No new contract was signed for the additional work."
        )
    },
    {
        "id": 5,
        "title": "Partial delivery — 60% work done, client wants full refund",
        "dispute": (
            "Developer completed 3 out of 5 agreed modules and stopped responding. "
            "The 3 delivered modules work correctly. The client wants a full refund "
            "but the developer argues partial payment is fair for partial delivery."
        )
    }
]


# ──────────────────────────────────────────────
# 3. Runner
# ──────────────────────────────────────────────
def run_all_cases():
    print("=" * 60)
    print("   DAY 08 — AI ESCROW ARBITER")
    print("   Author: Gopichand Challa | March 14, 2026")
    print("=" * 60)

    for case in TEST_DISPUTES:
        print(f"\nCase {case['id']}: {case['title']}")
        print("-" * 60)
        print(f"Dispute: {case['dispute'][:100]}...")
        print()
        verdict = ai_decide(case["dispute"])
        print(f"AI Decision:\n{verdict}")
        print("=" * 60)


if __name__ == "__main__":
    run_all_cases()
