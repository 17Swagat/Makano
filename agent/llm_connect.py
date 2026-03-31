import importlib.resources

import ollama


def stream_response(
    prompt: str, model: str = "qwen3.5:2b", format=None, stream=True, think=False
):
    stream = ollama.generate(
        model=model,
        prompt=prompt,
        format=format,
        stream=stream,
        think=think,
    )

    assistant_response = ""
    print("[Makano]: ", end="")
    for chunk in stream:
        assistant_response += chunk["response"]  # pyright: ignore[reportArgumentType, reportCallIssue]
        print(chunk["response"], end="", flush=True)  # pyright: ignore[reportCallIssue, reportArgumentType]
    print("")
    return assistant_response


AVAILABLE_COMMANDS = {
    "/exit": "Exits the program.",
    "/help": "List out all the availabe commands.",
}

# [System Prompt File]:
PACKAGE_NAME = "agent"
system_prompt = importlib.resources.read_text(PACKAGE_NAME, "prompt.md")
# with open("prompt.md", "r") as system_prompt_file:
#     system_prompt = system_prompt_file.read()


def interface():
    print("<Makano Agent>")
    print("How can I help you?")
    print("Use /help to view available commands.")
    while True:
        prompt_user = input("[User]> ")
        if prompt_user.strip() == "":
            continue
        elif prompt_user.strip() == "/exit":
            print("Bye :)")
            break
        elif prompt_user.strip() == "/help":
            print("List of available commands:")
            for command, descript in AVAILABLE_COMMANDS.items():
                print(f"`{command}` : {descript}")
        else:
            input_prompt = f"""{system_prompt} \n
            Agentic Conversation:
            [User]: {prompt_user}
            """
            assistant_response = stream_response(input_prompt)
            input_prompt += f"\n[Assistant]: {assistant_response}"
