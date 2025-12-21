# zero-to-AI

An educational series to take students from "zero" to hands-on AI skills.

Empower students to understand and build AI solutions.

---

## Summary

- An educational series for 3Cloud employees in many roles
  - Also form a community and build/strengthen relationships
- Start with the basics, then pertinent Azure Services, then AI
- Make the journey from theory to simple working solutions
  - IMO many people, such as PMs, are stuck in pure theory and can't advance their skills
  - Introduce some "AppDev" skills for Data Engineers
  - Introduce Python to "Low Code" enthusiasts
- Do a shallow but sufficient coverage of each topic
  - 30-minute "bite-size" sessions
- Focus on Python as the implementation language
- Presentations and working code to be in this public GitHub repository
  - Content developed in a corresponding private repository, and ported
  - Create a core set of reusable code for use in future projects
- (Optional) Polished documentation produced by mkdocs, see AIGraph4pg below

---

## Timeline

- Content to be created in January 2026
  - I have most of the code already available
- Sessions start in February, finish in April
- 30-minute sessions, 2x a week, 5:30pm EST Tuesday & Thursday
- 19 sessions = 10 weeks

---

## Meeting Format

- First 5 minutes: Questions and Answers from previous session
- Next 15 minutes: Lecture and Demo
- Last 10 minutes: Questions and Discussion
- Takeaway reading lists and lab at each session
  - Expectation is that students do some homework and reading
- Leverage a 3Cloud Teams channel
  - Post questions here
  - Students-helping-Students
  - Form a community and build relationships
- Record each meeting

## Azure 

- Use a 3Cloud subscription
- All provisioning done by the course instructor (Chris)
  - Storage, Search, Foundry (including models), Cosmos
- All services populated by the course instructor (Chris)
  - Storage, Search, Cosmos, etc
- Leverage read-only keys for the students
- Share the read-only keys in Teams, and rotate them as necessary
- Share keys in the form of a ".env" file, easily readable by Python

---

## Series Outline

One 30-minute meeting for each topic listed below.

### The Basics (8 sessions)

- Git and GitHub
  - account creation, installation, git pull, git push, branching, PRs
- Simple CLI program Python
  - pypi, uv, venv, main.py, environment variables
- Simple UI app with Python and Streamlit 
- Classes and Object Oriented Programming (OOP)
- Data Wrangling
  - the data you need is rarely available, it must first be "wrangled"
  - text, csv, json, toon
- Jupyter and Pandas
  - the gateway to Databricks
- Unit Testing
  - quality matters, coverage
- VSC, GitHub Copilot, Cursor
  - learn AI from AI

### Foundational Azure Services (5 sessions)

- Azure Storage - containers and blobs
- Azure Foundry - models
- Azure OpenAI - generate completions and embeddings
- Azure CosmosDB - NoSQL, SQL queries, and semantic/vector search
- Azure Search - fluent and semantic/vector search

### AI (6 sessions)

- PDF to Markdown with Azure Document Intelligence
  - Chunking of the Markdown
  - Vectorization of the chunks
- RAG and Vector Search 
- Knowledge Graphs
  - a better RAG
  - LPG: vertices and edges
  - RDF: triples, ontologies, sparql
  - implement a simple localhost graph with rdflib
  - reference CosmosAIGraph and OmniRAG (former MSFT project)
  - reference AIGraph4PG (former MSFT project)
- MCP
  - Cursor as client for local MCP server 
- Azure Agent Framework
  - the future SDK for Microsoft AI
- A complete AI App
  - using most of the topics previously discussed in the series

---

## Certification (Internal)

- After review of a student created app
- Or attendance of n-number of sessions in the series

## Other Potential Topics

- Azure Functions
- Databricks (with a guest speaker)
- Docker and Containers
- "Deep-Dive" future series?

## Out of Scope

- Low-code tools
- Azure PaaS Service Deployment by students

## Reference Repos

The repo for zero-to-AI will be similar to the following:

- https://github.com/cjoakim/AIGraph4pg
  - mkdocs at https://cjoakim.github.io/AIGraph4pg/
- https://github.com/AzureCosmosDB/CosmosAIGraph
