"""
Usage:
  python main-aoai.py <func>
  python main-aoai.py check_env
  python main-aoai.py tokens mary had a little lamb
  python main-aoai.py generate_embedding
  python main-aoai.py generate_embedding python fastapi pydantic web app with azure cosmosdb and azure storage
  python main-aoai.py generate_completion
  python main-aoai.py generate_completion_with_md_prompt > tmp/gettysburg.txt
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

# Chris Joakim, 3Cloud/Cognizant, 2026

import asyncio
import json
import sys
import os
import traceback

from pprint import pprint

from docopt import docopt
from dotenv import load_dotenv

import openai
import tiktoken

from openai import AzureOpenAI
from openai.types import CreateEmbeddingResponse
from openai.types.chat.chat_completion import ChatCompletion

from src.ai.aoai_util import AOAIUtil
from src.io.fs import FS


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


async def check_env():
    await asyncio.sleep(0.01)
    load_dotenv(override=True)
    for name in sorted(os.environ.keys()):
        if name.startswith("AZURE_OPENAI_"):
            print("{}: {}".format(name, os.environ[name]))


async def tokens():
    # print("sys.argv:   {}".format(sys.argv))
    sentence = " ".join(sys.argv[2:])
    print("sentence:   {}".format(sentence))
    encoding = tiktoken.encoding_for_model("gpt-4o-mini")
    tokens = encoding.encode(sentence)
    print("tokens:     {}".format(tokens))
    print("num_tokens: {}".format(len(tokens)))


async def generate_completion():
    aoai_util = AOAIUtil()  # See module python/src/ai/aoai_util.py in this repository
    system_context = "You are a helpful assistant who knows Major League Baseball."
    user_prompt = "What uniform number did Mickey Mantle wear?"
    completion = await aoai_util.generate_completion(system_context, user_prompt)
    print(completion)


async def generate_embedding():
    text = "Consulting companies like 3Cloud and Cognizant"
    if len(sys.argv) > 2:
        text = " ".join(sys.argv[1:])
    print(f"generating embedding for: {text}")
    ai_util = AOAIUtil()
    embedding = await ai_util.generate_embeddings(text)
    print(embedding)
    print(f"generated embedding for: {text}")

def generate_completion_with_md_prompt():
    url = os.getenv("AZURE_OPENAI_COMPLETIONS_URL")
    key = os.getenv("AZURE_OPENAI_COMPLETIONS_KEY")
    dep = os.getenv("AZURE_OPENAI_COMPLETIONS_DEP")
    vers = os.getenv("AZURE_OPENAI_COMPLETIONS_VERSION")

    client = AzureOpenAI(azure_endpoint=url, api_key=key, api_version=vers)
    messages=[
        {"role": "system", "content": text_summarization_md()},
        {"role": "user", "content": gettysburg_address_user_md()},
    ]
    print(f"prompt messages: \n{json.dumps(messages, indent=2)}")

    # <class 'openai.types.chat.chat_completion.ChatCompletion'>
    completion: ChatCompletion = client.chat.completions.create(
        model=dep,
        temperature=0.0,
        max_tokens=1000,
        messages=messages,
    )

    print("=== completion type ===")
    print(str(type(completion)))

    print("=== message ===")
    print(completion.choices[0].message)

    print("=== content ===")
    print(completion.choices[0].message.content)

    print("=== model_dump_json ===")
    print(completion.model_dump_json(indent=2))


def text_summarization_md():
    return """
## Purpose

You are a helpful assistant who summarizes text.

Summarize the following text into bullet points.

"""


def gettysburg_address_user_md():
    text = FS.read("data/text/gettysburg-address.txt").strip()
    return """
## Text to summarize

{}

""".format(text).lstrip()


async def main():
    try:
        load_dotenv(override=True)
        func = sys.argv[1].lower()
        if func == "check_env":
            await check_env()
        elif func == "tokens":
            await tokens()
        elif func == "generate_embedding":
            await generate_embedding()
        elif func == "generate_completion":
            await generate_completion()
        elif func == "generate_completion_with_md_prompt":
            generate_completion_with_md_prompt()
        else:
            print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())


if __name__ == "__main__":
    # __main__ is the entry-point to the program when python is executed at the command-line
    # Use the asyncio.run() method to run the main() function asynchronously
    asyncio.run(main())
