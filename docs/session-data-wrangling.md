# Part 1, Session 5 - Data Wrangling


This is what a real-world AI application looks like:

<p align="center">
   <img src="img/iceberg.jpeg" width="40%">
</p>

### Below the waterline

- That's the **Data - lots and lots of data**
- In multiple **Formats**
- From multiple **Sources**
- Sometimes it's not pretty
- The data you need is rarely available **as-is**, it usually must first be **wrangled** into a usable format.

### Above the waterline

- The **data wrangling code** that transforms the data into a usable format
- The standard/traditional **application code** that uses the data

### The Tip of the Iceberg

- That's the AI part - models, prompts, LLMs, MCP, Agent Framework, algorithms, etc.

### So, what is Data Wrangling?

- It's the art of transforming messy raw data into a usable formats for your needs
- [Data Wrangling at Wikipedia](https://en.wikipedia.org/wiki/Data_wrangling)

<br><br><br>

## Common File Formats

- Text 
- CSV = Comma Separated Values
- TSV = Tab Separated Values
- JSON = JavaScript Object Notation.  Widely used, flexible-schema
- Markdown - a simple text format to produce formatted HTML.  Liked by LLMs.
- **TOON** = Newer, compact, efficient format for LLMs and AI applications

<br><br><br>

## Common Data Wrangling Use-Cases

- Merging multiple data sources into a single file
- Create CSV content to load into a relational Database
  - Such as Azure PostgreSQL
  - Or a Spark dataframe (dataframe in the next lesson w/Jupyter)
- Create **JSON** content to load into **Azure Cosmos DB or Azure Search**
- Collect descriptive text content for creating **embeddings** for a **Vector Database** (i.e. - Semantic Search)
  - Embeddings and vector search will be covered in a later session

<br><br><br>

## Python is a great programming language for data Wrangling

  - Many useful standard and third-party libraries for this
  - json and csv standard libraries.  And many more
  - [pandas](https://pandas.pydata.org) for CSV/TSV data (covered in the next lesson w/Jupyter)
  - [duckdb](https://duckdb.org) for remote files in various formats, then read with SQL
  - [beautifulsoup](https://beautiful-soup-4.readthedocs.io/en/latest/) for parsing HTML
  - [openpyxl](https://openpyxl.readthedocs.io/en/stable/) for Excel files
  - PDF will be covered at a later session, using Azure Document Intelligence

We'll use the **duckdb** library in this session.  It's **NOT a database**.
Rather, it's a **library** that allows you to fetch data and query it with SQL.

<br><br><br>

## Excellent Public Data Sources

These are listed here for your exploration.

  - [Kaggle](https://www.kaggle.com/datasets)
  - [Hugging Face](https://huggingface.co/docs/datasets/en/index)
  - [Open Flights](https://openflights.org/data) - airports, airlines, routes
  - [IMDb](https://developer.imdb.com/non-commercial-datasets/) - movies
  - many, many, many more...

<br><br><br>

## Demonstration

This session uses file **main-wrangling.py**.

```
python main-wrangling.py help

Usage:
    Data wrangling with DuckDB with local and remote files.
    python main-wrangling.py <func>
    python main-wrangling.py postal_codes_nc
    python main-wrangling.py imdb
    python main-wrangling.py openflights
    python main-wrangling.py augment_openflights_airports
```

### Wrangling North Carolina Postal Codes

The input data, file **data/postal_codes/postal_codes_nc.csv**.

It is fairly clean data, and it has a useful header row that describes the columns.

```
id,postal_cd,country_cd,city_name,state_abbrv,latitude,longitude
10949,27006,US,Advance,NC,35.9445620000,-80.4376310000
10950,27007,US,Ararat,NC,36.3768840000,-80.5962650000
10951,27009,US,Belews Creek,NC,36.2239300000,-80.0800180000
10952,27010,US,Bethania,NC,36.1822000000,-80.3384000000
10953,27011,US,Boonville,NC,36.2091840000,-80.6937720000
10954,27012,US,Clemmons,NC,36.0040180000,-80.3714450000
10955,27013,US,Cleveland,NC,35.7634680000,-80.7037300000
10956,27014,US,Cooleemee,NC,35.8119670000,-80.5542580000
10957,27016,US,Danbury,NC,36.4445880000,-80.2165700000
...
```

The Python code to process this data:

```
def postal_codes_nc():
    """
    Read a local CSV file with DuckDB.
    Then query it with SQL.
    Then transform the CSV data into a JSON file.
    """
    infile = "data/postal_codes/postal_codes_nc.csv"
    rel = duckdb.read_csv(infile)
    rel.show()
    print(rel.shape)       # Print the shape of the data (1080, 7) rows and columns
    print(str(type(rel)))  # <class 'duckdb.duckdb.DuckDBPyRelation'>

    # In this SQL, 'rel' refers to the above python variable name!  Clever.
    davidson = duckdb.sql("SELECT postal_cd, city_name FROM rel WHERE postal_cd = 28036")
    davidson.show()
    print(rel.df().columns.tolist())

    # Transform the CSV data into a JSON file.
    # DuckDB has some dataframe methods - df().
    outfile = "tmp/postal_codes_nc.json"
    rel.df().to_json(outfile, orient="records", lines=True)
    print(f"file written: {outfile}")
```

<br><br><br>

### Wrangling IMDb Data

Very large TSV file dataset with Movies, Ratings,Actors, Directors, etc.

- See https://developer.imdb.com/non-commercial-datasets/
- name.basics.tsv.gz
- title.akas.tsv.gz
- title.basics.tsv.gz
- title.crew.tsv.gz
- title.episode.tsv.gz
- title.principals.tsv.gz
- title.ratings.tsv.gz

This is all the code we need to read the names g-zipped dataset.
This is also a clean dataset with a useful header row.

```
def imdb():
    data = duckdb.read_csv("https://datasets.imdbws.com/name.basics.tsv.gz")
    data.show()
    print(data.shape)  # (14972403, 6) <-- 14-million+ rows!
```

<br><br><br>

### Wrangling the OpenFlights Data 

This public dataset is from the OpenFlights project.
It contains airports, airlines, routes, planes, and countries.
It's not very clean, however, as it has no header rows, some of the columns
are null, and there are multiple character sets.

See the **openflights()** method of **main-wrangling.py**

<br><br><br>

### Augmenting the OpenFlights Data with Address information

This is derived from the latitude and longitude of the airports with the **geopy** library.

See the **augment_openflights_airports()** method of **main-wrangling.py**

<br><br><br>

## Links

 -[duckdb](https://pypi.org/project/duckdb/)
 -[geopy](https://geopy.readthedocs.io/en/stable/)
