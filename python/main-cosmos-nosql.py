"""
Usage:
  Example use of the Cosmos NoSQL API.
  python main-cosmos-nosql.py list_databases
  python main-cosmos-nosql.py create_database dev 0
  python main-cosmos-nosql.py create_container dev test /pk 1000 default_idx
  python main-cosmos-nosql.py create_container dev airports /pk 1000 default_idx
  python main-cosmos-nosql.py create_container dev libraries /pk 10000 cosmos/libraries_index.json
  python main-cosmos-nosql.py delete_database test
  python main-cosmos-nosql.py delete_container dev libraries
  python main-cosmos-nosql.py list_containers dev
  python main-cosmos-nosql.py load_airports dev airports pk --load
  python main-cosmos-nosql.py load_python_libraries dev libraries
  python main-cosmos-nosql.py test_cosmos_nosql dbname, db_ru, cname, c_ru, pkpath
  python main-cosmos-nosql.py test_cosmos_nosql dev 0 test /pk 1000
  python main-cosmos-nosql.py vector_search_similar_libs dev libraries fastapi
  python main-cosmos-nosql.py vector_search_similar_words dev libraries async web framework with pydantic and swagger
"""

# Chris Joakim, 3Cloud/Cognizant, 2026

# Wrangling the Cosmos DB Data:
# 0) run venv.sh 
# 1) python main-wrangling.py gen_pypi_download_lib_json_script 
# 2) ./pypi_download_lib_json.sh  (execute the generated script)
# 3) python main-wrangling.py create_cosmosdb_pypi_lib_documents 
# 4) python main-wrangling.py add_embeddings_to_cosmosdb_documents 


import asyncio
import json
import sys
import time
import logging
import traceback
import uuid

from docopt import docopt
from dotenv import load_dotenv

from faker import Faker

from src.ai.aoai_util import AOAIUtil
from src.io.fs import FS
from src.db.cosmos_nosql_util import CosmosNoSqlUtil
from src.util.data_gen import DataGenerator

fake = Faker()


def print_options(msg):
    print(msg)
    arguments = docopt(__doc__, version="1.0.0")
    print(arguments)


async def list_databases():
    try:
        cosmos = CosmosNoSqlUtil()
        await cosmos.initialize()
        db_list = await cosmos.list_databases()
        for db in db_list:
            print(f"Database: {db}")
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await cosmos.close()


async def create_database(dbname: str, db_ru: int):
    try:
        cosmos = CosmosNoSqlUtil()
        await cosmos.initialize()
        result = await cosmos.create_database(dbname, db_ru)
        print(f"create_database result: {result}")
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await cosmos.close()

async def delete_database(dbname: str):
    try:
        cosmos = CosmosNoSqlUtil()
        await cosmos.initialize()
        result =await cosmos.delete_database(dbname)
        print(f"delete_database result: {result}")
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await cosmos.close()


async def create_container(dbname, cname, pkpath, c_ru, idx_policy_filename=None):
    try:
        cosmos = CosmosNoSqlUtil()
        await cosmos.initialize()
        await cosmos.set_db(dbname)
        await cosmos.create_container(cname, pkpath, c_ru, idx_policy_filename)
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await cosmos.close()

async def delete_container(dbname, cname):
    try:
        cosmos = CosmosNoSqlUtil()
        await cosmos.initialize()
        await cosmos.set_db(dbname)
        await cosmos.delete_container(cname)
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await cosmos.close()

async def list_containers(dbname: str):
    try:
        cosmos = CosmosNoSqlUtil()
        await cosmos.initialize()
        await cosmos.set_db(dbname)
        containers = await cosmos.list_containers()
        for container in containers:
            print(f"Container: {container}")
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await cosmos.close()

async def load_airports(dbname: str, cname: str, pkpath: str):
    try:
        infile = "data/openflights/openflights_airports.json"
        airports = FS.read_json(infile)
        documents = list()
        nosql_util = None
        for rawdoc in airports:
            try:
                newdoc = dict()
                for key in sorted(rawdoc.keys()):
                    value = rawdoc[key]
                    newkey = key.lower()
                    newdoc[newkey] = value
                newdoc["id"] = str(uuid.uuid4())
                newdoc["airport_id"] = int(newdoc["airport_id"])
                newdoc[pkpath] = newdoc["country"]
                newdoc["altitude"] = float(newdoc["altitude"])
                latitude = float(newdoc["latitude"])
                longitude = float(newdoc["longitude"])
                newdoc["latitude"] = latitude
                newdoc["longitude"] = longitude

                # See https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/query/geospatial?tabs=javascript
                # Google: "azure ai search index nested geojson attributes"
                geojson = dict()
                geojson["type"] = "Point"
                geojson["coordinates"] = [longitude, latitude]
                newdoc["location"] = geojson

                if newdoc[pkpath] != "\\N":
                    if newdoc["iata_code"] != "\\N":
                        print(json.dumps(newdoc, sort_keys=False, indent=2))
                        documents.append(newdoc)
            except:
                print("bad json on rawdoc: {}".format(rawdoc))
                logging.info("bad json on rawdoc: {}".format(rawdoc))
                logging.info(traceback.format_exc())
        print(
            "{} documents parsed and filtered from {} raw docs".format(
                len(documents), len(airports)
            )
        )
        opts = dict()
        opts["enable_diagnostics_logging"] = True
        nosql_util = CosmosNoSqlUtil(opts)
        await nosql_util.initialize()

        dbproxy = await nosql_util.set_db(dbname)
        print("dbproxy: {}".format(dbproxy))

        ctrproxy = await nosql_util.set_container(cname)
        print("ctrproxy: {}".format(ctrproxy))

        if "--load" in sys.argv:
            for doc in documents:
                try:
                    cdb_doc = await nosql_util.upsert_item(doc)
                    print("upserted doc: {}".format(json.dumps(cdb_doc, indent=2)))
                    time.sleep(0.05)
                except Exception as e:
                    logging.info("Error upserting doc: {}".format(str(e)))
                    logging.info(traceback.format_exc())
                    time.sleep(1.0)
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    if nosql_util is not None:
        await nosql_util.close()
    print("load_airports completed")

async def load_pypi_libs(dbname: str, cname: str, pkpath: str):
    try:
        nosql_util = await initialize_cosmos_nosql_util(dbname, cname)
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())


async def test_cosmos_nosql(dbname: str, db_ru: int, cname: str, c_ru: int, pkpath: str):
    logging.info(
        "test_cosmos_nosql, dbname: {}, db_ru: {}, cname: {}, c_ru: {}, pk: {}".format(
            dbname, db_ru, cname, c_ru, pkpath
        )
    )
    try:
        opts = dict()
        opts["enable_diagnostics_logging"] = True
        nosql_util = CosmosNoSqlUtil(opts)
        await nosql_util.initialize()

        dbs = await nosql_util.list_databases()
        logging.info("===== databases: {}".format(dbs))

        try:
            result = await nosql_util.create_database(dbname, db_ru)
            logging.info("===== create_database: {} {} {}".format(dbname, db_ru, result))
        except Exception as e:
            logging.info(str(e))
            logging.info(traceback.format_exc())

        dbproxy = nosql_util.set_db(dbname)
        print("dbproxy: {}".format(dbproxy))

        containers = await nosql_util.list_containers()
        print("containers: {}".format(containers))

        try:
            result = await nosql_util.create_container(cname, c_ru, pkpath)
            logging.info("===== create_container: {} {} {} {}".format(cname, c_ru, pkpath, result))
        except Exception as e:
            logging.info(str(e))
            logging.info(traceback.format_exc())

        ctrproxy = nosql_util.set_container(cname)
        print("ctrproxy: {}".format(ctrproxy))

        # throw_exception_here()

        ctrproxy = nosql_util.set_container(cname)
        print("ctrproxy: {}".format(ctrproxy))

        id = str(uuid.uuid4())

        doc = await nosql_util.upsert_item(create_random_document(id, None))
        print("===== upsert_item doc: {}".format(doc))
        print("last_response_headers: {}".format(nosql_util.last_response_headers()))
        print("last_request_charge: {}".format(nosql_util.last_request_charge()))

        pk = doc["pk"]
        print("===== point_read id: {}, pk: {}".format(id, pk))
        doc = await nosql_util.point_read(id, pk)
        print("point_read doc: {}".format(doc))
        print("last_request_charge: {}".format(nosql_util.last_request_charge()))

        print("===== updating ...")
        doc["name"] = "updated"
        updated = await nosql_util.upsert_item(doc)
        print("updated doc: {}".format(updated))

        print("===== deleting ...")
        response = await nosql_util.delete_item(id, pk)
        print("delete_item response: {}".format(response))

        operations, pk = list(), "bulk_pk"
        for n in range(3):
            # example: ("create", (get_sales_order("create_item"),))
            # each operation is a 2-tuple, with the operation name as tup[0]
            # tup[1] is a nested 2-tuple , with the document as tup[0]
            doc = create_random_document(None, pk)
            print("bulk create_item doc: {}".format(doc))
            op = ("create", (doc,))
            operations.append(op)
        print("===== execute_item_batch with {} operations ...".format(len(operations)))
        results = await nosql_util.execute_item_batch(operations, pk)
        for idx, result in enumerate(results):
            print("batch result {}: {}".format(idx, result))

        print("===== query_items ...")
        results = await nosql_util.query_items("select * from c where c.doctype = 'sample'", True)
        for idx, result in enumerate(results):
            print("select * query result {}: {}".format(idx, result))
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await nosql_util.close()
    logging.info("end of test_cosmos_service")


async def load_python_libraries(dbname: str, cname: str):
    """
    Load the CosmosAIGraph Python libraries documents into the given
    Cosmos NoSQL API database and container.
    """
    logging.info("load_python_libraries, dbname: {}, cname: {}".format(dbname, cname))
    try:
        cosmos = CosmosNoSqlUtil()
        await cosmos.initialize()
        await cosmos.set_db(dbname)
        await cosmos.set_container(cname)

        files = FS.list_files_in_dir("data/cosmosdb")
        for idx, file in enumerate(sorted(files)):
            if idx < 999999:
                infile = f"data/cosmosdb/{file}"
                doc = FS.read_json(infile)
                if doc is not None:
                    resp = await cosmos.upsert_item(doc)
                    print("upsert_item response: {}".format(resp))
                    asyncio.sleep(0.05)
                else:
                    logging.info(f"Error: doc is None for file: {infile}")

        # For DiskANN Vector Search, first enable the Feature as described here:
        # https://learn.microsoft.com/en-us/azure/cosmos-db/nosql/vector-search#enable-the-vector-indexing-and-search-feature

        print("files count: {}".format(len(files)))
        await cosmos.close()

    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())


async def vector_search_similar_libs(dbname: str, cname: str, libname: str):
    nosql_util = await initialize_cosmos_nosql_util(dbname, cname)
    try:
        sql = (
            "SELECT c.id, c.pk, c.name, c.embedding FROM c where c.name = '{}' and c.pk = 'pypi' offset 0 limit 1"
        ).format(libname)
        docs = await nosql_util.query_items(sql, cross_partition=False, pk="/pk", max_items=1)
        if len(docs) == 0:
            print("No document found with id: {}".format(id))
        else:
            embedding = docs[0]["embedding"]
            print("embedding length: {}".format(len(embedding)))
            sql = vector_search_sql(5, embedding)
            FS.write(sql, "tmp/vector_search_sql.txt")
            results = await nosql_util.query_items(sql, True)
            for idx, result in enumerate(results):
                print(result)
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await nosql_util.close()


def vector_search_sql(top_n: int, embedding: list):
    return """
SELECT TOP {} c.id, c.pk, c.name, VectorDistance(c.embedding, {}) AS SimilarityScore
 FROM c
 ORDER BY VectorDistance(c.embedding, {})
""".format(top_n, embedding, embedding).lstrip()


async def vector_search_similar_words(dbname: str, cname: str, words: list):
    nosql_util = await initialize_cosmos_nosql_util(dbname, cname)
    try:
        ai_util = AOAIUtil()
        embedding = await ai_util.generate_embeddings(" ".join(words))
        sql = vector_search_sql(5, embedding)
        results = await nosql_util.query_items(sql, True)
        for idx, result in enumerate(results):
            print(result)
    except Exception as e:
        logging.info(str(e))
        logging.info(traceback.format_exc())
    await nosql_util.close()


async def initialize_cosmos_nosql_util(dbname: str, cname: str):
    opts = dict()
    opts["enable_diagnostics_logging"] = True
    nosql_util = CosmosNoSqlUtil(opts)
    await nosql_util.initialize()
    await nosql_util.set_db(dbname)
    await nosql_util.set_container(cname)
    return nosql_util


def create_random_document(id, pk):
    dg = DataGenerator()
    return dg.random_person_document(id, pk)


def throw_exception_here():
    # intentionally throw an exception
    intentional_exception = 1 / 0
    print("{}".format(intentional_exception))


if __name__ == "__main__":
    # standard initialization of env and logger
    load_dotenv(override=True)
    logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)
    if len(sys.argv) < 2:
        print_options("Error: invalid command-line")
        exit(1)
    else:
        try:
            func = sys.argv[1].lower()
            if func == "list_databases":
                asyncio.run(list_databases())
            elif func == "create_database":
                dbname, db_ru = sys.argv[2], int(sys.argv[3])
                asyncio.run(create_database(dbname, db_ru))
            elif func == "create_container":
                dbname, cname = sys.argv[2], sys.argv[3]
                pkpath, c_ru = sys.argv[4], int(sys.argv[5])
                idx_policy_filename = sys.argv[6]
                asyncio.run(create_container(dbname, cname, pkpath, c_ru, idx_policy_filename))
            elif func == "delete_database":
                dbname = sys.argv[2]
                asyncio.run(delete_database(dbname))
            elif func == "delete_container":
                dbname, cname = sys.argv[2], sys.argv[3]
                asyncio.run(delete_container(dbname, cname))
            elif func == "list_containers":
                dbname = sys.argv[2]
                asyncio.run(list_containers(dbname))
            elif func == "load_airports":
                dbname, cname, pk = sys.argv[2], sys.argv[3], sys.argv[4]
                asyncio.run(load_airports(dbname, cname, pk))
            elif func == "load_python_libraries":
                dbname, cname = sys.argv[2], sys.argv[3]
                asyncio.run(load_python_libraries(dbname, cname))
            elif func == "test_cosmos_nosql":
                dbname = sys.argv[2]
                db_ru = int(sys.argv[3])
                cname = sys.argv[4]
                c_ru = int(sys.argv[5])
                pkpath = sys.argv[6]
                asyncio.run(test_cosmos_nosql(dbname, db_ru, cname, c_ru, pkpath))
            elif func == "vector_search_similar_libs":
                dbname = sys.argv[2]
                cname = sys.argv[3]
                libname = sys.argv[4]
                asyncio.run(vector_search_similar_libs(dbname, cname, libname))
            elif func == "vector_search_similar_words":
                dbname = sys.argv[2]
                cname = sys.argv[3]
                words = sys.argv[4:]
                asyncio.run(vector_search_similar_words(dbname, cname, words))
            else:
                print_options("Error: invalid function: {}".format(func))
        except Exception as e:
            logging.info(str(e))
            logging.info(traceback.format_exc())
