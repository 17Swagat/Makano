# **Makano**

> ***This is my attempt to build an agent from scratch.  
> I’m trying to avoid using third‑party packages as much as possible—both for learning purposes and to explore what the idea of an agent in my mind really looks like.  
> I’ve tried a few existing agents, but something about them doesn’t sit right with me.  
> What I want is something that gives reasonable answers and can handle some basic tasks.  
> The goal here isn’t to create a super‑powerful agent that racks up a huge token bill. (I’m broke!)  
> Instead, I want to see how much good work a small, local AI model can actually do.***

## **Sandbox Playaround**
* **Folder `sandbox_playground` in the playground region where my agent can operate right now. Its basically, the folder in which the Agent can create/delete files/folders. Read and write files.**
* **Right now I want the agent to be only do 1 thing. In the specified folder, just be able to perform CRUD operations on files & folders.**

___________________________

## **NOTES:**
- **On my system, I find ollama to behave slower when using `ollama.Chat`, that's why I'm using `ollama.generate()` function in some concatenation tricks to behave it like an agent.**
- **`Hope for some changes`: Recently downloaded `qwen3.5:4b model` on my system and tried using ollama.chat, did not got any sort of visible delay. Maybe I was using qwen3.5:latest model with was larger in size, maybe due to that the loading time was slow. Not sure tbh, let's experiment with `ollama.chat` as it provides some additional benefits.**

<details>
  <summary>Things Bugging me [Currently]</summary>
-   When suggesting reference links for doing further research, the model should be able to do `internet-tool search`.
</details>
