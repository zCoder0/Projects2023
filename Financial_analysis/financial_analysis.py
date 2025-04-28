from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

from phi.tools.duckduckgo import DuckDuckGo
from gpt4all import GPT4All

# Load local LLM
model_path = "models/mistral-7b.Q4_0.gguf"  # Update with your model file
llm = GPT4All(model_path)

query = "What's happening in France?"

# Run the local model
response = llm.generate(query)
print(response)
