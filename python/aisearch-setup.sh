
# Invoke Azure AI Search Service, smoketest class AISearchUtil.
# Chris Joakim, 3Cloud/Cognizant, 2026

source .venv/bin/activate

python main-search.py check_env

echo "=== SHELL deleting indexer, index, and datasource ==="
python main-search.py delete_indexer nosql-libraries
python main-search.py delete_index nosql-libraries
python main-search.py delete_datasource cosmosdb-nosql-dev-libraries

echo "=== SHELL listing indexes, indexers, datasources (initial) ==="
python main-search.py list_indexes
python main-search.py list_indexers
python main-search.py list_datasources

echo "=== SHELL creating datasource, index, and indexer ==="
python main-search.py create_cosmos_nosql_datasource dev libraries
python main-search.py create_index nosql-libraries aisearch/libraries_vector_index.json
python main-search.py create_indexer nosql-libraries aisearch/libraries_indexer.json

echo "=== SHELL indexer status ==="
python main-search.py get_indexer_status nosql-libraries

echo "=== SHELL listing indexes, indexers, datasources (eoj) ==="
python main-search.py list_indexes
python main-search.py list_indexers
python main-search.py list_datasources

# Wait until the indexer is finished indexing, then run:
# python main-search.py search_index nosql-libraries libraries_clt aisearch/searches.json

echo "done"
