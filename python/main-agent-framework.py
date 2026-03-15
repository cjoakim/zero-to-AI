"""
Usage:
  python main-agent-framework.py <func>
  python main-agent-framework.py check_env
  python main-agent-framework.py explore1
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


from openai import OpenAI

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
        if name.startswith("AZURE_"):
            print("{}: {}".format(name, os.environ[name]))


async def explore1():
    await asyncio.sleep(0.01)
    #simple_openai_response()
    simple_openai_response_chaining()



def simple_openai_response():
    # See https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key

    foundry_name = os.environ["AZURE_FOUNDRY_NAME"]
    endpoint = f"https://{foundry_name}.openai.azure.com/openai/v1/"
    api_key = os.environ["AZURE_OPENAI_COMPLETIONS_KEY"]
    deployment_name = os.environ["AZURE_OPENAI_COMPLETIONS_DEP"]

    client = OpenAI(
        api_key = api_key,
        base_url = endpoint,
    )
    response1 = client.responses.create(   
        model=deployment_name,
        input="Explain the 'Rooster' song by Alice in Chains in 100 words",
    )

    print("=== response1 ===")
    print(str(type(response1)))  # <class 'openai.types.responses.response.Response'>
    print(response1.model_dump_json(indent=2)) 

    print("=== response2 ===")
    id = response1.id
    response2 = client.responses.retrieve(id)
    print(str(type(response2)))  # <class 'openai.types.responses.response.Response'>
    print(response2.model_dump_json(indent=2)) 
    print(response2.output[0].content[0].text) 


def simple_openai_response_chaining():
    # See https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key

    foundry_name = os.environ["AZURE_FOUNDRY_NAME"]
    endpoint = f"https://{foundry_name}.openai.azure.com/openai/v1/"
    api_key = os.environ["AZURE_OPENAI_COMPLETIONS_KEY"]
    deployment_name = os.environ["AZURE_OPENAI_COMPLETIONS_DEP"]

    inputs = [
        {"type": "message",
        "role": "user",
        "content": "Explain the 'Rooster' song by Alice in Chains in 600 words"}
    ] 

    client = OpenAI(
        api_key = api_key,
        base_url = endpoint,
    )
    response1 = client.responses.create(   
        model=deployment_name,
        input=inputs 
    )

    print("=== response1 ===")
    print(str(type(response1)))  # <class 'openai.types.responses.response.Response'>
    print(response1.model_dump_json(indent=2)) 

    inputs += response1.output
    print(str(type(inputs))) 

    inputs.append(
        {"role": "user",
        "type": "message",
        "content": "Explain the above very simply at the 8th grade level"}) 

    # By default, response data is retained for 30 days.
    cleanup = client.responses.delete(response1.id)
    print(cleanup)

    # Object of type ResponseOutputMessage is not JSON serializable
    print("inputs length: {}".format(len(inputs)))
    for idx, input in enumerate(inputs):
        print(input)
            
    print("=== response2 ===")
    response2 = client.responses.create(
        model=deployment_name,
        previous_response_id=response1.id,
        input=inputs
    )
    print(str(type(response2)))  # <class 'openai.types.responses.response.Response'>
    print(response2.model_dump_json(indent=2)) 
    print(response2.output[0].content[0].text) 

    # By default, response data is retained for 30 days.
    cleanup = client.responses.delete(response2.id)
    print(cleanup)


# def responses_client():
#     # https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/responses?tabs=python-key

#     endpoint = os.environ["AZURE_OPENAI_RESP_COMPLETIONS_URL"]
#     api_key = os.environ["AZURE_OPENAI_RESP_COMPLETIONS_KEY"]
#     deployment_name = os.environ["AZURE_OPENAI_RESP_COMPLETIONS_DEP"]

#     return AzureOpenAIResponsesClient(
#         endpoint = endpoint,
#         api_key = api_key,
#         deployment_name = deployment_name)


async def main():
    try:
        load_dotenv(override=True)
        func = sys.argv[1].lower()
        if func == "check_env":
            await check_env()
        elif func == "explore1":
            await explore1()
        else:
            print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())


if __name__ == "__main__":
    # __main__ is the entry-point to the program when python is executed at the command-line
    # Use the asyncio.run() method to run the main() function asynchronously
    asyncio.run(main())
