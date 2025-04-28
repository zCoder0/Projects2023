from langchain.llms import CTransformers

# Load the model with the correct path and config
llm = CTransformers(
    model="Models/llama-2-7b-chat.ggmlv3.q8_0.bin",
    model_type="llama",  # Try using gpt if llama doesn't work
    config={
        'max_new_tokens': 256,
        'temperature': 0.01
    }
)


response = llm("Hello, how are you?")
print(response)


