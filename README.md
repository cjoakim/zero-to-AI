# zero-to-AI

<br>

<p align="center">
   <img src="docs/img/zero-to-AI-logo-1024.png" width="80%">
</p>

<br>

<p align="center">
<strong>An educational series to take students from zero to hands-on AI skills.</strong>
</p>

<p align="center">
The goal is to <strong>empower students to build AI solutions.</strong>
</p>

<br><br><br>
---
<br><br><br>

# Series Outline

## Part 1 - The Basics

-  0  -  [Preparing for this Series](docs/session-preparing-for-this-series.md)
-  1  -  [Git and GitHub](docs/session-git-and-github.md)
-  2  -  [Installing Python and Tooling](docs/session-installing-python-and-tooling.md)
-  3  -  [A Python CLI (Command Line Interface) Program](docs/session-a-python-cli-program.md)
-  4  -  [A Python UI app with Streamlit](docs/session-a-python-ui-app-with-streamlit.md)
-  CLB -  [Command Line Basics and Catch-up Session](docs/command-line-cheat-sheet.md)
-  5  -  [Data Wrangling](docs/session-data-wrangling.md)
-  6  -  [Notebooks, Jupyter, Dataframes, Pandas](docs/session-jupyter-notebooks.md)
-  7  -  [Unit Testing, CI/CD. and Python Datatypes](docs/session-unit-testing-and-datatypes.md)
-  8  -  [IDEs and Tooling - VSC, GitHub Copilot, Cursor](docs/session-ides-cursor.md)

## Part 2 - Foundational Azure Services

-  9  -  [Azure Storage](docs/session-not-available.md)
-  10  -  [Models, Catalogs, Tokens, Prompts, Foundry](docs/session-not-available.md)
-  11  -  [Azure OpenAI SDK](docs/session-not-available.md)
-  12  -  [Azure CosmosDB](docs/session-not-available.md)
-  13  -  [Azure Search](docs/session-not-available.md)

## Part 3 - AI

-  14  -  [PDF to Markdown with Azure Document Intelligence](docs/session-not-available.md)
-  15  -  [Knowledge Graphs](docs/session-not-available.md)
-  16  -  [MCP, the Model Context Protocol](docs/session-not-available.md)
-  17  -  [Azure Agent Framework](docs/session-not-available.md)
-  18  -  [Your Turn, Create Something!](docs/session-not-available.md)

<br>

Notes:
- Some of these sessions are currently a work-in-progress
- All content is subject to updates
- The Python code is in a working state and is reasonably complete

<br><br>

## Tentative Session Schedule

| Date           | Session |
| -------------- | ------- |
| Tue 2026-02-03 | Preparing for this Series |
| Thu 2026-02-05 | Git and GitHub |
| Tue 2026-02-10 | Installing Python and Tooling |
| Thu 2026-02-12 | A Python CLI (Command Line Interface) Program |
| Tue 2026-02-17 | A Python UI app with Streamlit |
| Thu 2026-02-19 | Command Line Basics and Catch-up Session |
| Thu 2026-02-24 | Data Wrangling |
| Tue 2026-02-26 | Notebooks, Jupyter, Dataframes, Pandas |
| Thu 2026-03-03 | Unit Testing, CI/CD. and Python Datatypes |
| Tue 2026-03-05 | IDEs and Tooling - VSC, GitHub Copilot, Cursor |
| Thu 2026-03-10 | Azure Storage |
| Tue 2026-03-12 | Azure Foundry, Deploying Models/LLMs, Tokens, Throughput |
| Thu 2026-03-17 | Azure OpenAI SDK |
| Tue 2026-03-19 | Azure CosmosDB |
| Thu 2026-03-24 | Azure Search |
| Tue 2026-03-26 | PDF to Markdown with Azure Document Intelligence |
| Thu 2026-03-31 | Knowledge Graphs |
| Tue 2026-04-02 | MCP, the Model Context Protocol |
| Thu 2026-04-07 | Azure Agent Framework |
| Tue 2026-04-09 | Your Turn, Create Something! |

<br><br>
---
<br><br>

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

<br><br>
---
<br><br>

## Series Creator

```
Chris Joakim, 3Cloud/Cognizant, 2026
```
