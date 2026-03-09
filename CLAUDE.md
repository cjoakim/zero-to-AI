# CLAUDE.md

This file guides both Claude Code and Cursor when working with the code
in this repository.  It provides context, constraints, and instructions
on how to interact with the project.

## Project Overview

This repository is for the **zero-to-AI** training series at 3Cloud/Cognizant.

It is intended to be used for internal presentations as well as to provide
a working set of code to support the presentations as well as provide 
a **bootstrap codebase** for students to use as a starting point for their
own projects.

## Tech Stack

- Python 3.14.x
- uv package manager
- ruff code formatter
- pylint code linter
- pytest unit tests
- GitHub Actions for pytest testing and pylint linting
- PowerShell scriptsfor Windows 11 workstations
- bash scripts for Linux and macOS workstations
- Azure OpenAI
- Azure Foundry
- Azure Storage
- Azure CosmosDB
- Azure Search
- Azure Document Intelligence
- MCP Protocol with the fastmcp library 
- Primarily CLI applications
- Streamlit UI
- Jypyter Notebooks
- See the list of Python libraries in the python/pyproject.toml file

## Coding Standards & Rules

- Code should be formatted per the ruff program (i.e. `ruff format`)
- Code should be linted per the pylint program (i.e. `pylint`)
- Generate code per the existing style of the codebase 
- Prefer to generate easy-to-read code rather than an overly clever and concise style

## Program Execution 

- All code executes from within the python/ directory 
- The python virtual environment is created with the following scripts:
  - python/venv.ps1 on Windows 11 with PowerShell
  - python/venv.sh scripts on macOS/Linux with bash and Terminal

## Unit Testing

- These use the pytest library 
- See the python/tests.ps1 and python/tests.sh scripts
- Unit tests are located in the python/tests/ directory

## Documentation 

- See the docs/ and docs/img directories
- Session presentations have the filename prefix of `session-` in the docs/ directory

## Series Schedule

See the README.md file for the series schedule, under the `Tentative Session Schedule` heading.

## Directory Structure of this Repository

```
├── docs                           Documentation, markdown files (*.md)
│   ├── img                        Images
│   └── prompts                    Sample prompts for use with AI
└── python                         The Python code for the series
    ├── aisearch                   Configuration files for Azure AI Search
    ├── cosmos                     Configuration files for Azure Cosmos DB
    ├── data                       Data files for the series
    │   ├── cosmosdb               Cosmos DB JSON documents
    │   ├── documents              Documents for text extraction with Azure Document Intelligence
    │   ├── openflights            OpenFlights airport data
    │   ├── postal_codes           Postal codes for North Carolina, USA
    │   ├── pypi                   Data files related to the Python Package Index (PyPI)
    │   ├── pypi_libs              JSON data for Python Package Index (PyPI) libraries
    │   ├── rdf                    RDF graph data
    │   └── uv                     Data files created by the uv package manager
    ├── htmlcov                    Not in GitHub; created by pytest-cov library
    ├── jupyter                    Jupyter Notebooks
    ├── prompts                    Sample prompts for use with AI
    ├── rdf                        RDF graph files
    ├── src                        Python source code; they end with .py
    │   ├── ai                     AI-related python modules
    │   ├── app                    Application-specific python modules
    │   ├── db                     Database-related python modules (i.e. - Azure Cosmos DB)
    │   ├── io                     Input/Output-related python modules (i.e. - File System, Azure Storage)
    │   ├── os                     Operating system-related python modules
    │   └── util                   Utility python modules
    ├── templates                  Jinja2 text templates
    ├── tests                      Unit tests for the python code, implemented with the pytest library
    │   ├── fixtures               Sample data for the unit tests
    │   └── templates              Jinja2 text templates for the unit tests
``` 
