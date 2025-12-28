import asyncio
import random
import sys

async def write_me_a_poem(subject: str) -> str:
    # TODO:format the prompt and call the LLM asynchronously
    await asyncio.sleep(0.01)  # simulate async behavior with the sleep(seconds) method 
    color = random.choice(["blue", "green", "gray"])
    lines = list()
    lines.append("Roses are red")
    lines.append("Violets are blue")
    lines.append(f"I feel {color}")
    lines.append("When I'm not with you")
    lines.append("")
    lines.append(f"Oh, I forgot to include {subject} in this poem!")
    return "\n".join(lines) 

async def main():
    poem = await write_me_a_poem(sys.argv[1])
    print(poem) 

if __name__ == "__main__":
    # __main__ is the entry-point to the program when python is executed at the command-line 
    asyncio.run(main())
