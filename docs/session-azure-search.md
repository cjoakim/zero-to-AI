# Part 2, Session 13 - Azure Search

<br><br>

## What is Retrieval-Augmented Generation (RAG)?

### Microsoft Definition 

See https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-retrieval-augmented-generation-rag

> Retrieval-augmented generation is an AI framework that involves the retrieval
> of relevant information from external sources to inform and enhance the 
> generation of responses.  This dual capability allows RAG systems to produce 
> more informed and nuanced outputs than purely generative models.

### Comments 

- **Retrieval** means that you fetch relevant information to pass to the LLM 
  - So as to produce a more relevant response 
  - You pass the RAG data to the LLM via the prompt 
  - The RAG data is typically often retrieved from the following sources:
    - A Search Service such as **Azure Search** (aka: Lexical Search)
    - A Vector Search (aka: Semantic Search)
    - A Graph Database (aka: Graph RAG)
    - A Relational Database (aka: DB RAG)
    - And more...
- **Augmented** means that you augment the knowledge of the LLM 
  - The LLM is trained on **public data**, not your **private data**
- **Generation**
  - The LLM is generating a **completion** or **response** to a prompt

**RAG is widely used in AI applications** - it's a **fundamental pattern** in AI.

<br><br><br>
---
<br><br><br>

## Azure Search 

### Microsoft Description

> Azure AI Search (formerly Azure Cognitive Search) is a cloud-based, AI-powered
> information retrieval platform for building intelligent, high-performance 
> search experiences and Generative AI applications. It enables hybrid (vector + text), 
> semantic, and full-text searches over structured/unstructured data using AI 
> to index and analyze content, supporting RAG (Retrieval-Augmented Generation) architectures.

### Links

- https://azure.microsoft.com/en-us/products/ai-services/ai-search/
- https://learn.microsoft.com/en-us/azure/search/

### Comments

- PaaS service - Platform as a Service 
- Is widely used in AI applications
- It has a very **nice HTTP REST API** for configuring and searching.  Easy to use.
  - [REST (Representational State Transfer)](https://en.wikipedia.org/wiki/REST)
  - It's simply a standard set of conventions for interacting with a HTTP web service

### Key Concepts 

- **Index**
  - A collection of documents that are indexed for search
- **Document**
  - A unit of content that is indexed for search
  - The documents are in JSON format (just like Cosmos DB)
- **Field**
  - A named attribute of a document
- **DataSource**
  - An optional external data source that provides data to an index
  - Alternatively, you can directly add documents to the index
- **Indexer**
  - Takes a configured DataSource and populates an index 
  - On a given schedule or on demand 
- **AI Enrichments**
  - See https://learn.microsoft.com/en-us/azure/search/cognitive-search-concept-intro
  - "Enrich" the content with Azure Cognitive Services **skills**
- **Relevance**
  - Provides a score for each document returned from a query
- **Search Syntax**
  - Simple Syntax 
  - Or [Lucene Syntax](https://learn.microsoft.com/en-us/azure/search/query-lucene-syntax)
    - [Apache Lucene](https://lucene.apache.org/) is a popular open source search engine
- **Synonyms**
  - https://learn.microsoft.com/en-us/azure/search/search-synonyms
  - Example: USA, United States, United States of America
  - Example: MILO, Machine Intelligence Learning and Orchestrator

**There is a lot more functionality to Azure Search, this is just an introduction.**

<br><br><br>
---
<br><br><br>

### Demonstration

- Create a Cosmos DB **DataSource** 
- Create a search **Index**
- Create an **Indexer** to read the DataSource and populate the Index

### Setup Scripts and Configuration Files

- aisearch-setup.ps1 and aisearch-setup.sh in the python directory 
- See the **python/aisearch** directory for the configuration files


#### DataSource Configuration File

This defines a Cosmos DB **DataSource** for the **libraries** container.

```
{
  "name": "cosmosdb-nosql-libraries",
  "description": null,
  "type": "cosmosdb",
  "subtype": null,
  "credentials": {
    "connectionString": "... populate me ..."
  },
  "container": {
    "name": "libraries",
    "query": null
  },
  "dataChangeDetectionPolicy": {
    "@odata.type": "#Microsoft.Azure.Search.HighWaterMarkChangeDetectionPolicy",
    "highWaterMarkColumnName": "_ts"
  },
  "dataDeletionDetectionPolicy": null,
  "encryptionKey": null
}
```

#### Index Configuration File

We define each field of the JSON document that we want to expose.

Note how this enables vector search on the **embedding** field/attribute.
It creates a [Hierarchical Navigable Small World (HNSW)](https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world)
algorithm vector index hnsw.  This is an Approximate Nearest Neighbors (ANN) algorithm.

See https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-create-index

```
{
  "name": "nosql-libraries",
  "fields": [
    {
      "name": "id",
      "key": "true",
      "type": "Edm.String",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "pk",
      "type": "Edm.String",
      "key": "false",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "name",
      "type": "Edm.String",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "author",
      "type": "Edm.String",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "author_email",
      "type": "Edm.String",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "keywords",
      "type": "Edm.String",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "description",
      "type": "Edm.String",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "summary",
      "type": "Edm.String",
      "searchable": "true",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "release_count",
      "type": "Edm.Int32",
      "searchable": "false",
      "filterable": "true",
      "sortable": "true",
      "facetable": "true"
    },
    {
      "name": "embedding",
      "type": "Collection(Edm.Single)",
      "searchable": true,
      "retrievable": false,
      "stored": false,
      "dimensions": 1536,
      "vectorSearchProfile": "vector-profile-hnsw-scalar"
    }
  ],
  "vectorSearch": {
    "compressions": [
      {
        "name": "scalar-quantization",
        "kind": "scalarQuantization",
        "scalarQuantizationParameters": {
          "quantizedDataType": "int8"
        },
        "rescoringOptions": {
          "enableRescoring": true,
          "defaultOversampling": 10,
          "rescoreStorageMethod": "preserveOriginals"
        }
      },
      {
        "name": "binary-quantization",
        "kind": "binaryQuantization",
        "rescoringOptions": {
          "enableRescoring": true,
          "defaultOversampling": 10,
          "rescoreStorageMethod": "discardOriginals"
        }
      }
    ],
    "algorithms": [
      {
        "name": "hnsw-1",
        "kind": "hnsw",
        "hnswParameters": {
          "m": 4,
          "efConstruction": 400,
          "efSearch": 500,
          "metric": "cosine"
        }
      },
      {
        "name": "hnsw-2",
        "kind": "hnsw",
        "hnswParameters": {
          "m": 8,
          "efConstruction": 800,
          "efSearch": 800,
          "metric": "hamming"
        }
      },
      {
        "name": "eknn",
        "kind": "exhaustiveKnn",
        "exhaustiveKnnParameters": {
          "metric": "euclidean"
        }
      }
    ],
    "profiles": [
      {
        "name": "vector-profile-hnsw-scalar",
        "compression": "scalar-quantization",
        "algorithm": "hnsw-1"
      }
    ]
  }
}
```

#### Indexer Configuration File

Notice how this JSON weaves together the above **dataSourceName** and **targetIndexName**.

```
{
  "name": "nosql-libraries",
  "dataSourceName": "cosmosdb-nosql-dev-libraries",
  "targetIndexName": "nosql-libraries",
  "schedule": {
    "interval": "PT12H"
  }
}
```

#### Search Setup 

```
.\aisearch-setup.ps1
- or -
./aisearch-setup.sh
```

#### Execute Searches

See file **aisearch/libraries_searches.json** for the search parameters 
used in these named queries (i.e. - m26 and vector_search_fastapi_vector).

```
python main-search.py search_index nosql-libraries m26 aisearch/libraries_searches.json

Index name:  nosql-libraries
Search name: m26
Search params:
{
  "count": true,
  "search": "m26",
  "orderby": "pk"
}
2026-03-10 17:09:13,692 - HTTP Request: POST https://cj3csearchfree.search.windows.net/indexes/nosql-libraries/docs/search?api-version=2025-09-01 "HTTP/1.1 200 OK"
response.status_code: 200
{
  "url": "https://cj3csearchfree.search.windows.net/indexes/nosql-libraries/docs/search?api-version=2025-09-01",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "api-key": "HyfrxMrAjvgcgkehoBdYTa6BJm5z5FsVl3XIWw3ZvlAzSeDzaSC1"
  },
  "status_code": 200,
  "content": {
    "@odata.context": "https://cj3csearchfree.search.windows.net/indexes('nosql-libraries')/$metadata#docs(*)",
    "@odata.count": 1,
    "value": [
      {
        "@search.score": 19.821657,
        "id": "e652c76e-58bf-4a7d-841f-d0515a315085",
        "pk": "pypi",
        "name": "m26",
        "author": "None",
        "author_email": "Chris Joakim <christopher.joakim@gmail.com>",
        "keywords": "calculator, cycling, pace per mile, running, swimming",
        "description": "# m26\n\nm26 - calculations for sports like running, cycling, and swimming\n\n## Urls\n\n- GitHub: https://github.com/cjoakim/m26-py\n- PyPi: https://pypi.org/project/m26/\n\n## Features\n\n- Create Distances in either miles, kilometers, or yards.\n- Translates Distances to the other units of measure.\n- Specify ElapsedTime either in 'hh:mm:ss' strings, or int second values.\n- Calculates Speed from a given Distance and ElapsedTime - per mile, per kilometer, and per yard.\n- Calculates pace_per_mile and seconds_per_mile for a given Speed.\n- Projects one Speed to another Distance with either a simple or algorithmic formula.\n- RunWalkCalculator calculates pace and mph from given time intervals and paces.\n- Calculates the Age of person, and age_graded times.\n- Calculates five standard heart-rate training zones based on Age.\n\n\n## Quick start\n\n\n### Installation\n\n```\n$ pip install m26\n```\n\n### Use\n\n\n#### Sample Program\n\nSee sample-program.py in the GitHub repo.\n\n```\nimport json\n\nimport m26\n\nif __name__ == ",
        "summary": "m26 - calculations for sports like running, cycling, and swimming",
        "release_count": 6
      }
    ]
  }
}
```

```
python main-search.py search_index nosql-libraries vector_search_fastapi_vector aisearch/libraries_searches.json

Index name:  nosql-libraries
Search name: vector_search_fastapi_vector
Search params:
{
  "count": true,
  "queryType": "simple",
  "top": 10,
  "vectorQueries": [
    {
      "kind": "vector",
      "vector": [
        -0.00417686440050602,
        0.0037260728422552347,
        -0.00249696196988225,
        
        ...

        0.009368008933961391,
        -0.015749525278806686,
        -0.003849336178973317,
        -0.04767119511961937
      ],
      "fields": "embedding",
      "k": 5,
      "exhaustive": false
    }
  ],
  "vectorFilterMode": "preFilter"
}

response.status_code: 200

{
  "url": "https://cj3csearchfree.search.windows.net/indexes/nosql-libraries/docs/search?api-version=2025-09-01",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "api-key": "...redacted..."
  },
  "status_code": 200,
  "content": {
    "@odata.context": "https://cj3csearchfree.search.windows.net/indexes('nosql-libraries')/$metadata#docs(*)",
    "@odata.count": 5,
    "value": [
      {
        "@search.score": 0.01666666753590107,
        "id": "a0568939-1f6a-4482-a90d-54b906903cfc",
        "pk": "pypi",
        "name": "fastapi",
        "author": "None",
        "author_email": "=?utf-8?q?Sebasti=C3=A1n_Ram=C3=ADrez?= <tiangolo@gmail.com>",
        "keywords": "None",
        "description": "<p align=\"center\">\n  <a href=\"https://fastapi.tiangolo.com\"><img src=\"https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png\" alt=\"FastAPI\"></a>\n</p>\n<p align=\"center\">\n    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>\n</p>\n<p align=\"center\">\n<a href=\"https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster\" target=\"_blank\">\n    <img src=\"https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master\" alt=\"Test\">\n</a>\n<a href=\"https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi\" target=\"_blank\">\n    <img src=\"https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg\" alt=\"Coverage\">\n</a>\n<a href=\"https://pypi.org/project/fastapi\" target=\"_blank\">\n    <img src=\"https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package\" alt=\"Package version\">\n</a>\n<a href=\"https://pypi.org/project/fastapi\" target=\"_blank\">\n    <img sr",
        "summary": "FastAPI framework, high performance, easy to learn, fast to code, ready for production",
        "release_count": 266
      },
      {
        "@search.score": 0.016393441706895828,
        "id": "0650fb70-6b5d-48c4-bab0-ca00931876e9",
        "pk": "pypi",
        "name": "fastapi-cli",
        "author": "None",
        "author_email": "=?utf-8?q?Sebasti=C3=A1n_Ram=C3=ADrez?= <tiangolo@gmail.com>",
        "keywords": "None",
        "description": "# FastAPI CLI\n\n<a href=\"https://github.com/fastapi/fastapi-cli/actions/workflows/test.yml\" target=\"_blank\">\n    <img src=\"https://github.com/fastapi/fastapi-cli/actions/workflows/test.yml/badge.svg\" alt=\"Test\">\n</a>\n<a href=\"https://github.com/fastapi/fastapi-cli/actions/workflows/publish.yml\" target=\"_blank\">\n    <img src=\"https://github.com/fastapi/fastapi-cli/actions/workflows/publish.yml/badge.svg\" alt=\"Publish\">\n</a>\n<a href=\"https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi-cli\" target=\"_blank\">\n    <img src=\"https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi-cli.svg\" alt=\"Coverage\">\n<a href=\"https://pypi.org/project/fastapi-cli\" target=\"_blank\">\n    <img src=\"https://img.shields.io/pypi/v/fastapi-cli?color=%2334D058&label=pypi%20package\" alt=\"Package version\">\n</a>\n\n---\n\n**Source Code**: <a href=\"https://github.com/fastapi/fastapi-cli\" target=\"_blank\">https://github.com/fastapi/fastapi-cli</a>\n\n---\n\nRun and manage FastAPI apps from the command",
        "summary": "Run and manage FastAPI apps from the command line with FastAPI CLI. \ud83d\ude80",
        "release_count": 20
      },
      {
        "@search.score": 0.016129031777381897,
        "id": "0479252c-db56-4492-8e51-7b499d9c7898",
        "pk": "pypi",
        "name": "typer",
        "author": "None",
        "author_email": "Sebasti\u00e1n Ram\u00edrez <tiangolo@gmail.com>",
        "keywords": "None",
        "description": "<p align=\"center\">\n  <a href=\"https://typer.tiangolo.com\"><img src=\"https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg#only-light\" alt=\"Typer\"></a>\n\n</p>\n<p align=\"center\">\n    <em>Typer, build great CLIs. Easy to code. Based on Python type hints.</em>\n</p>\n<p align=\"center\">\n<a href=\"https://github.com/fastapi/typer/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster\" target=\"_blank\">\n    <img src=\"https://github.com/fastapi/typer/actions/workflows/test.yml/badge.svg?event=push&branch=master\" alt=\"Test\">\n</a>\n<a href=\"https://github.com/fastapi/typer/actions?query=workflow%3APublish\" target=\"_blank\">\n    <img src=\"https://github.com/fastapi/typer/workflows/Publish/badge.svg\" alt=\"Publish\">\n</a>\n<a href=\"https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/typer\" target=\"_blank\">\n    <img src=\"https://coverage-badge.samuelcolvin.workers.dev/fastapi/typer.svg\" alt=\"Coverage\">\n<a href=\"https://pypi.org/project/typer\" target=\"_blank\">\n    <img src=\"https:",
        "summary": "Typer, build great CLIs. Easy to code. Based on Python type hints.",
        "release_count": 68
      },
      ... more results ...
```

<br><br><br>
---
<br><br><br>

### Homework 

- Read The Links Above - RAG, Azure Search
- Execute The Above Searches 
- Create a new search definition in  **aisearch/libraries_searches.json** and execute it

<br><br><br>
---
<br><br><br>

[Home](../README.md)
