# Connect To Ollama
# %%
# !curl http://localhost:11434/api/generate -d '{  \"model\": \"qwen3.5:2b\",  \"prompt\": \"What color is the sky at different times of the day? Respond using JSON\",  \"format\": \"json\",}'

# %%
# Using
# ollama.chat:=>
import ollama

stream = ollama.chat(
    model="qwen3.5:4b",
    messages=[{"role": "user", "content": "What is the chemical formula of sodium dioxide"}],
    stream=True,
    think=False
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)

# %%
# Using
# ollama.generate :=>

stream = ollama.generate(
    model="qwen3.5:4b",
    prompt="why sky is blue?",
    # format=format,
    stream=True,
    think=False,
)

for chunk in stream:
    print(chunk["response"], end="", flush=True)  

# %%
import ollama

stream = ollama.generate(
    model="qwen3.5:2b",
    # Prompts:
    # prompt="What color is the sky at different times of the day? Respond using JSON",
    # prompt="What is love? Explain within 2 lines (AT MOST).",
    # prompt="Write me a c program function that takes `n`:integer as input and outputs a fibonacci sequence. PROVIDE NO EXPLAINATIONS AND OUTPUTS. JUST WRITE THE FUNCTION. No need to provide main() function and need to write the entire program. Just provide only with the function.",
    prompt="""You are a helpfull AI Assistant eargly ready to help you user.
    Question: How to use llama.cpp and integrate it into my application. I've downloaded models through ollama, which I want to use for inference on my machine through llama.cpp.""",
    # format="json",
    stream=True,
    think=False,
)

for chunk in stream:
    print(chunk["response"], end="", flush=True)

# %%
# @MY NOTE: BOTH options turned out to be slow
# Slow
print(
    ollama.chat(
        model="qwen3.5:2b", messages=[{"role": "user", "content": "Say hello"}]
    )["message"]["content"]
)
# %%
# Fast
print(ollama.generate(model="qwen3.5:2b", prompt="Say hello")["response"])
# %%
name = input("What is your name?")
print(name.strip())

# %%

with open("../agent/prompt.md", "r") as system_prompt_file:
    system_prompt = system_prompt_file.read()

system_prompt += "\n[User]: How are you doing?"
system_prompt += "\n[Assistant]: I'm doing fine. What about you?"
system_prompt += "\n[User]: What is the value of PI?"
system_prompt += "\n[Assistant]: The value of PI is 3.14"

print(system_prompt)
