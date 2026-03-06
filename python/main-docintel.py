"""
Usage:
  python main-docintel.py <func>
  python main-docintel.py supported_filetypes
  python main-docintel.py extract_text data/documents/2025_Outback_Consumer_Reports_v2.pdf
  python main-docintel.py extract_text data/documents/us_constitution.pdf
  python main-docintel.py extract_text data/documents/PrinceCatalogue.pdf
"""

# Chris Joakim, 3Cloud/Cognizant, 2026

import asyncio
import sys
import os
import traceback

from docopt import docopt
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential

from azure.ai.documentintelligence.aio import (
    DocumentIntelligenceClient as DocumentIntelligenceAsyncClient,
)
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import DocumentContentFormat
from azure.ai.documentintelligence.models import DocumentAnalysisFeature

from src.io.fs import FS


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


def supported_filetypes() -> list[str]:
    """
    Return the filetypes supported by Document Intelligence, plus 'md':
    Filetypes: bmp, docx, heif, html, jpeg, jpg, md, pdf, png, pptx, tiff, xlsx
    """
    general_types = "pdf,html"
    images_types = "jpeg,jpg,png,bmp,heif,tiff"
    ms_office_types = "docx,xlsx,pptx"
    additional_types = "md"  # TODO: what about txt?
    all_types = f"{general_types},{images_types},{ms_office_types},{additional_types}"
    return sorted(all_types.lower().strip().split(","))


def build_async_docintel_client() -> DocumentIntelligenceAsyncClient | None:
    try:
        endpoint = os.environ.get("AZURE_DOCINTEL_URL")
        key = os.environ.get("AZURE_DOCINTEL_KEY")
        print(f"endpoint: {endpoint}")
        client = DocumentIntelligenceAsyncClient(
            endpoint=endpoint, credential=AzureKeyCredential(key)
        )
        return client
    except Exception as e:
        print("Error building Document Intelligence client:")
        print(str(e))
        print(traceback.format_exc())
        return None


async def extract_text(infile: str):
    di_client: build_async_docintel_client = build_async_docintel_client()
    print(f"Analyzing file: {infile} ...")

    output_format = DocumentContentFormat.MARKDOWN
    features_list = list()
    # features.append(DocumentAnalysisFeature.STYLE_FONT)

    async with di_client:
        with open(infile, "rb") as f:
            poller = await di_client.begin_analyze_document(
                "prebuilt-layout",
                body=f,
                output_content_format=output_format,
                features=features_list,
            )
            print(f"poller type: {str(type(poller))}")

        result: AnalyzeResult = await poller.result()
        print(f"result type: {str(type(result))}")
        print(f"result page count is {len(result.pages)}")
        print(f"result content:\n{result.content}\n")

        basename = os.path.basename(infile)
        content_outfile = f"tmp/{basename}.md"
        result_outfile = f"tmp/{basename}.json"
        FS.write(result.content, content_outfile)
        FS.write_json(result.as_dict(), result_outfile)


if __name__ == "__main__":
    try:
        load_dotenv(override=True)
        if len(sys.argv) < 2:
            print_options("Error: no CLI args provided")
        else:
            func = sys.argv[1].lower()
            if func == "supported_filetypes":
                types = supported_filetypes()
                print("Supported file types: {}".format(", ".join(types)))
            elif func == "extract_text":
                infile = sys.argv[2]
                asyncio.run(extract_text(infile))
            else:
                print_options("Error: invalid function: {}".format(func))
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
