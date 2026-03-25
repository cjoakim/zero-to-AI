import asyncio
import logging
import os
import traceback

from pprint import pprint

from docopt import docopt
from dotenv import load_dotenv

import openai
from openai import OpenAI
from openai import AzureOpenAI
from openai.types import CreateEmbeddingResponse
from openai.types.chat.chat_completion import ChatCompletion

from src.io.fs import FS

# This Python module defines a class `AIUtil` that encapsulates operations
# on the Azure OpenAI service.
# Chris Joakim, 3Cloud/Cognizant, 2026


class AIUtil:
    def __init__(self):
        self.completions_client = None
        self.embeddings_client = None

    async def generate_completion(self,
        system_context: str,
        user_prompt: str,
        deployment_name: str | None = None) -> object | None:
        try:
            if deployment_name is None:
                deployment_name = os.getenv("AZURE_OPENAI_COMPLETIONS_DEP")
            return self.get_completions_client().chat.completions.create(
                model=deployment_name,
                messages=[
                    {"role": "system", "content": system_context},
                    {"role": "user", "content": user_prompt},
                ],
            )
        except Exception as e:
            print(f"Error generate_completion: {e}")
            print(traceback.format_exc())
            return None

    async def generate_embedding(self, text: str, deployment_name: str | None = None) -> list[float] | None:
        try:
            await asyncio.sleep(0.01)
            if deployment_name is None: 
                deployment_name = os.getenv("AZURE_OPENAI_EMBEDDINGS_DEP")
            return self.get_embeddings_client().embeddings.create(
                input=text, model=deployment_name).data[0].embedding
        except Exception as e:
            print(f"Error generate_embeddings: {e}")
            return None

    def get_completions_client(self) -> AzureOpenAI | None:
        if self.completions_client is None:
            try:
                foundry_name = os.getenv("AZURE_FOUNDRY_NAME")
                endpoint = f"https://{foundry_name}.openai.azure.com/openai/v1/"
                api_key = os.getenv("AZURE_OPENAI_COMPLETIONS_KEY")
                dep = os.getenv("AZURE_OPENAI_COMPLETIONS_DEP")
                logging.debug("AIUtil#get_completions_client name:  {}".format(foundry_name))
                logging.debug("AIUtil#get_completions_client url:   {}".format(endpoint))
                logging.debug("AIUtil#get_completions_client dep:   {}".format(dep))
                logging.debug("AIUtil#get_completions_client key:   {}".format(api_key[0:4]))
                self.completions_client = OpenAI(
                    api_key = api_key,
                    base_url = endpoint,
                )
            except Exception as e:
                logging.error(f"Error in AIUtil#get_completions_client: {e}")
                logging.error(traceback.format_exc())
                return None
        return self.completions_client

    def get_embeddings_client(self) -> AzureOpenAI | None:
        if self.embeddings_client is None:
            try:
                url = os.getenv("AZURE_OPENAI_EMBEDDINGS_URL")
                key = os.getenv("AZURE_OPENAI_EMBEDDINGS_KEY")
                vers = os.getenv("AZURE_OPENAI_EMBEDDINGS_VERSION")
                dep  = os.getenv("AZURE_OPENAI_EMBEDDINGS_DEP")
                logging.debug("AIUtil#get_embeddings_client url:  {}".format(url))
                logging.debug("AIUtil#get_embeddings_client dep:  {}".format(dep))
                logging.debug("AIUtil#get_embeddings_client vers: {}".format(vers))
                logging.debug("AIUtil#get_embeddings_client key:  {}".format(key[0:4]))
                self.embeddings_client = AzureOpenAI(
                    api_key=key, api_version=vers, azure_endpoint=url
                )
            except Exception as e:
                logging.error(f"Error in AIUtil#get_embeddings_client: {e}")
                logging.error(traceback.format_exc())
                return None
        return self.embeddings_client
