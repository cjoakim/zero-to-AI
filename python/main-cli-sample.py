"""
Usage:
  python main-cli-sample.py <func>
  python main-cli-sample.py add_numbers 1 2 3 4 5
  python main-cli-sample.py add_numbers_better 1 2 3 4 oops 5
  python main-cli-sample.py print_environment_variables
  python main-cli-sample.py download_openflights_airports
  python main-cli-sample.py download_openflights_airports_async
Options:
  -h --help     Show this screen
  --version     Show version
"""

# The above content is so that the docopt library can display command-line help
# regarding how to run this program.

# Import statements are used to load the necessary standard libraries,
# third-party libraries, and our own code into the program.
# These are typically in this sequence - standard libraries, third-party libraries, our own code.

import os  # standard library for operating system-related functions
import sys  # standard library for system-related functions
import traceback  # standard library for traceback functions

import asyncio  # pythonlibrary for asynchronous programming (async/await)
import httpx  # python library for HTTP requests

from docopt import docopt
from dotenv import load_dotenv  # from the dotenv library use the load_dotenv function

from src.io.fs import (
    FS,
)  # class FS is in the src/fs.py file, our own code for filesystem operations


def print_options():
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


def add_numbers():
    total = 0.0
    print(f"sys.argv: {sys.argv}")  # print the command line arguments
    for arg in sys.argv[2:]:  # iterate the command line arguments, ignoring the first two
        print(arg)  # print the command line argument
        n = float(arg)  # convert the command line string value to a floating-point number
        total = total + n  # float() is one of the Python built-in functions
    print(f"The total is {total}")


def add_numbers_better():
    total = 0.0
    for arg in sys.argv[2:]:
        print(arg)
        try:
            n = float(arg)
            total = total + n
        except Exception as e:  # "catch any exceptions"
            pass  # ignore the non-numeric arguments provided on the command line
    print(f"The total is {total}")


def print_environment_variables():
    env_var_names = sorted(os.environ.keys())  # get a sorted list of the environment variable names
    for name in env_var_names:
        print(f"{name}")
        # print(f"{name}: {os.environ[name]}")


def openflights_airports_url() -> str:
    # See https://openflights.org/data#airport
    return "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"


def download_openflights_airports():
    # This is a synchronous HTTP GET request
    url = openflights_airports_url()
    response = httpx.get(url)
    print(f"response: {response}")
    print(f"response.status_code: {response.status_code}")
    print(f"response.text: {response.text}")


async def download_openflights_airports_async():
    # This is an asynchronous HTTP GET request
    # Several languages use the "async/await" syntax to write asynchronous code
    async with httpx.AsyncClient() as client:
        response = await client.get(openflights_airports_url())
        print(f"Status Code: {response.status_code}")
        print(f"Content Type: {response.headers['content-type']}")
        print(response.text)


if __name__ == "__main__":  # __main__ is execute when the program is run from the command line
    try:
        load_dotenv(override=True)  # load the .env file into the environment
        func = sys.argv[1].lower()  # get the function name from the command line
        # sys.argv is a list of command line arguments
        if func == "add_numbers":
            add_numbers()
        elif func == "add_numbers_better":
            add_numbers_better()
        elif func == "print_environment_variables":
            print_environment_variables()
        elif func == "download_openflights_airports":
            download_openflights_airports()
        elif func == "download_openflights_airports_async":
            asyncio.run(download_openflights_airports_async())
        else:
            print_options()
    except Exception as e:
        print(str(e))  # print the error message
        print(traceback.format_exc())  # print the traceback, or stack trace
