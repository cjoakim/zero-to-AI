# Part 1, Session 2 - Installing Python and Tooling

<br><br>

**This may be the most important session in this series, as it will enable you to be successful with this series, and with Python and AI in general.**

Please get Python and uv installed on your computer in the days ahead.

<br>

## Install Python 3.1x

- Please use **python.org python**, not Anaconda or other distributions
- 3.13 or 3.14
- [Download Page](https://www.python.org/downloads/)
- [YouTube Video on Installing Python on Windows 11](https://www.youtube.com/watch?v=fjzwqEoFTww)

<br><br><br>
---
<br><br><br>

## What are "Package Managers"?

- **They allow you to define, then reconcile and install, the third-party libraries in your project**
- **The Python ecosystem has a huge number of third-party libraries/packages**
  - See **PyPI (Python Package Index)** at https://pypi.org
- For example, if you want to use Azure Cosmos DB and Azure Storage in your project
  - Defined, in this series, in the **pyproject.toml file** - discussed below
  - See [azure-cosmos @ pypi](https://pypi.org/project/azure-cosmos/)
  - See [azure-storage @ pypi](https://pypi.org/project/azure-storage/)
- Current python package manager options are pip, poetry, **uv**, and others
  - This variety of options is typical of open-source
- They determine and resolve the **Dependency Graph** for you 
  - For example, your app uses Library A 
  - Library A uses Library B 
  - Library B uses Library C
  - Library D also uses Library C
  - So download A, B, C, and D from PyPI
  - And use the version of C that is compatible with B and D
  - The dependency graph also includes **the version of each library to use**
- They download the resolved set of dependencies
- **"Dependency Hell"** is where you have incompatible library versions.  For example:
  - Your application depends on libraries A and Library B
  - Library A depends on version 1.0.0 of Library X
  - Library B depends on version 2.0.0 of Library X
- By comparison, the Java ecosystem has several package managers also: Maven and Gradle
- The DotNet ecosystem is much simpler - the dotnet CLI program

<br><br><br>
---
<br><br><br>

## Install the uv package manager

- This is a modern and **very fast python project manager**, written in Rust
- It is much faster than the pip tool
- **uv is used by Microsoft for their Azure SDKs for Python**
  - See [Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)
  - See the sdk directory in the above repository; it contains many SDKs!
- [What is UV?](https://docs.astral.sh/uv/)
- [Installation Instructions](https://docs.astral.sh/uv/getting-started/installation/)
  - Several options are shown there, use the one you're most comfortable with

### Install the uv package manager - On Windows 11

This installation approach worked successfully for our 3Cloud teammate Nazar.
See https://docs.astral.sh/uv/getting-started/installation/#winget

```
winget install --id=astral-sh.uv  -e
```

<br><br>

### ruff 

- **Optionally install ruff if you'd like** - it's not required in this series
- An extremely fast Python **linter and code formatter**, written in Rust
  - A linter checks the code for syntax errors
- ruff is a sibling tool to uv, also from Astral
- I use it to reformat my code 
  - See the **code-reformat.ps1** and **code-reformat.sh** scripts in this repository
  - It's a good idea for Development teams to use a standard code style, reduces friction
- [Overview](https://docs.astral.sh/ruff/)
- [Installation Instructions](https://docs.astral.sh/ruff/installation/)
  - Several options are shown there, use the one you're most comfortable with

```
winget install -e --id astral-sh.ruff
```

<br><br><br>
---
<br><br><br>

## Terminology: Python "Virtual Environment"

- A **"Virtual Environment"** is an isolated project-specific version of Python and a set of libraries you need for that project
- So that you can have several python projects on your system 
  - Since each project will have its own unique set of required libraries (i.e. - dependencies)
  - The python [venv module](https://docs.python.org/3/library/venv.html) is the standard way to create a virtual environments
  - The [uv program has a venv command](https://docs.astral.sh/uv/pip/environments/) to create a virtual environment
    - **We will use uv venv in this series.**
  - The **venv.ps1** and **venv.sh** scripts in this repository create a virtual environment for you

<br><br><br>
---
<br><br><br>

## Demonstration - Creating a Python Project with uv

**If you can run the following in PowerShell or macOS/Linux Terminal, then you have successfully installed python and uv.**

```
Command:                            Description:

uv init my-project                  Use the uv program to initialize a new project named my-project

cd my-project/                      Navigate ino the new direcctory (PowerShell or macOS/Linux Terminal)

uv add numpy pandas jupyter         Add three third-party libraries to your project

uv venv                             Creating a new python virtual environment (in the .venv directory)

.\.venv\Scripts\activate            Activate the virtual environment (on Windows, in PowerShell)
- or -
source .venv/bin/activate           Activate the virtual environment (on macOS/Linux, in Terminal)

uv pip install --editable .         Install the libraries into the virtual environment

uv pip list                         See the list of libraries installed in the virtual environment

uv tree                             Display the dependency graph of your project libraries

python --version                    Display the version of python you are using

Python 3.14.2                       See the output in your PowerShell or Terminal (you may have a different version)

python main.py                      Run the program (the main.py file)

Hello from my-project!              See the output from main.py
```

<br><br>

Note: The **venv.ps1** (Windows PowerShell) and **venv.sh** (macOS/Linus bash)
scripts in this repository execute the last several commands shown above.
You can copy and reuse these scripts in your own projects (I do).

Note: The **activate.ps1** (Windows PowerShell) and **activate.sh** (macOS/Linus bash)
scripts in this repository can be used to activate the virtual environment.
You can copy and reuse these scripts in your own projects (I do).

Note: If you're on Windows, and you're using PowerShell, you may need to enable 
ps1 script execution, with the following command. 

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Windows PowerShell scripts end with the .ps1 extension, while 
macOS/Linux bash scripts end with the .sh extension.

<br><br><br>
---
<br><br><br>

### Wait, when do you create and activate a python virtual environment?

#### Create 

- You should **create** a virtual environment when you start a new project
- Or start using a project for the first time (i.e. - this zero-to-AI/python project)
- Or when your project's dependencies change

#### Activate

- You must **activate** the virtual environment each time you navigate into that project directory
- Activate on Windows with the **.venv\Scripts\activate** command
- Activate on macOS/Linux with the **source .venv/bin/activate** command

<br><br><br>
---
<br><br><br>

## Your Homework 

- Install Python and uv as described in this session
- Run the above demonstration on your computer
  - Execute the **venv.ps1** or **venv.sh** scripts in this repository
  - Execute the **activate.ps1** or **activate.sh** scripts in this repository
  - Execute "python main.py --help"
- Post this message into the Teams Channel: "Installed Python and uv, and ran the demonstration!"
  - This will enable us to know that the group is successful
  - Reach out in the Teams Channel if you get stuck

### What if I see something like this?

It's ok.

There seems to be an issue the docopt library that creates the first few 
error lines when the virtual environment is used for the first time. 

The "IndexError: list index out of range" part error is caused by 
not providing enough command-line arguments to the main.py program.

```
python main.py

/Users/cjoakim/github/zero-to-AI/python/.venv/lib/python3.14/site-packages/docopt.py:165: SyntaxWarning: "\S" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\S"? A raw string is also an option.
  name = re.findall('(<\S*?>)', source)[0]
/Users/cjoakim/github/zero-to-AI/python/.venv/lib/python3.14/site-packages/docopt.py:166: SyntaxWarning: "\[" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\["? A raw string is also an option.
  value = re.findall('\[default: (.*)\]', source, flags=re.I)
/Users/cjoakim/github/zero-to-AI/python/.venv/lib/python3.14/site-packages/docopt.py:207: SyntaxWarning: "\[" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\["? A raw string is also an option.
  matched = re.findall('\[default: (.*)\]', description, flags=re.I)
/Users/cjoakim/github/zero-to-AI/python/.venv/lib/python3.14/site-packages/docopt.py:456: SyntaxWarning: "\S" is an invalid escape sequence. Such sequences will not work in the future. Did you mean "\\S"? A raw string is also an option.
  split = re.split('\n *(<\S+?>|-\S+?)', doc)[1:]
list index out of range
Traceback (most recent call last):
  File "/Users/cjoakim/github/zero-to-AI/python/main.py", line 93, in <module>
    func = sys.argv[1].lower()
           ~~~~~~~~^^^
IndexError: list index out of range
```

<br><br><br>
---
<br><br><br>

## The pyproject.toml file

- uv uses this file to define your project - the dependencies, etc.
- Dependencies are the third-party libraries that your project uses
- Python has a rich set of **Standard Libraries**
- But you can also use **Third-party Libraries**
  - One reason why Python is so popular is because of the rich set of third-party libraries available
  - Such as the **Microsoft Azure SDKs for Python**
  - **FastAPI**, **FastMCP**, **SQLAlchemy**, etc.
  - See [PyPI (Python Package Index)](https://pypi.org) for these libraries

See file **python/pyproject.toml** in this repository.

Note that you can optionally specify specific versions of the libraries you use.

```
[project]
name = "zero-to-AI"
version = "0.1.0"
dependencies = [
  "agent-framework",
  "aiohttp>=3.11.18",
  "azure-ai-documentintelligence==1.0.2",
  "azure-ai-projects",
  "azure-core==1.36.0",
  "azure-cosmos>=4.9.0",
  "azure-identity",
  "azure-mgmt-cognitiveservices",
  "azure-search-documents==11.5.2",
  "azure-storage-blob",
  "beautifulsoup4",
  "docopt",
  "duckdb>=1.4.3",
  "Faker",
  "geopy",
  "h11>=0.14.0",
  "httpx",
  "Jinja2>= 3.1.4",
  "openai>=1.96.0",
  "pandas", 
  "psutil",
  "pydantic-core>=2.41.0",
  "pytest-asyncio>=1.0.0",
  "pytest-cov>=6.1.1",
  "pytest>= 8.3.5",
  "python-dotenv>=1.1.1",
  "pytz",
  "six==1.17.0",
  "tenacity>=9.1.2",
  "tiktoken>=0.12.0"
]
requires-python = ">=3.13"
authors = [
  {name = "Chris Joakim", email = "christopher.joakim@gmail.com"}
]
maintainers = [
  {name = "Chris Joakim", email = "christopher.joakim@gmail.com"}
]
description = "The 'zero-to-AI' series of lessons at 3Cloud"
readme = "readme.md"
license = "MIT"
license-files = ["LICEN[CS]E.*"]
keywords = ["python", "AI", "3Cloud", "internal", "training"]
classifiers = [
  "Programming Language :: Python"
]

[project.urls]
Homepage = "https://github.com/cjoakim/zero-to-AI/"

[tool.ruff]
line-length = 100

[tool.ruff.lint]
ignore = ["E722"]
```

<br><br><br>
---
<br><br><br>

## References

- [venv and Virtual Environments](https://docs.python.org/3/library/venv.html)
- [Creating Projects with uv](https://docs.astral.sh/uv/concepts/projects/init/)
- [TOML, A config file format for humans](https://toml.io/en/)
- [The tomllib standard library](https://docs.python.org/3/library/tomllib.html)
- [Microsoft Azure SDK for Python](https://github.com/Azure/azure-sdk-for-python)

<br><br><br>
---
<br><br><br>

## Wait, what's a "Standard Library"?

- Python is a programming language with a defined yntax
- But it also includes a built-in set of libraries that are included with the python distribution
  - **"Batteries included"**
- [The Standard Libraries](https://docs.python.org/3/library/index.html)


<br><br><br>
---
<br><br><br>

## uv library list 

You can run command **uv pip list** to see the list of libraries installed in your virtual environment
for this series.

This list will evolve over time as the course is developed,but you should see similar results.

### uv pip list 

```
$ uv pip list

Package                                  Version      Editable project location
---------------------------------------- ------------ -----------------------------------------------
agent-framework                          1.0.0b251120
agent-framework-core                     1.0.0b251001
aiofiles                                 25.1.0
aiohappyeyeballs                         2.6.1
aiohttp                                  3.13.2
aiosignal                                1.4.0
annotated-types                          0.7.0
anyio                                    4.12.0
appnope                                  0.1.4
argon2-cffi                              25.1.0
argon2-cffi-bindings                     25.1.0
arrow                                    1.4.0
asgiref                                  3.11.0
asttokens                                3.0.1
async-lru                                2.0.5
attrs                                    25.4.0
azure-ai-agents                          1.1.0
azure-ai-documentintelligence            1.0.2
azure-ai-projects                        1.0.0
azure-common                             1.1.28
azure-core                               1.36.0
azure-core-tracing-opentelemetry         1.0.0b12
azure-cosmos                             4.14.3
azure-identity                           1.25.1
azure-mgmt-cognitiveservices             14.1.0
azure-mgmt-core                          1.6.0
azure-monitor-opentelemetry              1.8.2
azure-monitor-opentelemetry-exporter     1.0.0b45
azure-search-documents                   11.5.2
azure-storage-blob                       12.27.1
babel                                    2.17.0
beautifulsoup4                           4.14.3
bleach                                   6.3.0
certifi                                  2025.11.12
cffi                                     2.0.0
charset-normalizer                       3.4.4
click                                    8.3.1
comm                                     0.2.3
coverage                                 7.13.1
cryptography                             46.0.3
debugpy                                  1.8.19
decorator                                5.2.1
defusedxml                               0.7.1
distro                                   1.9.0
docopt                                   0.6.2
duckdb                                   1.4.3
executing                                2.2.1
faker                                    39.0.0
fastjsonschema                           2.21.2
fqdn                                     1.5.1
frozenlist                               1.8.0
geographiclib                            2.1
geopy                                    2.4.1
googleapis-common-protos                 1.72.0
grpcio                                   1.76.0
h11                                      0.16.0
httpcore                                 1.0.9
httpx                                    0.28.1
httpx-sse                                0.4.3
idna                                     3.11
importlib-metadata                       8.7.1
iniconfig                                2.3.0
ipykernel                                7.1.0
ipython                                  9.8.0
ipython-pygments-lexers                  1.1.1
ipywidgets                               8.1.8
isodate                                  0.7.2
isoduration                              20.11.0
jedi                                     0.19.2
jinja2                                   3.1.6
jiter                                    0.12.0
json5                                    0.12.1
jsonpointer                              3.0.0
jsonschema                               4.25.1
jsonschema-specifications                2025.9.1
jupyter                                  1.1.1
jupyter-client                           8.7.0
jupyter-console                          6.6.3
jupyter-core                             5.9.1
jupyter-events                           0.12.0
jupyter-lsp                              2.3.0
jupyter-server                           2.17.0
jupyter-server-terminals                 0.5.3
jupyterlab                               4.5.1
jupyterlab-pygments                      0.3.0
jupyterlab-server                        2.28.0
jupyterlab-widgets                       3.0.16
lark                                     1.3.1
markupsafe                               3.0.3
matplotlib-inline                        0.2.1
mcp                                      1.25.0
mistune                                  3.2.0
msal                                     1.34.0
msal-extensions                          1.3.1
msrest                                   0.7.1
multidict                                6.7.0
nbclient                                 0.10.4
nbconvert                                7.16.6
nbformat                                 5.10.4
nest-asyncio                             1.6.0
notebook                                 7.5.1
notebook-shim                            0.2.4
numpy                                    2.4.0
oauthlib                                 3.3.1
openai                                   2.14.0
opentelemetry-api                        1.39.1
opentelemetry-exporter-otlp-proto-common 1.39.1
opentelemetry-exporter-otlp-proto-grpc   1.39.1
opentelemetry-instrumentation            0.60b1
opentelemetry-instrumentation-asgi       0.60b1
opentelemetry-instrumentation-dbapi      0.60b1
opentelemetry-instrumentation-django     0.60b1
opentelemetry-instrumentation-fastapi    0.60b1
opentelemetry-instrumentation-flask      0.60b1
opentelemetry-instrumentation-psycopg2   0.60b1
opentelemetry-instrumentation-requests   0.60b1
opentelemetry-instrumentation-urllib     0.60b1
opentelemetry-instrumentation-urllib3    0.60b1
opentelemetry-instrumentation-wsgi       0.60b1
opentelemetry-proto                      1.39.1
opentelemetry-resource-detector-azure    0.1.5
opentelemetry-sdk                        1.39.1
opentelemetry-semantic-conventions       0.60b1
opentelemetry-semantic-conventions-ai    0.4.13
opentelemetry-util-http                  0.60b1
packaging                                25.0
pandas                                   2.3.3
pandocfilters                            1.5.1
parso                                    0.8.5
pexpect                                  4.9.0
platformdirs                             4.5.1
pluggy                                   1.6.0
prometheus-client                        0.23.1
prompt-toolkit                           3.0.52
propcache                                0.4.1
protobuf                                 6.33.2
psutil                                   7.2.0
ptyprocess                               0.7.0
pure-eval                                0.2.3
pycparser                                2.23
pydantic                                 2.12.5
pydantic-core                            2.41.5
pydantic-settings                        2.12.0
pygments                                 2.19.2
pyjwt                                    2.10.1
pytest                                   9.0.2
pytest-asyncio                           1.3.0
pytest-cov                               7.0.0
python-dateutil                          2.9.0.post0
python-dotenv                            1.2.1
python-json-logger                       4.0.0
python-multipart                         0.0.21
pytz                                     2025.2
pyyaml                                   6.0.3
pyzmq                                    27.1.0
referencing                              0.37.0
regex                                    2025.11.3
requests                                 2.32.5
requests-oauthlib                        2.0.0
rfc3339-validator                        0.1.4
rfc3986-validator                        0.1.1
rfc3987-syntax                           1.1.0
rpds-py                                  0.30.0
send2trash                               1.8.3
setuptools                               80.9.0
six                                      1.17.0
sniffio                                  1.3.1
soupsieve                                2.8.1
sse-starlette                            3.1.1
stack-data                               0.6.3
starlette                                0.50.0
tenacity                                 9.1.2
terminado                                0.18.1
tiktoken                                 0.12.0
tinycss2                                 1.4.0
tornado                                  6.5.4
tqdm                                     4.67.1
traitlets                                5.14.3
typing-extensions                        4.15.0
typing-inspection                        0.4.2
tzdata                                   2025.3
uri-template                             1.3.0
urllib3                                  2.6.2
uvicorn                                  0.40.0
wcwidth                                  0.2.14
webcolors                                25.10.0
webencodings                             0.5.1
websocket-client                         1.9.0
websockets                               15.0.1
widgetsnbextension                       4.0.15
wrapt                                    1.17.3
yarl                                     1.22.0
zero-to-ai                               0.1.0        /Users/cjoakim/github/zero-to-AI/python
zipp                                     3.23.0
```

<br><br><br>
---
<br><br><br>

## uv library dependency graph 

- The package managers do a lot "under the covers"
- They not only install the libraries that you specify in your pyproject.toml file
- But they install the dependencies of those libraries
- And the dependencies of those, and on and on ...
- This is called a "dependency graph"
- uv strives to reconcile the versions of the libraries to avoid "dependency hell"
- The following is a visualization of the dependency graph for the zero-to-AI project
- Execute it with the **uv tree** command
- This graph will evolve over time, but you should see similar results

### Incompatible dependencies (aka: "dependency hell") looks like this 

When running the venv.ps1 or venv.sh script, you'll see an error similar to the following:

```
...
Creating a new virtual environment in .venv ...
Using CPython 3.14.3 interpreter at: /opt/homebrew/opt/python@3.14/bin/python3.14
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
Activating the virtual environment ...
Installing libraries ...
  × No solution found when resolving dependencies:
  ╰─▶ Because toon-python was not found in the package registry and zero-to-ai==1.0.0 depends on toon-python, we can
      conclude that zero-to-ai==1.0.0 cannot be used.
      And because only zero-to-ai==1.0.0 is available and you require zero-to-ai, we can conclude that your
      requirements are unsatisfiable.
Creating a requirements.txt file for users of pip instead of uv ...
  × No solution found when resolving dependencies:
  ╰─▶ Because toon-python was not found in the package registry and zero-to-ai depends on toon-python, we can conclude
      that your requirements are unsatisfiable.
```

### uv tree

```
uv tree

Resolved 198 packages in 5ms

zero-to-ai v0.1.0
├── agent-framework v1.0.0b251120
│   └── agent-framework-core v1.0.0b251001
│       ├── aiofiles v25.1.0
│       ├── azure-identity v1.25.1
│       │   ├── azure-core v1.36.0
│       │   │   ├── requests v2.32.5
│       │   │   │   ├── certifi v2025.11.12
│       │   │   │   ├── charset-normalizer v3.4.4
│       │   │   │   ├── idna v3.11
│       │   │   │   └── urllib3 v2.6.2
│       │   │   └── typing-extensions v4.15.0
│       │   ├── cryptography v46.0.3
│       │   │   └── cffi v2.0.0
│       │   │       └── pycparser v2.23
│       │   ├── msal v1.34.0
│       │   │   ├── cryptography v46.0.3 (*)
│       │   │   ├── pyjwt[crypto] v2.10.1
│       │   │   │   └── cryptography v46.0.3 (extra: crypto) (*)
│       │   │   └── requests v2.32.5 (*)
│       │   ├── msal-extensions v1.3.1
│       │   │   └── msal v1.34.0 (*)
│       │   └── typing-extensions v4.15.0
│       ├── azure-monitor-opentelemetry v1.8.2
│       │   ├── azure-core v1.36.0 (*)
│       │   ├── azure-core-tracing-opentelemetry v1.0.0b12
│       │   │   ├── azure-core v1.36.0 (*)
│       │   │   └── opentelemetry-api v1.39.1
│       │   │       ├── importlib-metadata v8.7.1
│       │   │       │   └── zipp v3.23.0
│       │   │       └── typing-extensions v4.15.0
│       │   ├── azure-monitor-opentelemetry-exporter v1.0.0b45
│       │   │   ├── azure-core v1.36.0 (*)
│       │   │   ├── azure-identity v1.25.1 (*)
│       │   │   ├── msrest v0.7.1
│       │   │   │   ├── azure-core v1.36.0 (*)
│       │   │   │   ├── certifi v2025.11.12
│       │   │   │   ├── isodate v0.7.2
│       │   │   │   ├── requests v2.32.5 (*)
│       │   │   │   └── requests-oauthlib v2.0.0
│       │   │   │       ├── oauthlib v3.3.1
│       │   │   │       └── requests v2.32.5 (*)
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-sdk v1.39.1
│       │   │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   │   ├── opentelemetry-semantic-conventions v0.60b1
│       │   │   │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   │   │   └── typing-extensions v4.15.0
│       │   │   │   └── typing-extensions v4.15.0
│       │   │   └── psutil v7.2.0
│       │   ├── opentelemetry-instrumentation-django v0.60b1
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-instrumentation v0.60b1
│       │   │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   │   ├── packaging v25.0
│       │   │   │   └── wrapt v1.17.3
│       │   │   ├── opentelemetry-instrumentation-wsgi v0.60b1
│       │   │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   │   └── opentelemetry-util-http v0.60b1
│       │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   └── opentelemetry-util-http v0.60b1
│       │   ├── opentelemetry-instrumentation-fastapi v0.60b1
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   ├── opentelemetry-instrumentation-asgi v0.60b1
│       │   │   │   ├── asgiref v3.11.0
│       │   │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   │   └── opentelemetry-util-http v0.60b1
│       │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   └── opentelemetry-util-http v0.60b1
│       │   ├── opentelemetry-instrumentation-flask v0.60b1
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   ├── opentelemetry-instrumentation-wsgi v0.60b1 (*)
│       │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   ├── opentelemetry-util-http v0.60b1
│       │   │   └── packaging v25.0
│       │   ├── opentelemetry-instrumentation-psycopg2 v0.60b1
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   └── opentelemetry-instrumentation-dbapi v0.60b1
│       │   │       ├── opentelemetry-api v1.39.1 (*)
│       │   │       ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │       ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │       └── wrapt v1.17.3
│       │   ├── opentelemetry-instrumentation-requests v0.60b1
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   └── opentelemetry-util-http v0.60b1
│       │   ├── opentelemetry-instrumentation-urllib v0.60b1
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   └── opentelemetry-util-http v0.60b1
│       │   ├── opentelemetry-instrumentation-urllib3 v0.60b1
│       │   │   ├── opentelemetry-api v1.39.1 (*)
│       │   │   ├── opentelemetry-instrumentation v0.60b1 (*)
│       │   │   ├── opentelemetry-semantic-conventions v0.60b1 (*)
│       │   │   ├── opentelemetry-util-http v0.60b1
│       │   │   └── wrapt v1.17.3
│       │   ├── opentelemetry-resource-detector-azure v0.1.5
│       │   │   └── opentelemetry-sdk v1.39.1 (*)
│       │   └── opentelemetry-sdk v1.39.1 (*)
│       ├── azure-monitor-opentelemetry-exporter v1.0.0b45 (*)
│       ├── mcp[ws] v1.25.0
│       │   ├── anyio v4.12.0
│       │   │   └── idna v3.11
│       │   ├── httpx v0.28.1
│       │   │   ├── anyio v4.12.0 (*)
│       │   │   ├── certifi v2025.11.12
│       │   │   ├── httpcore v1.0.9
│       │   │   │   ├── certifi v2025.11.12
│       │   │   │   └── h11 v0.16.0
│       │   │   └── idna v3.11
│       │   ├── httpx-sse v0.4.3
│       │   ├── jsonschema v4.25.1
│       │   │   ├── attrs v25.4.0
│       │   │   ├── jsonschema-specifications v2025.9.1
│       │   │   │   └── referencing v0.37.0
│       │   │   │       ├── attrs v25.4.0
│       │   │   │       └── rpds-py v0.30.0
│       │   │   ├── referencing v0.37.0 (*)
│       │   │   ├── rpds-py v0.30.0
│       │   │   ├── fqdn v1.5.1 (extra: format-nongpl)
│       │   │   ├── idna v3.11 (extra: format-nongpl)
│       │   │   ├── isoduration v20.11.0 (extra: format-nongpl)
│       │   │   │   └── arrow v1.4.0
│       │   │   │       ├── python-dateutil v2.9.0.post0
│       │   │   │       │   └── six v1.17.0
│       │   │   │       └── tzdata v2025.3
│       │   │   ├── jsonpointer v3.0.0 (extra: format-nongpl)
│       │   │   ├── rfc3339-validator v0.1.4 (extra: format-nongpl)
│       │   │   │   └── six v1.17.0
│       │   │   ├── rfc3986-validator v0.1.1 (extra: format-nongpl)
│       │   │   ├── rfc3987-syntax v1.1.0 (extra: format-nongpl)
│       │   │   │   └── lark v1.3.1
│       │   │   ├── uri-template v1.3.0 (extra: format-nongpl)
│       │   │   └── webcolors v25.10.0 (extra: format-nongpl)
│       │   ├── pydantic v2.12.5
│       │   │   ├── annotated-types v0.7.0
│       │   │   ├── pydantic-core v2.41.5
│       │   │   │   └── typing-extensions v4.15.0
│       │   │   ├── typing-extensions v4.15.0
│       │   │   └── typing-inspection v0.4.2
│       │   │       └── typing-extensions v4.15.0
│       │   ├── pydantic-settings v2.12.0
│       │   │   ├── pydantic v2.12.5 (*)
│       │   │   ├── python-dotenv v1.2.1
│       │   │   └── typing-inspection v0.4.2 (*)
│       │   ├── pyjwt[crypto] v2.10.1 (*)
│       │   ├── python-multipart v0.0.21
│       │   ├── sse-starlette v3.1.1
│       │   │   ├── anyio v4.12.0 (*)
│       │   │   └── starlette v0.50.0
│       │   │       └── anyio v4.12.0 (*)
│       │   ├── starlette v0.50.0 (*)
│       │   ├── typing-extensions v4.15.0
│       │   ├── typing-inspection v0.4.2 (*)
│       │   ├── uvicorn v0.40.0
│       │   │   ├── click v8.3.1
│       │   │   └── h11 v0.16.0
│       │   └── websockets v15.0.1 (extra: ws)
│       ├── openai v2.14.0
│       │   ├── anyio v4.12.0 (*)
│       │   ├── distro v1.9.0
│       │   ├── httpx v0.28.1 (*)
│       │   ├── jiter v0.12.0
│       │   ├── pydantic v2.12.5 (*)
│       │   ├── sniffio v1.3.1
│       │   ├── tqdm v4.67.1
│       │   └── typing-extensions v4.15.0
│       ├── opentelemetry-api v1.39.1 (*)
│       ├── opentelemetry-exporter-otlp-proto-grpc v1.39.1
│       │   ├── googleapis-common-protos v1.72.0
│       │   │   └── protobuf v6.33.2
│       │   ├── grpcio v1.76.0
│       │   │   └── typing-extensions v4.15.0
│       │   ├── opentelemetry-api v1.39.1 (*)
│       │   ├── opentelemetry-exporter-otlp-proto-common v1.39.1
│       │   │   └── opentelemetry-proto v1.39.1
│       │   │       └── protobuf v6.33.2
│       │   ├── opentelemetry-proto v1.39.1 (*)
│       │   ├── opentelemetry-sdk v1.39.1 (*)
│       │   └── typing-extensions v4.15.0
│       ├── opentelemetry-sdk v1.39.1 (*)
│       ├── opentelemetry-semantic-conventions-ai v0.4.13
│       ├── pydantic v2.12.5 (*)
│       ├── pydantic-settings v2.12.0 (*)
│       └── typing-extensions v4.15.0
├── aiohttp v3.13.2
│   ├── aiohappyeyeballs v2.6.1
│   ├── aiosignal v1.4.0
│   │   └── frozenlist v1.8.0
│   ├── attrs v25.4.0
│   ├── frozenlist v1.8.0
│   ├── multidict v6.7.0
│   ├── propcache v0.4.1
│   └── yarl v1.22.0
│       ├── idna v3.11
│       ├── multidict v6.7.0
│       └── propcache v0.4.1
├── azure-ai-documentintelligence v1.0.2
│   ├── azure-core v1.36.0 (*)
│   ├── isodate v0.7.2
│   └── typing-extensions v4.15.0
├── azure-ai-projects v1.0.0
│   ├── azure-ai-agents v1.1.0
│   │   ├── azure-core v1.36.0 (*)
│   │   ├── isodate v0.7.2
│   │   └── typing-extensions v4.15.0
│   ├── azure-core v1.36.0 (*)
│   ├── azure-storage-blob v12.27.1
│   │   ├── azure-core v1.36.0 (*)
│   │   ├── cryptography v46.0.3 (*)
│   │   ├── isodate v0.7.2
│   │   └── typing-extensions v4.15.0
│   ├── isodate v0.7.2
│   └── typing-extensions v4.15.0
├── azure-core v1.36.0 (*)
├── azure-cosmos v4.14.3
│   ├── azure-core v1.36.0 (*)
│   └── typing-extensions v4.15.0
├── azure-identity v1.25.1 (*)
├── azure-mgmt-cognitiveservices v14.1.0
│   ├── azure-mgmt-core v1.6.0
│   │   └── azure-core v1.36.0 (*)
│   ├── msrest v0.7.1 (*)
│   └── typing-extensions v4.15.0
├── azure-search-documents v11.5.2
│   ├── azure-common v1.1.28
│   ├── azure-core v1.36.0 (*)
│   ├── isodate v0.7.2
│   └── typing-extensions v4.15.0
├── azure-storage-blob v12.27.1 (*)
├── beautifulsoup4 v4.14.3
│   ├── soupsieve v2.8.1
│   └── typing-extensions v4.15.0
├── docopt v0.6.2
├── duckdb v1.4.3
├── faker v39.0.0
│   └── tzdata v2025.3
├── geopy v2.4.1
│   └── geographiclib v2.1
├── h11 v0.16.0
├── httpx v0.28.1 (*)
├── jinja2 v3.1.6
│   └── markupsafe v3.0.3
├── openai v2.14.0 (*)
├── pandas v2.3.3
│   ├── numpy v2.4.0
│   ├── python-dateutil v2.9.0.post0 (*)
│   ├── pytz v2025.2
│   └── tzdata v2025.3
├── psutil v7.2.0
├── pydantic-core v2.41.5 (*)
├── pytest v9.0.2
│   ├── iniconfig v2.3.0
│   ├── packaging v25.0
│   ├── pluggy v1.6.0
│   └── pygments v2.19.2
├── pytest-asyncio v1.3.0
│   └── pytest v9.0.2 (*)
├── pytest-cov v7.0.0
│   ├── coverage v7.13.1
│   ├── pluggy v1.6.0
│   └── pytest v9.0.2 (*)
├── python-dotenv v1.2.1
├── pytz v2025.2
├── six v1.17.0
├── tenacity v9.1.2
└── tiktoken v0.12.0
    ├── regex v2025.11.3
    └── requests v2.32.5 (*)
my-project v0.1.0
├── jupyter v1.1.1
│   ├── ipykernel v7.1.0
│   │   ├── appnope v0.1.4
│   │   ├── comm v0.2.3
│   │   ├── debugpy v1.8.19
│   │   ├── ipython v9.8.0
│   │   │   ├── decorator v5.2.1
│   │   │   ├── ipython-pygments-lexers v1.1.1
│   │   │   │   └── pygments v2.19.2
│   │   │   ├── jedi v0.19.2
│   │   │   │   └── parso v0.8.5
│   │   │   ├── matplotlib-inline v0.2.1
│   │   │   │   └── traitlets v5.14.3
│   │   │   ├── pexpect v4.9.0
│   │   │   │   └── ptyprocess v0.7.0
│   │   │   ├── prompt-toolkit v3.0.52
│   │   │   │   └── wcwidth v0.2.14
│   │   │   ├── pygments v2.19.2
│   │   │   ├── stack-data v0.6.3
│   │   │   │   ├── asttokens v3.0.1
│   │   │   │   ├── executing v2.2.1
│   │   │   │   └── pure-eval v0.2.3
│   │   │   └── traitlets v5.14.3
│   │   ├── jupyter-client v8.7.0
│   │   │   ├── jupyter-core v5.9.1
│   │   │   │   ├── platformdirs v4.5.1
│   │   │   │   └── traitlets v5.14.3
│   │   │   ├── python-dateutil v2.9.0.post0 (*)
│   │   │   ├── pyzmq v27.1.0
│   │   │   ├── tornado v6.5.4
│   │   │   └── traitlets v5.14.3
│   │   ├── jupyter-core v5.9.1 (*)
│   │   ├── matplotlib-inline v0.2.1 (*)
│   │   ├── nest-asyncio v1.6.0
│   │   ├── packaging v25.0
│   │   ├── psutil v7.2.0
│   │   ├── pyzmq v27.1.0
│   │   ├── tornado v6.5.4
│   │   └── traitlets v5.14.3
│   ├── ipywidgets v8.1.8
│   │   ├── comm v0.2.3
│   │   ├── ipython v9.8.0 (*)
│   │   ├── jupyterlab-widgets v3.0.16
│   │   ├── traitlets v5.14.3
│   │   └── widgetsnbextension v4.0.15
│   ├── jupyter-console v6.6.3
│   │   ├── ipykernel v7.1.0 (*)
│   │   ├── ipython v9.8.0 (*)
│   │   ├── jupyter-client v8.7.0 (*)
│   │   ├── jupyter-core v5.9.1 (*)
│   │   ├── prompt-toolkit v3.0.52 (*)
│   │   ├── pygments v2.19.2
│   │   ├── pyzmq v27.1.0
│   │   └── traitlets v5.14.3
│   ├── jupyterlab v4.5.1
│   │   ├── async-lru v2.0.5
│   │   ├── httpx v0.28.1 (*)
│   │   ├── ipykernel v7.1.0 (*)
│   │   ├── jinja2 v3.1.6 (*)
│   │   ├── jupyter-core v5.9.1 (*)
│   │   ├── jupyter-lsp v2.3.0
│   │   │   └── jupyter-server v2.17.0
│   │   │       ├── anyio v4.12.0 (*)
│   │   │       ├── argon2-cffi v25.1.0
│   │   │       │   └── argon2-cffi-bindings v25.1.0
│   │   │       │       └── cffi v2.0.0 (*)
│   │   │       ├── jinja2 v3.1.6 (*)
│   │   │       ├── jupyter-client v8.7.0 (*)
│   │   │       ├── jupyter-core v5.9.1 (*)
│   │   │       ├── jupyter-events v0.12.0
│   │   │       │   ├── jsonschema[format-nongpl] v4.25.1 (*)
│   │   │       │   ├── packaging v25.0
│   │   │       │   ├── python-json-logger v4.0.0
│   │   │       │   ├── pyyaml v6.0.3
│   │   │       │   ├── referencing v0.37.0 (*)
│   │   │       │   ├── rfc3339-validator v0.1.4 (*)
│   │   │       │   ├── rfc3986-validator v0.1.1
│   │   │       │   └── traitlets v5.14.3
│   │   │       ├── jupyter-server-terminals v0.5.3
│   │   │       │   └── terminado v0.18.1
│   │   │       │       ├── ptyprocess v0.7.0
│   │   │       │       └── tornado v6.5.4
│   │   │       ├── nbconvert v7.16.6
│   │   │       │   ├── beautifulsoup4 v4.14.3 (*)
│   │   │       │   ├── bleach[css] v6.3.0
│   │   │       │   │   ├── webencodings v0.5.1
│   │   │       │   │   └── tinycss2 v1.4.0 (extra: css)
│   │   │       │   │       └── webencodings v0.5.1
│   │   │       │   ├── defusedxml v0.7.1
│   │   │       │   ├── jinja2 v3.1.6 (*)
│   │   │       │   ├── jupyter-core v5.9.1 (*)
│   │   │       │   ├── jupyterlab-pygments v0.3.0
│   │   │       │   ├── markupsafe v3.0.3
│   │   │       │   ├── mistune v3.2.0
│   │   │       │   ├── nbclient v0.10.4
│   │   │       │   │   ├── jupyter-client v8.7.0 (*)
│   │   │       │   │   ├── jupyter-core v5.9.1 (*)
│   │   │       │   │   ├── nbformat v5.10.4
│   │   │       │   │   │   ├── fastjsonschema v2.21.2
│   │   │       │   │   │   ├── jsonschema v4.25.1 (*)
│   │   │       │   │   │   ├── jupyter-core v5.9.1 (*)
│   │   │       │   │   │   └── traitlets v5.14.3
│   │   │       │   │   └── traitlets v5.14.3
│   │   │       │   ├── nbformat v5.10.4 (*)
│   │   │       │   ├── packaging v25.0
│   │   │       │   ├── pandocfilters v1.5.1
│   │   │       │   ├── pygments v2.19.2
│   │   │       │   └── traitlets v5.14.3
│   │   │       ├── nbformat v5.10.4 (*)
│   │   │       ├── packaging v25.0
│   │   │       ├── prometheus-client v0.23.1
│   │   │       ├── pyzmq v27.1.0
│   │   │       ├── send2trash v1.8.3
│   │   │       ├── terminado v0.18.1 (*)
│   │   │       ├── tornado v6.5.4
│   │   │       ├── traitlets v5.14.3
│   │   │       └── websocket-client v1.9.0
│   │   ├── jupyter-server v2.17.0 (*)
│   │   ├── jupyterlab-server v2.28.0
│   │   │   ├── babel v2.17.0
│   │   │   ├── jinja2 v3.1.6 (*)
│   │   │   ├── json5 v0.12.1
│   │   │   ├── jsonschema v4.25.1 (*)
│   │   │   ├── jupyter-server v2.17.0 (*)
│   │   │   ├── packaging v25.0
│   │   │   └── requests v2.32.5 (*)
│   │   ├── notebook-shim v0.2.4
│   │   │   └── jupyter-server v2.17.0 (*)
│   │   ├── packaging v25.0
│   │   ├── setuptools v80.9.0
│   │   ├── tornado v6.5.4
│   │   └── traitlets v5.14.3
│   ├── nbconvert v7.16.6 (*)
│   └── notebook v7.5.1
│       ├── jupyter-server v2.17.0 (*)
│       ├── jupyterlab v4.5.1 (*)
│       ├── jupyterlab-server v2.28.0 (*)
│       ├── notebook-shim v0.2.4 (*)
│       └── tornado v6.5.4
├── numpy v2.4.0
└── pandas v2.3.3 (*)
(*) Package tree already displayed
```

<br><br><br>
---
<br><br><br>

[Home](../README.md)
