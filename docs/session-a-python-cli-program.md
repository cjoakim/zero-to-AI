# Part 1, Session 3 - A Python CLI (Command Line Interface) Program


## In this session we'll cover the following topics:

- Running a Python program from the command line
- The **__main__** entry point
- Importing standard libraries, third-party libraries, and our own code
- Command Line Arguments
- Branching with the **if**, **elif**, and **else** statements
- Looping/Iteration with the **for** statement
- Environment Variables
- Exception Handling with the **try** and **except** statements
  - Ignore the exceptions with the **pass** statement in this example program
- Built-in functions - float() and sorted()
- Invoking HTTP GET requests synchronously and asynchronously with the **httpx** library
- Synchronous and Asynchronous Programming
- Common Built-in Datatypes you'll use in every program:
  - str - string values (text values, such as "Hello, World!")
  - int - integer numbers
  - float - floating-point numbers
  - dict - dictionary, a set of key-value pairs, such as os.environ
  - list - an array of sequential values, such as sys.argv
- Indentation matters in Python
  - It must be properly indented or you'll get an error at runtime

This session uses file **main-cli-sample.py** as our Python CLI program.

Python is a relatively simple language, and this sample program
goes far in demonstrating the core concepts of the language.


<br><br><br>
---
<br><br><br>

## What does this program do?

Let's execute it to ask it for help.

```
python main-cli-sample.py help
```

It responds with:

```
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
```

<br><br><br>

### Wait, how was that help content created?

The program uses the **docopt** library for this.

It's important give users of your program instructions on how to use it.

We define our help content in a multi-line string comment at the top of the file.

Python multi-line string values begin with three double quotes (""") and end with three double quotes (""").

<br><br><br>
---
<br><br><br>

## Demonstration 

These topics are best described by walking through the the code and executing it.

---

### Add Numbers provided on the command line

```
python main-cli-sample.py add_numbers 1 2 3 4 5

sys.argv: ['main-cli-sample.py', 'add_numbers', '1', '2', '3', '4', '5']
1
2
3
4
5
The total is 15.0
```

Let's try it with an invalid number.

```
python main-cli-sample.py add_numbers 1 2 3 4 oops 5

sys.argv: ['main-cli-sample.py', 'add_numbers', '1', '2', '3', '4', 'oops', '5']
1
2
3
4
oops
could not convert string to float: 'oops'
Traceback (most recent call last):
  File "/Users/cjoakim/github/zero-to-AI-private/python/main-cli-sample.py", line 100, in <module>
    add_numbers()
    ~~~~~~~~~~~^^
  File "/Users/cjoakim/github/zero-to-AI-private/python/main-cli-sample.py", line 46, in add_numbers
    n = float(arg)  # convert the command line string value to a floating-point number
ValueError: could not convert string to float: 'oops'
```

---

### Add Numbers provided on the command line, but with exception handling

```
python main-cli-sample.py add_numbers_better 1 2 3 4 oops 5
1
2
3
4
oops
5
The total is 15.0
```

oops is not a number, so it is ignored.

The **try/except** statement is used to catch exceptions, and either handle or ignore them.

---

### Print Environment Variables

Display the environment variable names on your system, or in the **.env** file,
in sorted order with the **sorted()** built-in function.

```
python main-cli-sample.py print_environment_variables

...
AZURE_COSMOSDB_EMULATOR_ACCT
AZURE_COSMOSDB_EMULATOR_KEY
AZURE_COSMOSDB_EMULATOR_URI
AZURE_COSMOSDB_NOSQL_ACCT
AZURE_COSMOSDB_NOSQL_AUTHTYPE
AZURE_COSMOSDB_NOSQL_CONN_STR
AZURE_COSMOSDB_NOSQL_KEY
AZURE_COSMOSDB_NOSQL_URI
...
```

Create or edit the .env file in the python directory, and run this again.
You should see the your new environment variable(s).

---

### Download OpenFlights Airports

This uses the **httpx** library to invoke an HTTP GET request to the OpenFlights API.

```
python main-cli-sample.py download_openflights_airports

 python main-cli-sample.py download_openflights_airports | head
response: <Response [200 OK]>
response.status_code: 200
response.text: 1,"Goroka Airport","Goroka","Papua New Guinea","GKA","AYGA",-6.081689834590001,145.391998291,5282,10,"U","Pacific/Port_Moresby","airport","OurAirports"
2,"Madang Airport","Madang","Papua New Guinea","MAG","AYMD",-5.20707988739,145.789001465,20,10,"U","Pacific/Port_Moresby","airport","OurAirports"
3,"Mount Hagen Kagamuga Airport","Mount Hagen","Papua New Guinea","HGU","AYMH",-5.826789855957031,144.29600524902344,5388,10,"U","Pacific/Port_Moresby","airport","OurAirports"

...

14108,"Krechevitsy Air Base","Novgorod","Russia",\N,"ULLK",58.625,31.385000228881836,85,\N,\N,\N,"airport","OurAirports"
14109,"Desierto de Atacama Airport","Copiapo","Chile","CPO","SCAT",-27.2611999512,-70.7791976929,670,\N,\N,\N,"airport","OurAirports"
14110,"Melitopol Air Base","Melitopol","Ukraine",\N,"UKDM",46.880001,35.305,0,\N,\N,\N,"airport","OurAirports"
```

---

### Code Formatting

This program was formatted using the **ruff** program.

It's good to use a standard code style on your projects as it 
enhances readability and reduces team friction.

```
ruff format main-cli-sample.py
1 file reformatted
```

---

### main-cli-sample.py

The complete program is shown below:

```
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

```
