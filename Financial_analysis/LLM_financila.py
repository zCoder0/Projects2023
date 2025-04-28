from langchain.llms import GPT4All
from langchain.agents import AgentType, initialize_agent
from langchain.tools import DuckDuckGoSearchRun
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# Load Local LLM
model_path = "models/mistral-7b.Q4_0.gguf"  # Update with your model file
llm = GPT4All(model=model_path, verbose=True)

# Add Web Search Tool
search_tool = DuckDuckGoSearchRun()

# Set up an Agent with memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

agent = initialize_agent(
    tools=[search_tool],  # Add more tools if needed
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

# Run the agent with a query
response = agent.run("What's happening in France?")
print(response)
