# Part 2, Session 12 - Azure CosmosDB

<br><br>

## NoSQL Databases - Cosmos DB, MongoDB, Document DB

- They don't use **Relational Database Technology** (i.e. - tables, rows, columns)
  - "NoRelational" would have been a better name
- They store JSON content
- They are schemaless
- They enable high-Performance applications
- They can be distributed across many compute and storage nodes

<br><br><br>

## Why Cosmos DB?

  - **High-Availability**, five nines (99.999% financially-backed guaranteed uptime!)
  - **Low Latency**, 4-5 milliseconds (ms) for **point read** operations
  - **Scales from very small to extremely large workloads**
  - **Autoscaling** - it adds more storage as needed
  - Regional and availability-zone replication
  - Easy to use SQL syntax for queries
    - Yes, this "NoSQL" database uses **SQL** as the query language!
  - Priced and scaled by the **Request Unit (RU)**
  - **Microsoft Teams, Toyota, and Azure OpenAI use Cosmos** - huge workloads
  - **No Locking**, Optimitistic Concurrency Control (OCC) instead 
    - See the generated _etag attribute in each document
  - **Azure Integrations**
    - Azure Functions via the **Change Feed** stream of events from Cosmos DB
    - Azure Search (future session)
    - Microsoft Fabric
  - Vector Search(https://docs.azure.cn/en-us/cosmos-db/nosql/vector-search)
  - **Vector search** uses the fast and cost-effective [DiskANN](https://devblogs.microsoft.com/cosmosdb/microsoft-diskann-in-azure-cosmos-db-whitepaper/) algorithm
  - Enables rapid development and application evolution because of the **schemaless** nature of the database
  - It's a **Hero Database** at Microsoft - lots of investment in it
  - My recommendation: Consider Cosmos DB for your next project

Note: There are several **variants**, or **APIs** of Cosmos DB. 
The primary one is the **NoSQL API**, which is what we'll be using in this series.

<br><br><br>

## Concepts 

- Cosmos DB **Account** 
  - This session is about the **Cosmos DB NoSQL API**, or version of the database
- Cosmos DB **Database**
  - zero to many databases per account
- Cosmos DB **Container**
  - zero to many containers per database
  - A container is similar to a relational database table 
  - **But, it's schemaless** - you can store any JSON content in a container
  - As long as the partition key attribute is in the JSON content
- Cosmos DB **Item**
  - A JSON document in a container

<br><br><br>

## Partitioning - How it Works

  - Logical Partitioning with the **Partition Key** attribute
    - You, the customer, specify the Partition Key attribute
  - Physical Partitioning
    - Cosmos DB determines where to store the data based on the Partition Key

<p align="center">
   <img src="img/cosmosdb-partitioning.png" width="60%">
</p>

<br><br><br>

## Cosmos DB SDK for Python

 -[Documentation](https://learn.microsoft.com/en-us/azure/cosmos-db/sdk-python)
 -[azure-cosmos @ PyPI](https://pypi.org/project/azure-cosmos/)
- See class **CosmosNoSqlUtil** in file src/db/cosmos_nosql_util.py

<br><br><br>

## Demonstration: Vector Search with Cosmos DB

This uses a **vectorized** dataset in directory **python/data/cosmosdb/**
that has been previously loaded into the **libraries** container in the **dev** database. 

Vector search, or **semantic search**, is widely used by AI applications.
It's a key component of the RAG (Retrieval-Augmented Generation) pattern.

**Note: I've already populated the Cosmos DB database with the necessary containers and data.**

**NOTE: PLEASE DO NOT DELETE OR MODIFY THE DATA IN THIS COSMOS DB ACCOUNT.**

### These are the implemented command-line functions:

```
$ python main-cosmos-nosql.py

Usage:
  Example use of the Cosmos NoSQL API.
  python main-cosmos-nosql.py list_databases
  python main-cosmos-nosql.py create_database dev 0
  python main-cosmos-nosql.py create_container dev test /pk 1000 default_idx
  python main-cosmos-nosql.py create_container dev airports /pk 5000 default_idx
  python main-cosmos-nosql.py create_container dev libraries /pk 10000 cosmos/libraries_index.json
  python main-cosmos-nosql.py delete_database test
  python main-cosmos-nosql.py delete_container dev libraries
  python main-cosmos-nosql.py list_containers dev
  python main-cosmos-nosql.py load_python_libraries dev libraries
  python main-cosmos-nosql.py test_cosmos_nosql dbname, db_ru, cname, c_ru, pkpath
  python main-cosmos-nosql.py test_cosmos_nosql dev 0 test /pk 1000
  python main-cosmos-nosql.py vector_search_similar_libs dev libraries fastapi
  python main-cosmos-nosql.py vector_search_similar_words dev libraries async web framework with pydantic and swagger
```

### Vector Search - Similar Libraries

See https://docs.azure.cn/en-us/cosmos-db/vector-search

Read the **fastapi** document, get its embedding, then execute a vector search
using that embedding to find similar libraries.

```
$ python main-cosmos-nosql.py vector_search_similar_libs dev libraries fastapi
```

#### Sample Document in Cosmos DB 

```
{
    "id": "fa9e6d98-b848-46dc-bf25-8816adddd1f3",
    "pk": "pypi",
    "name": "azure-identity",
    "author": "None",
    "author_email": "Microsoft Corporation <azpysdkhelp@microsoft.com> License-Expression: MIT",
    "classifiers": [
        "Development Status :: 5 - Production/Stable"
    ],
    "description": "# Azure Identity client library for Python\n\nThe Azure Identity library provides [Microsoft Entra ID](https://learn.microsoft.com/entra/fundamentals/whatis) token-based authentication support across the Azure SDK. It provides a set of [`TokenCredential`][token_cred_ref]/[`SupportsTokenInfo`][supports_token_info_ref] implementations, which can be used to construct Azure SDK clients that support Microsoft Entra token authentication.\n\n[Source code](https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/identity/azure-identity)\n| [Package (PyPI)](https://pypi.org/project/azure-identity/)\n| [Package (Conda)](https://anaconda.org/microsoft/azure-identity/)\n| [API reference documentation][ref_docs]\n| [Microsoft Entra ID documentation](https://learn.microsoft.com/entra/identity/)\n\n## Getting started\n\n### Install the package\n\nInstall Azure Identity with pip:\n\n```sh\npip install azure-identity\n```\n\n### Prerequisites\n\n- An [Azure subscription](https://azure.microsoft.com/free/python)\n- Python ",
    "docs_url": "None",
    "downloads": "{'last_day': -1, 'last_month': -1, 'last_week': -1}",
    "home_page": "None",
    "keywords": "azure, azure sdk",
    "maintainer": "None",
    "maintainer_email": "None",
    "requires_python": ">=3.9",
    "summary": "Microsoft Azure Identity Library for Python",
    "version": "1.25.1",
    "release_count": 80,
    "embedding": [
        0.000010099463906954043,
        0.003638420021161437,
        0.012143994681537151,
        -0.025844387710094452,
        -0.012867582961916924,
        
        ...

        0.02445182204246521,
        -0.005286972504109144,
        -0.014963258057832718,
        -0.0027492940425872803,
        -0.04906747490167618
    ],
    "_rid": "fxkUANp6gFYsAAAAAAAAAA==",
    "_self": "dbs/fxkUAA==/colls/fxkUANp6gFY=/docs/fxkUANp6gFYsAAAAAAAAAA==/",
    "_etag": "\"810074e7-0000-0100-0000-69a8b4920000\"",
    "_attachments": "attachments/",
    "_ts": 1772663954
}
```

### Vector Search - Similar Words

Use the given words on the command line to generate an embedding,
then execute a vector search using that embedding to find similar libraries.

```
$ python main-cosmos-nosql.py vector_search_similar_words dev libraries async web framework with pydantic and swagger
```

<br><br><br>

## Homework 

- Execute the above vector search 
- Execute the above vector search with a different set of words
  - See the python/data/cosmosdb/ directory and find a library of interest to search for
- See class CosmosNoSqlUtil in file python/src/db/cosmos_nosql_util.py
  - Understand how it works (Cursor may be helpful to you here)
- Understand what a "partition key attribute" is in Cosmos DB
- See file python/cosmos/libraries_index.json 
  - This is the index policy for the libraries container
  - Understand what diskANN is
  - See https://docs.azure.cn/en-us/cosmos-db/vector-search


<br><br><br>

## Pro Tip - Let me advise you

- I was previously a **Cosmos DB Global Black Belt (GBB) at Microsoft**
- I can help you use it properly, and avoid common errors

<br><br><br>
---
<br><br><br>

[Home](../README.md)
