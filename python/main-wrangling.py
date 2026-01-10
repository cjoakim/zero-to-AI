"""
Usage:
    Data wrangling with DuckDB with local and remote files.
    python main-wrangling.py <func>
    python main-wrangling.py postal_codes_nc
    python main-wrangling.py imdb
    python main-wrangling.py openflights
    python main-wrangling.py augment_openflights_airports
Options:
  -h --help     Show this screen.
  --version     Show version.
"""

import json
import sys
import os
import time
import traceback
from typing import Any

import duckdb

from docopt import docopt
from dotenv import load_dotenv

from geopy.geocoders import Nominatim

from src.io.fs import FS
from src.os.env import Env


def print_options():
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


def postal_codes_nc():
    """
    Read a local CSV file with DuckDB.
    Then query it with SQL.
    Then transform the CSV data into a JSON file.
    """
    infile = "data/postal_codes/postal_codes_nc.csv"
    rel = duckdb.read_csv(infile)
    rel.show()
    print(rel.shape)  # (1080, 7)
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


def imdb():
    data = duckdb.read_csv("https://datasets.imdbws.com/name.basics.tsv.gz")
    data.show()
    print(data.shape)  # (15003543, 6) <-- 15-million+ rows!

    # See https://developer.imdb.com/non-commercial-datasets/
    # name.basics.tsv.gz
    # title.akas.tsv.gz
    # title.basics.tsv.gz
    # title.crew.tsv.gz
    # title.episode.tsv.gz
    # title.principals.tsv.gz
    # title.ratings.tsv.gz


def openflights():
    """
    Read the OpenFlights dataset from a remote URL with DuckDB,
    parse each, and save each to a JSON file.
    See https://openflights.org/data.html
    """
    dataset_names = openflights_dataset_names()
    for idx, dataset_name in enumerate(dataset_names):
        if idx < 5:
            rel = read_remote_openflights_csv(dataset_name)
            rel.show(max_width=100)
            print(rel.shape)
            print(rel.df().columns.tolist())
            save_openflights_relation_to_json(rel, dataset_name)


def openflights_dataset_names():
    """
    Return the names of the OpenFlights datasets that are of interest to us.
    These are used in the openflights_url() method to form the URLs for each dataset.
    See https://openflights.org/data.html
    """
    return [
        "airports",
        "airlines",
        "routes",
        "planes",
        "countries",
    ]


def openflights_url(dataset_name: str):
    return f"https://raw.githubusercontent.com/jpatokal/openflights/master/data/{dataset_name}.dat"


def read_remote_openflights_csv(dataset_name: str):
    """
    Read a remote OpenFlights CSV file into a DuckDB relation.
    The remote CSV files do NOT have headers, so we need to specify the columns.
    See https://openflights.org/data.html
    """
    url = openflights_url(dataset_name)
    columns = openflights_colnames(dataset_name)
    return duckdb.read_csv(
        url,
        header=False,
        delimiter=",",
        columns=columns,
        strict_mode=False,
        ignore_errors=True,
        encoding="utf-8",
    )


def openflights_colnames(dataset_name: str):
    """
    Return the column names for each OpenFlights dataset since the remote CSV files do NOT have headers.
    See https://openflights.org/data.html
    """
    if dataset_name == "airports":
        return {
            "airport_id": "string",
            "name": "string",
            "city": "string",
            "country": "string",
            "iata_code": "string",
            "icao_code": "string",
            "latitude": "string",
            "longitude": "string",
            "altitude": "string",
            "timezone_code": "string",
            "dst": "string",
            "tz_database_time_zone": "string",
            "type": "string",
            "source": "string",
        }
    elif dataset_name == "airlines":
        return {
            "airline_id": "string",
            "name": "string",
            "alias": "string",
            "iata_code": "string",
            "icao_code": "string",
            "callsign": "string",
            "country": "string",
            "active": "string",
        }
    elif dataset_name == "routes":
        return {
            "airline_iata": "string",
            "airline_id": "string",
            "from_airport_iata": "string",
            "from_airport_id": "string",
            "to_airport_iata": "string",
            "to_airport_id": "string",
            "codeshare": "string",
            "stops": "string",
            "equipment": "string",
        }
    elif dataset_name == "planes":
        # "Airbus A319neo","31N","A19N"
        return {
            "name": "string",
            "iata_code": "string",
            "icao_code": "string",
        }
    elif dataset_name == "countries":
        return {
            "name": "string",
            "iso_code": "string",
            "dafif_code": "string",
        }
    else:
        return {}


def save_openflights_relation_to_json(rel, dataset_name: str):
    """
    Write the given DuckDB relation to a JSON file with one object-per-line.
    Then read it back and transform it into one big JSON object instead of object-per-line.
    """
    outfile1 = f"tmp/openflights_{dataset_name}_lines.json"
    rel.df().to_json(outfile1, orient="records", lines=True)
    print(f"file written: {outfile1}")

    outfile2 = f"tmp/openflights_{dataset_name}.json"
    lines = FS.read_lines(outfile1)
    objects = list()
    for line in lines:
        objects.append(json.loads(line))
    FS.write_json(objects, outfile2)


def augment_openflights_airports():
    """
    Augment each airport object with an address and and emptyembedding.
    The address is geocoded using the latitude and longitude with the geopy library.
    Bypass the airports with invalid IATA codes.
    This method reads and writes the same file multiple times, due to geopy rate limiting,
    to ensure that all airports are augmented correctly.
    """
    infile = "tmp/openflights_airports.json"
    objects = FS.read_json(infile)
    airport_count = len(objects)
    print(f"{airport_count} airports read from file {infile}")
    user_agent = "zero-to-AI-{}".format(int(time.time()))
    geolocator = Nominatim(user_agent=user_agent)
    time.sleep(10)
    exception_count, with_address_count, bypassed_count = 0, 0, 0

    for idx, obj in enumerate(objects):
        seq = idx + 1
        try:
            obj["embedding"] = list[float]()
            if exception_count < 100:
                iata_code = str(obj["iata_code"]).strip()
                if is_valid_iata_code(iata_code):
                    if "address" in obj.keys():
                        with_address_count += 1
                        print(f"{seq}/{airport_count}: {iata_code} already has an address")
                    else:
                        time.sleep(1.2)
                        latitude = float(obj["latitude"])
                        longitude = float(obj["longitude"])
                        location = geolocator.reverse(
                            (latitude, longitude), language="en", exactly_one=True
                        )
                        address = location.address
                        obj["address"] = address
                        print(f"{seq}/{airport_count}: {iata_code} --> {address}")
                        objects[idx] = obj
                else:
                    bypassed_count += 1
                    obj["address"] = "bypassed"
                    objects[idx] = obj
        except Exception as e:
            exception_count += 1
            print(f"Exception: {exception_count}: {e} on obj: {obj}")
            print(traceback.format_exc())

    print(f"with_address_count: {with_address_count}")
    print(f"bypassed_count:     {bypassed_count}")
    print(f"objects_count:      {len(objects)}")
    print(f"exception_count:    {exception_count}")
    FS.write_json(objects, infile)
    print(f"file written: {infile}")


def is_valid_iata_code(iata_code: str) -> bool:
    result: bool = True
    if len(iata_code) == 3:
        if "/" in iata_code:  # n/a, N/A
            result = False
        elif "\\" in iata_code:  # \N
            result = False
    else:
        result = False
    print(f"is_valid_iata_code: {iata_code} -> {result}")
    return result


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print_options("Error: no CLI args provided")
        else:
            func = sys.argv[1].lower()
            if func == "postal_codes_nc":
                postal_codes_nc()
            elif func == "imdb":
                imdb()
            elif func == "openflights":
                openflights()
            elif func == "augment_openflights_airports":
                augment_openflights_airports()
            else:
                print_options()
    except Exception as e:
        print(str(e))
        print(traceback.format_exc())
