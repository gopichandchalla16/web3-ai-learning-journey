# LangChain + Web3.py — The AI × Web3 Bridge
**Gopichand Challa | @GopichandAI | Day 06**

---

## Why Combine LangChain and Web3.py?

| LangChain alone | Web3.py alone | LangChain + Web3.py |
|---|---|---|
| Talks, explains, reasons | Reads blockchain | AI that reads + explains blockchain |
| No real-world access | No natural language | Best of both worlds |
| Chatbot | Script | AI Agent |

---

## The Simple Version (No API Key Needed)

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider("YOUR_ALCHEMY_URL"))

def get_balance(address):
    bal = w3.eth.get_balance(Web3.to_checksum_address(address))
    return w3.from_wei(bal, 'ether')

# Call it
print(get_balance("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"))
```

---

## With Real LangChain Agent (Free via Groq)

```python
# pip install langchain langchain-groq web3

from web3 import Web3
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

w3 = Web3(Web3.HTTPProvider("YOUR_ALCHEMY_URL"))

@tool
def get_wallet_balance(address: str) -> str:
    """Gets the ETH balance of any Ethereum wallet address."""
    checksum = Web3.to_checksum_address(address)
    balance_wei = w3.eth.get_balance(checksum)
    return f"{w3.from_wei(balance_wei, 'ether'):.6f} ETH"

llm = ChatGroq(model="llama3-8b-8192", api_key="YOUR_GROQ_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Web3 assistant. Use your tools to fetch on-chain data."),
    ("human", "{input}"),
    MessagesPlaceholder("agent_scratchpad"),
])

agent = create_openai_functions_agent(llm, [get_wallet_balance], prompt)
runner = AgentExecutor(agent=agent, tools=[get_wallet_balance], verbose=True)

result = runner.invoke({"input": "What is the balance of 0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045?"})
print(result["output"])
```

---

## Get Free Groq API Key
1. Go to **console.groq.com**
2. Sign up free
3. Create API key
4. Use Llama 3 — completely free, fast
