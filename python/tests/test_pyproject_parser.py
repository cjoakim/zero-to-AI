from src.util.pyproject_parser import PyprojectParser

# pytest -v tests/test_pyproject_parser.py
# Chris Joakim, 3Cloud/Cognizant, 2026


def test_all():
    pp = PyprojectParser()
    pp.parse()
    print(f"name: {pp.get_name()}")
    print(f"version: {pp.get_version()}")
    print(f"description: {pp.get_description()}")
    print(f"dependencies: {pp.get_dependencies()}")
    print(f"dependency names: {pp.get_dependency_names()}")

    assert pp.get_name() == "zero-to-AI"
    assert pp.get_version() == "1.0.0"
    assert pp.get_description() == "The 'zero-to-AI' series of lessons at 3Cloud/Cognizant"
    dep_names = pp.get_dependency_names()
    # for name in sorted(dep_names):
    #     print(f"assert '{name}' in dep_names")
    assert len(dep_names) == 69
    assert "Faker" in dep_names
    assert "Jinja2" in dep_names
    assert "SQLAlchemy" in dep_names
    assert "agent-framework" in dep_names
    assert "aiohttp" in dep_names
    assert "alembic" in dep_names
    assert "av" in dep_names
    assert "azure-ai-agents" in dep_names
    assert "azure-ai-documentintelligence" in dep_names
    assert "azure-ai-evaluation" in dep_names
    assert "azure-ai-projects" in dep_names
    assert "azure-ai-textanalytics" in dep_names
    assert "azure-core" in dep_names
    assert "azure-core-tracing-opentelemetry" in dep_names
    assert "azure-cosmos" in dep_names
    assert "azure-identity" in dep_names
    assert "azure-keyvault-secrets" in dep_names
    assert "azure-mgmt-applicationinsights" in dep_names
    assert "azure-mgmt-cognitiveservices" in dep_names
    assert "azure-search-documents" in dep_names
    assert "azure-storage-blob" in dep_names
    assert "beautifulsoup4" in dep_names
    assert "docopt" in dep_names
    assert "duckdb" in dep_names
    assert "fastapi[standard]" in dep_names
    assert "fastmcp" in dep_names
    assert "geopy" in dep_names
    assert "h11" in dep_names
    assert "httpx" in dep_names
    assert "httpx[cli]" in dep_names
    assert "jupyter" in dep_names
    assert "m26" in dep_names
    assert "markdown" in dep_names
    assert "matplotlib" in dep_names
    assert "openai" in dep_names
    assert "opentelemetry-api" in dep_names
    assert "opentelemetry-exporter-otlp-proto-grpc" in dep_names
    assert "opentelemetry-instrumentation-httpx" in dep_names
    assert "opentelemetry-instrumentation-logging" in dep_names
    assert "opentelemetry-instrumentation-psycopg2" in dep_names
    assert "opentelemetry-instrumentation-requests" in dep_names
    assert "opentelemetry-sdk" in dep_names
    assert "pandas" in dep_names
    assert "pgvector" in dep_names
    assert "psutil" in dep_names
    assert "psycopg2-binary" in dep_names
    assert "pydantic" in dep_names
    assert "pydantic-core" in dep_names
    assert "pylint" in dep_names
    assert "pytest" in dep_names
    assert "pytest-asyncio" in dep_names
    assert "pytest-cov" in dep_names
    assert "pytest-randomly" in dep_names
    assert "python-dotenv" in dep_names
    assert "python-json-logger" in dep_names
    assert "python-multipart" in dep_names
    assert "pytz" in dep_names
    assert "rdflib" in dep_names
    assert "six" in dep_names
    assert "sqlalchemy_utils" in dep_names
    assert "streamlit" in dep_names
    assert "tenacity" in dep_names
    assert "tiktoken" in dep_names
    assert "uvicorn" in dep_names
    assert "watchdog" in dep_names
