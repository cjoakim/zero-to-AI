#!/bin/bash

# This script downloads the JSON metadata for each library in the uv-pip-list.txt file.
# It then saves the JSON to a library-specific file in the data/pypi directory.
# Chris Joakim, 3Cloud/Cognizant, 2026

echo "1/289: agent-framework"
curl -s -L https://pypi.python.org/pypi/agent-framework/json | jq > data/pypi_libs/agent-framework.json
sleep 1

echo "2/289: agent-framework-core"
curl -s -L https://pypi.python.org/pypi/agent-framework-core/json | jq > data/pypi_libs/agent-framework-core.json
sleep 1

echo "3/289: aiofiles"
curl -s -L https://pypi.python.org/pypi/aiofiles/json | jq > data/pypi_libs/aiofiles.json
sleep 1

echo "4/289: aiohappyeyeballs"
curl -s -L https://pypi.python.org/pypi/aiohappyeyeballs/json | jq > data/pypi_libs/aiohappyeyeballs.json
sleep 1

echo "5/289: aiohttp"
curl -s -L https://pypi.python.org/pypi/aiohttp/json | jq > data/pypi_libs/aiohttp.json
sleep 1

echo "6/289: aiosignal"
curl -s -L https://pypi.python.org/pypi/aiosignal/json | jq > data/pypi_libs/aiosignal.json
sleep 1

echo "7/289: alembic"
curl -s -L https://pypi.python.org/pypi/alembic/json | jq > data/pypi_libs/alembic.json
sleep 1

echo "8/289: altair"
curl -s -L https://pypi.python.org/pypi/altair/json | jq > data/pypi_libs/altair.json
sleep 1

echo "9/289: annotated-doc"
curl -s -L https://pypi.python.org/pypi/annotated-doc/json | jq > data/pypi_libs/annotated-doc.json
sleep 1

echo "10/289: annotated-types"
curl -s -L https://pypi.python.org/pypi/annotated-types/json | jq > data/pypi_libs/annotated-types.json
sleep 1

echo "11/289: anyio"
curl -s -L https://pypi.python.org/pypi/anyio/json | jq > data/pypi_libs/anyio.json
sleep 1

echo "12/289: appnope"
curl -s -L https://pypi.python.org/pypi/appnope/json | jq > data/pypi_libs/appnope.json
sleep 1

echo "13/289: argon2-cffi"
curl -s -L https://pypi.python.org/pypi/argon2-cffi/json | jq > data/pypi_libs/argon2-cffi.json
sleep 1

echo "14/289: argon2-cffi-bindings"
curl -s -L https://pypi.python.org/pypi/argon2-cffi-bindings/json | jq > data/pypi_libs/argon2-cffi-bindings.json
sleep 1

echo "15/289: arrow"
curl -s -L https://pypi.python.org/pypi/arrow/json | jq > data/pypi_libs/arrow.json
sleep 1

echo "16/289: asgiref"
curl -s -L https://pypi.python.org/pypi/asgiref/json | jq > data/pypi_libs/asgiref.json
sleep 1

echo "17/289: astroid"
curl -s -L https://pypi.python.org/pypi/astroid/json | jq > data/pypi_libs/astroid.json
sleep 1

echo "18/289: asttokens"
curl -s -L https://pypi.python.org/pypi/asttokens/json | jq > data/pypi_libs/asttokens.json
sleep 1

echo "19/289: async-lru"
curl -s -L https://pypi.python.org/pypi/async-lru/json | jq > data/pypi_libs/async-lru.json
sleep 1

echo "20/289: attrs"
curl -s -L https://pypi.python.org/pypi/attrs/json | jq > data/pypi_libs/attrs.json
sleep 1

echo "21/289: authlib"
curl -s -L https://pypi.python.org/pypi/authlib/json | jq > data/pypi_libs/authlib.json
sleep 1

echo "22/289: av"
curl -s -L https://pypi.python.org/pypi/av/json | jq > data/pypi_libs/av.json
sleep 1

echo "23/289: azure-ai-agents"
curl -s -L https://pypi.python.org/pypi/azure-ai-agents/json | jq > data/pypi_libs/azure-ai-agents.json
sleep 1

echo "24/289: azure-ai-documentintelligence"
curl -s -L https://pypi.python.org/pypi/azure-ai-documentintelligence/json | jq > data/pypi_libs/azure-ai-documentintelligence.json
sleep 1

echo "25/289: azure-ai-evaluation"
curl -s -L https://pypi.python.org/pypi/azure-ai-evaluation/json | jq > data/pypi_libs/azure-ai-evaluation.json
sleep 1

echo "26/289: azure-ai-projects"
curl -s -L https://pypi.python.org/pypi/azure-ai-projects/json | jq > data/pypi_libs/azure-ai-projects.json
sleep 1

echo "27/289: azure-ai-textanalytics"
curl -s -L https://pypi.python.org/pypi/azure-ai-textanalytics/json | jq > data/pypi_libs/azure-ai-textanalytics.json
sleep 1

echo "28/289: azure-common"
curl -s -L https://pypi.python.org/pypi/azure-common/json | jq > data/pypi_libs/azure-common.json
sleep 1

echo "29/289: azure-core"
curl -s -L https://pypi.python.org/pypi/azure-core/json | jq > data/pypi_libs/azure-core.json
sleep 1

echo "30/289: azure-core-tracing-opentelemetry"
curl -s -L https://pypi.python.org/pypi/azure-core-tracing-opentelemetry/json | jq > data/pypi_libs/azure-core-tracing-opentelemetry.json
sleep 1

echo "31/289: azure-cosmos"
curl -s -L https://pypi.python.org/pypi/azure-cosmos/json | jq > data/pypi_libs/azure-cosmos.json
sleep 1

echo "32/289: azure-identity"
curl -s -L https://pypi.python.org/pypi/azure-identity/json | jq > data/pypi_libs/azure-identity.json
sleep 1

echo "33/289: azure-keyvault-secrets"
curl -s -L https://pypi.python.org/pypi/azure-keyvault-secrets/json | jq > data/pypi_libs/azure-keyvault-secrets.json
sleep 1

echo "34/289: azure-mgmt-applicationinsights"
curl -s -L https://pypi.python.org/pypi/azure-mgmt-applicationinsights/json | jq > data/pypi_libs/azure-mgmt-applicationinsights.json
sleep 1

echo "35/289: azure-mgmt-cognitiveservices"
curl -s -L https://pypi.python.org/pypi/azure-mgmt-cognitiveservices/json | jq > data/pypi_libs/azure-mgmt-cognitiveservices.json
sleep 1

echo "36/289: azure-mgmt-core"
curl -s -L https://pypi.python.org/pypi/azure-mgmt-core/json | jq > data/pypi_libs/azure-mgmt-core.json
sleep 1

echo "37/289: azure-monitor-opentelemetry"
curl -s -L https://pypi.python.org/pypi/azure-monitor-opentelemetry/json | jq > data/pypi_libs/azure-monitor-opentelemetry.json
sleep 1

echo "38/289: azure-monitor-opentelemetry-exporter"
curl -s -L https://pypi.python.org/pypi/azure-monitor-opentelemetry-exporter/json | jq > data/pypi_libs/azure-monitor-opentelemetry-exporter.json
sleep 1

echo "39/289: azure-search-documents"
curl -s -L https://pypi.python.org/pypi/azure-search-documents/json | jq > data/pypi_libs/azure-search-documents.json
sleep 1

echo "40/289: azure-storage-blob"
curl -s -L https://pypi.python.org/pypi/azure-storage-blob/json | jq > data/pypi_libs/azure-storage-blob.json
sleep 1

echo "41/289: babel"
curl -s -L https://pypi.python.org/pypi/babel/json | jq > data/pypi_libs/babel.json
sleep 1

echo "42/289: beartype"
curl -s -L https://pypi.python.org/pypi/beartype/json | jq > data/pypi_libs/beartype.json
sleep 1

echo "43/289: beautifulsoup4"
curl -s -L https://pypi.python.org/pypi/beautifulsoup4/json | jq > data/pypi_libs/beautifulsoup4.json
sleep 1

echo "44/289: bleach"
curl -s -L https://pypi.python.org/pypi/bleach/json | jq > data/pypi_libs/bleach.json
sleep 1

echo "45/289: blinker"
curl -s -L https://pypi.python.org/pypi/blinker/json | jq > data/pypi_libs/blinker.json
sleep 1

echo "46/289: cachetools"
curl -s -L https://pypi.python.org/pypi/cachetools/json | jq > data/pypi_libs/cachetools.json
sleep 1

echo "47/289: certifi"
curl -s -L https://pypi.python.org/pypi/certifi/json | jq > data/pypi_libs/certifi.json
sleep 1

echo "48/289: cffi"
curl -s -L https://pypi.python.org/pypi/cffi/json | jq > data/pypi_libs/cffi.json
sleep 1

echo "49/289: charset-normalizer"
curl -s -L https://pypi.python.org/pypi/charset-normalizer/json | jq > data/pypi_libs/charset-normalizer.json
sleep 1

echo "50/289: click"
curl -s -L https://pypi.python.org/pypi/click/json | jq > data/pypi_libs/click.json
sleep 1

echo "51/289: cloudpickle"
curl -s -L https://pypi.python.org/pypi/cloudpickle/json | jq > data/pypi_libs/cloudpickle.json
sleep 1

echo "52/289: comm"
curl -s -L https://pypi.python.org/pypi/comm/json | jq > data/pypi_libs/comm.json
sleep 1

echo "53/289: contourpy"
curl -s -L https://pypi.python.org/pypi/contourpy/json | jq > data/pypi_libs/contourpy.json
sleep 1

echo "54/289: coverage"
curl -s -L https://pypi.python.org/pypi/coverage/json | jq > data/pypi_libs/coverage.json
sleep 1

echo "55/289: croniter"
curl -s -L https://pypi.python.org/pypi/croniter/json | jq > data/pypi_libs/croniter.json
sleep 1

echo "56/289: cryptography"
curl -s -L https://pypi.python.org/pypi/cryptography/json | jq > data/pypi_libs/cryptography.json
sleep 1

echo "57/289: cycler"
curl -s -L https://pypi.python.org/pypi/cycler/json | jq > data/pypi_libs/cycler.json
sleep 1

echo "58/289: cyclopts"
curl -s -L https://pypi.python.org/pypi/cyclopts/json | jq > data/pypi_libs/cyclopts.json
sleep 1

echo "59/289: debugpy"
curl -s -L https://pypi.python.org/pypi/debugpy/json | jq > data/pypi_libs/debugpy.json
sleep 1

echo "60/289: decorator"
curl -s -L https://pypi.python.org/pypi/decorator/json | jq > data/pypi_libs/decorator.json
sleep 1

echo "61/289: defusedxml"
curl -s -L https://pypi.python.org/pypi/defusedxml/json | jq > data/pypi_libs/defusedxml.json
sleep 1

echo "62/289: dill"
curl -s -L https://pypi.python.org/pypi/dill/json | jq > data/pypi_libs/dill.json
sleep 1

echo "63/289: diskcache"
curl -s -L https://pypi.python.org/pypi/diskcache/json | jq > data/pypi_libs/diskcache.json
sleep 1

echo "64/289: distro"
curl -s -L https://pypi.python.org/pypi/distro/json | jq > data/pypi_libs/distro.json
sleep 1

echo "65/289: dnspython"
curl -s -L https://pypi.python.org/pypi/dnspython/json | jq > data/pypi_libs/dnspython.json
sleep 1

echo "66/289: docopt"
curl -s -L https://pypi.python.org/pypi/docopt/json | jq > data/pypi_libs/docopt.json
sleep 1

echo "67/289: docstring-parser"
curl -s -L https://pypi.python.org/pypi/docstring-parser/json | jq > data/pypi_libs/docstring-parser.json
sleep 1

echo "68/289: docutils"
curl -s -L https://pypi.python.org/pypi/docutils/json | jq > data/pypi_libs/docutils.json
sleep 1

echo "69/289: duckdb"
curl -s -L https://pypi.python.org/pypi/duckdb/json | jq > data/pypi_libs/duckdb.json
sleep 1

echo "70/289: email-validator"
curl -s -L https://pypi.python.org/pypi/email-validator/json | jq > data/pypi_libs/email-validator.json
sleep 1

echo "71/289: exceptiongroup"
curl -s -L https://pypi.python.org/pypi/exceptiongroup/json | jq > data/pypi_libs/exceptiongroup.json
sleep 1

echo "72/289: executing"
curl -s -L https://pypi.python.org/pypi/executing/json | jq > data/pypi_libs/executing.json
sleep 1

echo "73/289: faker"
curl -s -L https://pypi.python.org/pypi/faker/json | jq > data/pypi_libs/faker.json
sleep 1

echo "74/289: fakeredis"
curl -s -L https://pypi.python.org/pypi/fakeredis/json | jq > data/pypi_libs/fakeredis.json
sleep 1

echo "75/289: fastapi"
curl -s -L https://pypi.python.org/pypi/fastapi/json | jq > data/pypi_libs/fastapi.json
sleep 1

echo "76/289: fastapi-cli"
curl -s -L https://pypi.python.org/pypi/fastapi-cli/json | jq > data/pypi_libs/fastapi-cli.json
sleep 1

echo "77/289: fastapi-cloud-cli"
curl -s -L https://pypi.python.org/pypi/fastapi-cloud-cli/json | jq > data/pypi_libs/fastapi-cloud-cli.json
sleep 1

echo "78/289: fastar"
curl -s -L https://pypi.python.org/pypi/fastar/json | jq > data/pypi_libs/fastar.json
sleep 1

echo "79/289: fastjsonschema"
curl -s -L https://pypi.python.org/pypi/fastjsonschema/json | jq > data/pypi_libs/fastjsonschema.json
sleep 1

echo "80/289: fastmcp"
curl -s -L https://pypi.python.org/pypi/fastmcp/json | jq > data/pypi_libs/fastmcp.json
sleep 1

echo "81/289: fonttools"
curl -s -L https://pypi.python.org/pypi/fonttools/json | jq > data/pypi_libs/fonttools.json
sleep 1

echo "82/289: fqdn"
curl -s -L https://pypi.python.org/pypi/fqdn/json | jq > data/pypi_libs/fqdn.json
sleep 1

echo "83/289: frozenlist"
curl -s -L https://pypi.python.org/pypi/frozenlist/json | jq > data/pypi_libs/frozenlist.json
sleep 1

echo "84/289: geographiclib"
curl -s -L https://pypi.python.org/pypi/geographiclib/json | jq > data/pypi_libs/geographiclib.json
sleep 1

echo "85/289: geopy"
curl -s -L https://pypi.python.org/pypi/geopy/json | jq > data/pypi_libs/geopy.json
sleep 1

echo "86/289: gitdb"
curl -s -L https://pypi.python.org/pypi/gitdb/json | jq > data/pypi_libs/gitdb.json
sleep 1

echo "87/289: gitpython"
curl -s -L https://pypi.python.org/pypi/gitpython/json | jq > data/pypi_libs/gitpython.json
sleep 1

echo "88/289: googleapis-common-protos"
curl -s -L https://pypi.python.org/pypi/googleapis-common-protos/json | jq > data/pypi_libs/googleapis-common-protos.json
sleep 1

echo "89/289: grpcio"
curl -s -L https://pypi.python.org/pypi/grpcio/json | jq > data/pypi_libs/grpcio.json
sleep 1

echo "90/289: h11"
curl -s -L https://pypi.python.org/pypi/h11/json | jq > data/pypi_libs/h11.json
sleep 1

echo "91/289: httpcore"
curl -s -L https://pypi.python.org/pypi/httpcore/json | jq > data/pypi_libs/httpcore.json
sleep 1

echo "92/289: httptools"
curl -s -L https://pypi.python.org/pypi/httptools/json | jq > data/pypi_libs/httptools.json
sleep 1

echo "93/289: httpx"
curl -s -L https://pypi.python.org/pypi/httpx/json | jq > data/pypi_libs/httpx.json
sleep 1

echo "94/289: httpx-sse"
curl -s -L https://pypi.python.org/pypi/httpx-sse/json | jq > data/pypi_libs/httpx-sse.json
sleep 1

echo "95/289: idna"
curl -s -L https://pypi.python.org/pypi/idna/json | jq > data/pypi_libs/idna.json
sleep 1

echo "96/289: importlib-metadata"
curl -s -L https://pypi.python.org/pypi/importlib-metadata/json | jq > data/pypi_libs/importlib-metadata.json
sleep 1

echo "97/289: iniconfig"
curl -s -L https://pypi.python.org/pypi/iniconfig/json | jq > data/pypi_libs/iniconfig.json
sleep 1

echo "98/289: ipykernel"
curl -s -L https://pypi.python.org/pypi/ipykernel/json | jq > data/pypi_libs/ipykernel.json
sleep 1

echo "99/289: ipython"
curl -s -L https://pypi.python.org/pypi/ipython/json | jq > data/pypi_libs/ipython.json
sleep 1

echo "100/289: ipython-pygments-lexers"
curl -s -L https://pypi.python.org/pypi/ipython-pygments-lexers/json | jq > data/pypi_libs/ipython-pygments-lexers.json
sleep 1

echo "101/289: ipywidgets"
curl -s -L https://pypi.python.org/pypi/ipywidgets/json | jq > data/pypi_libs/ipywidgets.json
sleep 1

echo "102/289: isodate"
curl -s -L https://pypi.python.org/pypi/isodate/json | jq > data/pypi_libs/isodate.json
sleep 1

echo "103/289: isoduration"
curl -s -L https://pypi.python.org/pypi/isoduration/json | jq > data/pypi_libs/isoduration.json
sleep 1

echo "104/289: isort"
curl -s -L https://pypi.python.org/pypi/isort/json | jq > data/pypi_libs/isort.json
sleep 1

echo "105/289: jaraco-classes"
curl -s -L https://pypi.python.org/pypi/jaraco-classes/json | jq > data/pypi_libs/jaraco-classes.json
sleep 1

echo "106/289: jaraco-context"
curl -s -L https://pypi.python.org/pypi/jaraco-context/json | jq > data/pypi_libs/jaraco-context.json
sleep 1

echo "107/289: jaraco-functools"
curl -s -L https://pypi.python.org/pypi/jaraco-functools/json | jq > data/pypi_libs/jaraco-functools.json
sleep 1

echo "108/289: jedi"
curl -s -L https://pypi.python.org/pypi/jedi/json | jq > data/pypi_libs/jedi.json
sleep 1

echo "109/289: jinja2"
curl -s -L https://pypi.python.org/pypi/jinja2/json | jq > data/pypi_libs/jinja2.json
sleep 1

echo "110/289: jiter"
curl -s -L https://pypi.python.org/pypi/jiter/json | jq > data/pypi_libs/jiter.json
sleep 1

echo "111/289: joblib"
curl -s -L https://pypi.python.org/pypi/joblib/json | jq > data/pypi_libs/joblib.json
sleep 1

echo "112/289: json5"
curl -s -L https://pypi.python.org/pypi/json5/json | jq > data/pypi_libs/json5.json
sleep 1

echo "113/289: jsonpointer"
curl -s -L https://pypi.python.org/pypi/jsonpointer/json | jq > data/pypi_libs/jsonpointer.json
sleep 1

echo "114/289: jsonschema"
curl -s -L https://pypi.python.org/pypi/jsonschema/json | jq > data/pypi_libs/jsonschema.json
sleep 1

echo "115/289: jsonschema-path"
curl -s -L https://pypi.python.org/pypi/jsonschema-path/json | jq > data/pypi_libs/jsonschema-path.json
sleep 1

echo "116/289: jsonschema-specifications"
curl -s -L https://pypi.python.org/pypi/jsonschema-specifications/json | jq > data/pypi_libs/jsonschema-specifications.json
sleep 1

echo "117/289: jupyter"
curl -s -L https://pypi.python.org/pypi/jupyter/json | jq > data/pypi_libs/jupyter.json
sleep 1

echo "118/289: jupyter-client"
curl -s -L https://pypi.python.org/pypi/jupyter-client/json | jq > data/pypi_libs/jupyter-client.json
sleep 1

echo "119/289: jupyter-console"
curl -s -L https://pypi.python.org/pypi/jupyter-console/json | jq > data/pypi_libs/jupyter-console.json
sleep 1

echo "120/289: jupyter-core"
curl -s -L https://pypi.python.org/pypi/jupyter-core/json | jq > data/pypi_libs/jupyter-core.json
sleep 1

echo "121/289: jupyter-events"
curl -s -L https://pypi.python.org/pypi/jupyter-events/json | jq > data/pypi_libs/jupyter-events.json
sleep 1

echo "122/289: jupyter-lsp"
curl -s -L https://pypi.python.org/pypi/jupyter-lsp/json | jq > data/pypi_libs/jupyter-lsp.json
sleep 1

echo "123/289: jupyter-server"
curl -s -L https://pypi.python.org/pypi/jupyter-server/json | jq > data/pypi_libs/jupyter-server.json
sleep 1

echo "124/289: jupyter-server-terminals"
curl -s -L https://pypi.python.org/pypi/jupyter-server-terminals/json | jq > data/pypi_libs/jupyter-server-terminals.json
sleep 1

echo "125/289: jupyterlab"
curl -s -L https://pypi.python.org/pypi/jupyterlab/json | jq > data/pypi_libs/jupyterlab.json
sleep 1

echo "126/289: jupyterlab-pygments"
curl -s -L https://pypi.python.org/pypi/jupyterlab-pygments/json | jq > data/pypi_libs/jupyterlab-pygments.json
sleep 1

echo "127/289: jupyterlab-server"
curl -s -L https://pypi.python.org/pypi/jupyterlab-server/json | jq > data/pypi_libs/jupyterlab-server.json
sleep 1

echo "128/289: jupyterlab-widgets"
curl -s -L https://pypi.python.org/pypi/jupyterlab-widgets/json | jq > data/pypi_libs/jupyterlab-widgets.json
sleep 1

echo "129/289: keyring"
curl -s -L https://pypi.python.org/pypi/keyring/json | jq > data/pypi_libs/keyring.json
sleep 1

echo "130/289: kiwisolver"
curl -s -L https://pypi.python.org/pypi/kiwisolver/json | jq > data/pypi_libs/kiwisolver.json
sleep 1

echo "131/289: lark"
curl -s -L https://pypi.python.org/pypi/lark/json | jq > data/pypi_libs/lark.json
sleep 1

echo "132/289: lupa"
curl -s -L https://pypi.python.org/pypi/lupa/json | jq > data/pypi_libs/lupa.json
sleep 1

echo "133/289: m26"
curl -s -L https://pypi.python.org/pypi/m26/json | jq > data/pypi_libs/m26.json
sleep 1

echo "134/289: mako"
curl -s -L https://pypi.python.org/pypi/mako/json | jq > data/pypi_libs/mako.json
sleep 1

echo "135/289: markdown"
curl -s -L https://pypi.python.org/pypi/markdown/json | jq > data/pypi_libs/markdown.json
sleep 1

echo "136/289: markdown-it-py"
curl -s -L https://pypi.python.org/pypi/markdown-it-py/json | jq > data/pypi_libs/markdown-it-py.json
sleep 1

echo "137/289: markupsafe"
curl -s -L https://pypi.python.org/pypi/markupsafe/json | jq > data/pypi_libs/markupsafe.json
sleep 1

echo "138/289: matplotlib"
curl -s -L https://pypi.python.org/pypi/matplotlib/json | jq > data/pypi_libs/matplotlib.json
sleep 1

echo "139/289: matplotlib-inline"
curl -s -L https://pypi.python.org/pypi/matplotlib-inline/json | jq > data/pypi_libs/matplotlib-inline.json
sleep 1

echo "140/289: mccabe"
curl -s -L https://pypi.python.org/pypi/mccabe/json | jq > data/pypi_libs/mccabe.json
sleep 1

echo "141/289: mcp"
curl -s -L https://pypi.python.org/pypi/mcp/json | jq > data/pypi_libs/mcp.json
sleep 1

echo "142/289: mdurl"
curl -s -L https://pypi.python.org/pypi/mdurl/json | jq > data/pypi_libs/mdurl.json
sleep 1

echo "143/289: mistune"
curl -s -L https://pypi.python.org/pypi/mistune/json | jq > data/pypi_libs/mistune.json
sleep 1

echo "144/289: more-itertools"
curl -s -L https://pypi.python.org/pypi/more-itertools/json | jq > data/pypi_libs/more-itertools.json
sleep 1

echo "145/289: msal"
curl -s -L https://pypi.python.org/pypi/msal/json | jq > data/pypi_libs/msal.json
sleep 1

echo "146/289: msal-extensions"
curl -s -L https://pypi.python.org/pypi/msal-extensions/json | jq > data/pypi_libs/msal-extensions.json
sleep 1

echo "147/289: msrest"
curl -s -L https://pypi.python.org/pypi/msrest/json | jq > data/pypi_libs/msrest.json
sleep 1

echo "148/289: multidict"
curl -s -L https://pypi.python.org/pypi/multidict/json | jq > data/pypi_libs/multidict.json
sleep 1

echo "149/289: narwhals"
curl -s -L https://pypi.python.org/pypi/narwhals/json | jq > data/pypi_libs/narwhals.json
sleep 1

echo "150/289: nbclient"
curl -s -L https://pypi.python.org/pypi/nbclient/json | jq > data/pypi_libs/nbclient.json
sleep 1

echo "151/289: nbconvert"
curl -s -L https://pypi.python.org/pypi/nbconvert/json | jq > data/pypi_libs/nbconvert.json
sleep 1

echo "152/289: nbformat"
curl -s -L https://pypi.python.org/pypi/nbformat/json | jq > data/pypi_libs/nbformat.json
sleep 1

echo "153/289: nest-asyncio"
curl -s -L https://pypi.python.org/pypi/nest-asyncio/json | jq > data/pypi_libs/nest-asyncio.json
sleep 1

echo "154/289: nltk"
curl -s -L https://pypi.python.org/pypi/nltk/json | jq > data/pypi_libs/nltk.json
sleep 1

echo "155/289: notebook"
curl -s -L https://pypi.python.org/pypi/notebook/json | jq > data/pypi_libs/notebook.json
sleep 1

echo "156/289: notebook-shim"
curl -s -L https://pypi.python.org/pypi/notebook-shim/json | jq > data/pypi_libs/notebook-shim.json
sleep 1

echo "157/289: numpy"
curl -s -L https://pypi.python.org/pypi/numpy/json | jq > data/pypi_libs/numpy.json
sleep 1

echo "158/289: oauthlib"
curl -s -L https://pypi.python.org/pypi/oauthlib/json | jq > data/pypi_libs/oauthlib.json
sleep 1

echo "159/289: openai"
curl -s -L https://pypi.python.org/pypi/openai/json | jq > data/pypi_libs/openai.json
sleep 1

echo "160/289: openapi-pydantic"
curl -s -L https://pypi.python.org/pypi/openapi-pydantic/json | jq > data/pypi_libs/openapi-pydantic.json
sleep 1

echo "161/289: opentelemetry-api"
curl -s -L https://pypi.python.org/pypi/opentelemetry-api/json | jq > data/pypi_libs/opentelemetry-api.json
sleep 1

echo "162/289: opentelemetry-exporter-otlp-proto-common"
curl -s -L https://pypi.python.org/pypi/opentelemetry-exporter-otlp-proto-common/json | jq > data/pypi_libs/opentelemetry-exporter-otlp-proto-common.json
sleep 1

echo "163/289: opentelemetry-exporter-otlp-proto-grpc"
curl -s -L https://pypi.python.org/pypi/opentelemetry-exporter-otlp-proto-grpc/json | jq > data/pypi_libs/opentelemetry-exporter-otlp-proto-grpc.json
sleep 1

echo "164/289: opentelemetry-instrumentation"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation/json | jq > data/pypi_libs/opentelemetry-instrumentation.json
sleep 1

echo "165/289: opentelemetry-instrumentation-asgi"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-asgi/json | jq > data/pypi_libs/opentelemetry-instrumentation-asgi.json
sleep 1

echo "166/289: opentelemetry-instrumentation-dbapi"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-dbapi/json | jq > data/pypi_libs/opentelemetry-instrumentation-dbapi.json
sleep 1

echo "167/289: opentelemetry-instrumentation-django"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-django/json | jq > data/pypi_libs/opentelemetry-instrumentation-django.json
sleep 1

echo "168/289: opentelemetry-instrumentation-fastapi"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-fastapi/json | jq > data/pypi_libs/opentelemetry-instrumentation-fastapi.json
sleep 1

echo "169/289: opentelemetry-instrumentation-flask"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-flask/json | jq > data/pypi_libs/opentelemetry-instrumentation-flask.json
sleep 1

echo "170/289: opentelemetry-instrumentation-httpx"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-httpx/json | jq > data/pypi_libs/opentelemetry-instrumentation-httpx.json
sleep 1

echo "171/289: opentelemetry-instrumentation-logging"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-logging/json | jq > data/pypi_libs/opentelemetry-instrumentation-logging.json
sleep 1

echo "172/289: opentelemetry-instrumentation-psycopg2"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-psycopg2/json | jq > data/pypi_libs/opentelemetry-instrumentation-psycopg2.json
sleep 1

echo "173/289: opentelemetry-instrumentation-requests"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-requests/json | jq > data/pypi_libs/opentelemetry-instrumentation-requests.json
sleep 1

echo "174/289: opentelemetry-instrumentation-urllib"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-urllib/json | jq > data/pypi_libs/opentelemetry-instrumentation-urllib.json
sleep 1

echo "175/289: opentelemetry-instrumentation-urllib3"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-urllib3/json | jq > data/pypi_libs/opentelemetry-instrumentation-urllib3.json
sleep 1

echo "176/289: opentelemetry-instrumentation-wsgi"
curl -s -L https://pypi.python.org/pypi/opentelemetry-instrumentation-wsgi/json | jq > data/pypi_libs/opentelemetry-instrumentation-wsgi.json
sleep 1

echo "177/289: opentelemetry-proto"
curl -s -L https://pypi.python.org/pypi/opentelemetry-proto/json | jq > data/pypi_libs/opentelemetry-proto.json
sleep 1

echo "178/289: opentelemetry-resource-detector-azure"
curl -s -L https://pypi.python.org/pypi/opentelemetry-resource-detector-azure/json | jq > data/pypi_libs/opentelemetry-resource-detector-azure.json
sleep 1

echo "179/289: opentelemetry-sdk"
curl -s -L https://pypi.python.org/pypi/opentelemetry-sdk/json | jq > data/pypi_libs/opentelemetry-sdk.json
sleep 1

echo "180/289: opentelemetry-semantic-conventions"
curl -s -L https://pypi.python.org/pypi/opentelemetry-semantic-conventions/json | jq > data/pypi_libs/opentelemetry-semantic-conventions.json
sleep 1

echo "181/289: opentelemetry-semantic-conventions-ai"
curl -s -L https://pypi.python.org/pypi/opentelemetry-semantic-conventions-ai/json | jq > data/pypi_libs/opentelemetry-semantic-conventions-ai.json
sleep 1

echo "182/289: opentelemetry-util-http"
curl -s -L https://pypi.python.org/pypi/opentelemetry-util-http/json | jq > data/pypi_libs/opentelemetry-util-http.json
sleep 1

echo "183/289: packaging"
curl -s -L https://pypi.python.org/pypi/packaging/json | jq > data/pypi_libs/packaging.json
sleep 1

echo "184/289: pandas"
curl -s -L https://pypi.python.org/pypi/pandas/json | jq > data/pypi_libs/pandas.json
sleep 1

echo "185/289: pandocfilters"
curl -s -L https://pypi.python.org/pypi/pandocfilters/json | jq > data/pypi_libs/pandocfilters.json
sleep 1

echo "186/289: parso"
curl -s -L https://pypi.python.org/pypi/parso/json | jq > data/pypi_libs/parso.json
sleep 1

echo "187/289: pathable"
curl -s -L https://pypi.python.org/pypi/pathable/json | jq > data/pypi_libs/pathable.json
sleep 1

echo "188/289: pathvalidate"
curl -s -L https://pypi.python.org/pypi/pathvalidate/json | jq > data/pypi_libs/pathvalidate.json
sleep 1

echo "189/289: pexpect"
curl -s -L https://pypi.python.org/pypi/pexpect/json | jq > data/pypi_libs/pexpect.json
sleep 1

echo "190/289: pgvector"
curl -s -L https://pypi.python.org/pypi/pgvector/json | jq > data/pypi_libs/pgvector.json
sleep 1

echo "191/289: pillow"
curl -s -L https://pypi.python.org/pypi/pillow/json | jq > data/pypi_libs/pillow.json
sleep 1

echo "192/289: platformdirs"
curl -s -L https://pypi.python.org/pypi/platformdirs/json | jq > data/pypi_libs/platformdirs.json
sleep 1

echo "193/289: pluggy"
curl -s -L https://pypi.python.org/pypi/pluggy/json | jq > data/pypi_libs/pluggy.json
sleep 1

echo "194/289: polars"
curl -s -L https://pypi.python.org/pypi/polars/json | jq > data/pypi_libs/polars.json
sleep 1

echo "195/289: polars-runtime-32"
curl -s -L https://pypi.python.org/pypi/polars-runtime-32/json | jq > data/pypi_libs/polars-runtime-32.json
sleep 1

echo "196/289: prometheus-client"
curl -s -L https://pypi.python.org/pypi/prometheus-client/json | jq > data/pypi_libs/prometheus-client.json
sleep 1

echo "197/289: prompt-toolkit"
curl -s -L https://pypi.python.org/pypi/prompt-toolkit/json | jq > data/pypi_libs/prompt-toolkit.json
sleep 1

echo "198/289: propcache"
curl -s -L https://pypi.python.org/pypi/propcache/json | jq > data/pypi_libs/propcache.json
sleep 1

echo "199/289: protobuf"
curl -s -L https://pypi.python.org/pypi/protobuf/json | jq > data/pypi_libs/protobuf.json
sleep 1

echo "200/289: psutil"
curl -s -L https://pypi.python.org/pypi/psutil/json | jq > data/pypi_libs/psutil.json
sleep 1

echo "201/289: psycopg2-binary"
curl -s -L https://pypi.python.org/pypi/psycopg2-binary/json | jq > data/pypi_libs/psycopg2-binary.json
sleep 1

echo "202/289: ptyprocess"
curl -s -L https://pypi.python.org/pypi/ptyprocess/json | jq > data/pypi_libs/ptyprocess.json
sleep 1

echo "203/289: pure-eval"
curl -s -L https://pypi.python.org/pypi/pure-eval/json | jq > data/pypi_libs/pure-eval.json
sleep 1

echo "204/289: py-key-value-aio"
curl -s -L https://pypi.python.org/pypi/py-key-value-aio/json | jq > data/pypi_libs/py-key-value-aio.json
sleep 1

echo "205/289: py-key-value-shared"
curl -s -L https://pypi.python.org/pypi/py-key-value-shared/json | jq > data/pypi_libs/py-key-value-shared.json
sleep 1

echo "206/289: pyarrow"
curl -s -L https://pypi.python.org/pypi/pyarrow/json | jq > data/pypi_libs/pyarrow.json
sleep 1

echo "207/289: pycparser"
curl -s -L https://pypi.python.org/pypi/pycparser/json | jq > data/pypi_libs/pycparser.json
sleep 1

echo "208/289: pydantic"
curl -s -L https://pypi.python.org/pypi/pydantic/json | jq > data/pypi_libs/pydantic.json
sleep 1

echo "209/289: pydantic-core"
curl -s -L https://pypi.python.org/pypi/pydantic-core/json | jq > data/pypi_libs/pydantic-core.json
sleep 1

echo "210/289: pydantic-extra-types"
curl -s -L https://pypi.python.org/pypi/pydantic-extra-types/json | jq > data/pypi_libs/pydantic-extra-types.json
sleep 1

echo "211/289: pydantic-settings"
curl -s -L https://pypi.python.org/pypi/pydantic-settings/json | jq > data/pypi_libs/pydantic-settings.json
sleep 1

echo "212/289: pydeck"
curl -s -L https://pypi.python.org/pypi/pydeck/json | jq > data/pypi_libs/pydeck.json
sleep 1

echo "213/289: pydocket"
curl -s -L https://pypi.python.org/pypi/pydocket/json | jq > data/pypi_libs/pydocket.json
sleep 1

echo "214/289: pygments"
curl -s -L https://pypi.python.org/pypi/pygments/json | jq > data/pypi_libs/pygments.json
sleep 1

echo "215/289: pyjwt"
curl -s -L https://pypi.python.org/pypi/pyjwt/json | jq > data/pypi_libs/pyjwt.json
sleep 1

echo "216/289: pylint"
curl -s -L https://pypi.python.org/pypi/pylint/json | jq > data/pypi_libs/pylint.json
sleep 1

echo "217/289: pyparsing"
curl -s -L https://pypi.python.org/pypi/pyparsing/json | jq > data/pypi_libs/pyparsing.json
sleep 1

echo "218/289: pyperclip"
curl -s -L https://pypi.python.org/pypi/pyperclip/json | jq > data/pypi_libs/pyperclip.json
sleep 1

echo "219/289: pytest"
curl -s -L https://pypi.python.org/pypi/pytest/json | jq > data/pypi_libs/pytest.json
sleep 1

echo "220/289: pytest-asyncio"
curl -s -L https://pypi.python.org/pypi/pytest-asyncio/json | jq > data/pypi_libs/pytest-asyncio.json
sleep 1

echo "221/289: pytest-cov"
curl -s -L https://pypi.python.org/pypi/pytest-cov/json | jq > data/pypi_libs/pytest-cov.json
sleep 1

echo "222/289: pytest-randomly"
curl -s -L https://pypi.python.org/pypi/pytest-randomly/json | jq > data/pypi_libs/pytest-randomly.json
sleep 1

echo "223/289: python-dateutil"
curl -s -L https://pypi.python.org/pypi/python-dateutil/json | jq > data/pypi_libs/python-dateutil.json
sleep 1

echo "224/289: python-dotenv"
curl -s -L https://pypi.python.org/pypi/python-dotenv/json | jq > data/pypi_libs/python-dotenv.json
sleep 1

echo "225/289: python-json-logger"
curl -s -L https://pypi.python.org/pypi/python-json-logger/json | jq > data/pypi_libs/python-json-logger.json
sleep 1

echo "226/289: python-multipart"
curl -s -L https://pypi.python.org/pypi/python-multipart/json | jq > data/pypi_libs/python-multipart.json
sleep 1

echo "227/289: pytz"
curl -s -L https://pypi.python.org/pypi/pytz/json | jq > data/pypi_libs/pytz.json
sleep 1

echo "228/289: pyyaml"
curl -s -L https://pypi.python.org/pypi/pyyaml/json | jq > data/pypi_libs/pyyaml.json
sleep 1

echo "229/289: pyzmq"
curl -s -L https://pypi.python.org/pypi/pyzmq/json | jq > data/pypi_libs/pyzmq.json
sleep 1

echo "230/289: rdflib"
curl -s -L https://pypi.python.org/pypi/rdflib/json | jq > data/pypi_libs/rdflib.json
sleep 1

echo "231/289: redis"
curl -s -L https://pypi.python.org/pypi/redis/json | jq > data/pypi_libs/redis.json
sleep 1

echo "232/289: referencing"
curl -s -L https://pypi.python.org/pypi/referencing/json | jq > data/pypi_libs/referencing.json
sleep 1

echo "233/289: regex"
curl -s -L https://pypi.python.org/pypi/regex/json | jq > data/pypi_libs/regex.json
sleep 1

echo "234/289: requests"
curl -s -L https://pypi.python.org/pypi/requests/json | jq > data/pypi_libs/requests.json
sleep 1

echo "235/289: requests-oauthlib"
curl -s -L https://pypi.python.org/pypi/requests-oauthlib/json | jq > data/pypi_libs/requests-oauthlib.json
sleep 1

echo "236/289: rfc3339-validator"
curl -s -L https://pypi.python.org/pypi/rfc3339-validator/json | jq > data/pypi_libs/rfc3339-validator.json
sleep 1

echo "237/289: rfc3986-validator"
curl -s -L https://pypi.python.org/pypi/rfc3986-validator/json | jq > data/pypi_libs/rfc3986-validator.json
sleep 1

echo "238/289: rfc3987-syntax"
curl -s -L https://pypi.python.org/pypi/rfc3987-syntax/json | jq > data/pypi_libs/rfc3987-syntax.json
sleep 1

echo "239/289: rich"
curl -s -L https://pypi.python.org/pypi/rich/json | jq > data/pypi_libs/rich.json
sleep 1

echo "240/289: rich-rst"
curl -s -L https://pypi.python.org/pypi/rich-rst/json | jq > data/pypi_libs/rich-rst.json
sleep 1

echo "241/289: rich-toolkit"
curl -s -L https://pypi.python.org/pypi/rich-toolkit/json | jq > data/pypi_libs/rich-toolkit.json
sleep 1

echo "242/289: rignore"
curl -s -L https://pypi.python.org/pypi/rignore/json | jq > data/pypi_libs/rignore.json
sleep 1

echo "243/289: rpds-py"
curl -s -L https://pypi.python.org/pypi/rpds-py/json | jq > data/pypi_libs/rpds-py.json
sleep 1

echo "244/289: ruamel-yaml"
curl -s -L https://pypi.python.org/pypi/ruamel-yaml/json | jq > data/pypi_libs/ruamel-yaml.json
sleep 1

echo "245/289: send2trash"
curl -s -L https://pypi.python.org/pypi/send2trash/json | jq > data/pypi_libs/send2trash.json
sleep 1

echo "246/289: sentry-sdk"
curl -s -L https://pypi.python.org/pypi/sentry-sdk/json | jq > data/pypi_libs/sentry-sdk.json
sleep 1

echo "247/289: setuptools"
curl -s -L https://pypi.python.org/pypi/setuptools/json | jq > data/pypi_libs/setuptools.json
sleep 1

echo "248/289: shellingham"
curl -s -L https://pypi.python.org/pypi/shellingham/json | jq > data/pypi_libs/shellingham.json
sleep 1

echo "249/289: six"
curl -s -L https://pypi.python.org/pypi/six/json | jq > data/pypi_libs/six.json
sleep 1

echo "250/289: smmap"
curl -s -L https://pypi.python.org/pypi/smmap/json | jq > data/pypi_libs/smmap.json
sleep 1

echo "251/289: sniffio"
curl -s -L https://pypi.python.org/pypi/sniffio/json | jq > data/pypi_libs/sniffio.json
sleep 1

echo "252/289: sortedcontainers"
curl -s -L https://pypi.python.org/pypi/sortedcontainers/json | jq > data/pypi_libs/sortedcontainers.json
sleep 1

echo "253/289: soupsieve"
curl -s -L https://pypi.python.org/pypi/soupsieve/json | jq > data/pypi_libs/soupsieve.json
sleep 1

echo "254/289: sqlalchemy"
curl -s -L https://pypi.python.org/pypi/sqlalchemy/json | jq > data/pypi_libs/sqlalchemy.json
sleep 1

echo "255/289: sqlalchemy-utils"
curl -s -L https://pypi.python.org/pypi/sqlalchemy-utils/json | jq > data/pypi_libs/sqlalchemy-utils.json
sleep 1

echo "256/289: sse-starlette"
curl -s -L https://pypi.python.org/pypi/sse-starlette/json | jq > data/pypi_libs/sse-starlette.json
sleep 1

echo "257/289: stack-data"
curl -s -L https://pypi.python.org/pypi/stack-data/json | jq > data/pypi_libs/stack-data.json
sleep 1

echo "258/289: starlette"
curl -s -L https://pypi.python.org/pypi/starlette/json | jq > data/pypi_libs/starlette.json
sleep 1

echo "259/289: streamlit"
curl -s -L https://pypi.python.org/pypi/streamlit/json | jq > data/pypi_libs/streamlit.json
sleep 1

echo "260/289: tenacity"
curl -s -L https://pypi.python.org/pypi/tenacity/json | jq > data/pypi_libs/tenacity.json
sleep 1

echo "261/289: terminado"
curl -s -L https://pypi.python.org/pypi/terminado/json | jq > data/pypi_libs/terminado.json
sleep 1

echo "262/289: tiktoken"
curl -s -L https://pypi.python.org/pypi/tiktoken/json | jq > data/pypi_libs/tiktoken.json
sleep 1

echo "263/289: tinycss2"
curl -s -L https://pypi.python.org/pypi/tinycss2/json | jq > data/pypi_libs/tinycss2.json
sleep 1

echo "264/289: toml"
curl -s -L https://pypi.python.org/pypi/toml/json | jq > data/pypi_libs/toml.json
sleep 1

echo "265/289: tomlkit"
curl -s -L https://pypi.python.org/pypi/tomlkit/json | jq > data/pypi_libs/tomlkit.json
sleep 1

echo "266/289: toon-python"
curl -s -L https://pypi.python.org/pypi/toon-python/json | jq > data/pypi_libs/toon-python.json
sleep 1

echo "267/289: tornado"
curl -s -L https://pypi.python.org/pypi/tornado/json | jq > data/pypi_libs/tornado.json
sleep 1

echo "268/289: tqdm"
curl -s -L https://pypi.python.org/pypi/tqdm/json | jq > data/pypi_libs/tqdm.json
sleep 1

echo "269/289: traitlets"
curl -s -L https://pypi.python.org/pypi/traitlets/json | jq > data/pypi_libs/traitlets.json
sleep 1

echo "270/289: typer"
curl -s -L https://pypi.python.org/pypi/typer/json | jq > data/pypi_libs/typer.json
sleep 1

echo "271/289: typing-extensions"
curl -s -L https://pypi.python.org/pypi/typing-extensions/json | jq > data/pypi_libs/typing-extensions.json
sleep 1

echo "272/289: typing-inspection"
curl -s -L https://pypi.python.org/pypi/typing-inspection/json | jq > data/pypi_libs/typing-inspection.json
sleep 1

echo "273/289: tzdata"
curl -s -L https://pypi.python.org/pypi/tzdata/json | jq > data/pypi_libs/tzdata.json
sleep 1

echo "274/289: uri-template"
curl -s -L https://pypi.python.org/pypi/uri-template/json | jq > data/pypi_libs/uri-template.json
sleep 1

echo "275/289: urllib3"
curl -s -L https://pypi.python.org/pypi/urllib3/json | jq > data/pypi_libs/urllib3.json
sleep 1

echo "276/289: uvicorn"
curl -s -L https://pypi.python.org/pypi/uvicorn/json | jq > data/pypi_libs/uvicorn.json
sleep 1

echo "277/289: uvloop"
curl -s -L https://pypi.python.org/pypi/uvloop/json | jq > data/pypi_libs/uvloop.json
sleep 1

echo "278/289: watchdog"
curl -s -L https://pypi.python.org/pypi/watchdog/json | jq > data/pypi_libs/watchdog.json
sleep 1

echo "279/289: watchfiles"
curl -s -L https://pypi.python.org/pypi/watchfiles/json | jq > data/pypi_libs/watchfiles.json
sleep 1

echo "280/289: wcwidth"
curl -s -L https://pypi.python.org/pypi/wcwidth/json | jq > data/pypi_libs/wcwidth.json
sleep 1

echo "281/289: webcolors"
curl -s -L https://pypi.python.org/pypi/webcolors/json | jq > data/pypi_libs/webcolors.json
sleep 1

echo "282/289: webencodings"
curl -s -L https://pypi.python.org/pypi/webencodings/json | jq > data/pypi_libs/webencodings.json
sleep 1

echo "283/289: websocket-client"
curl -s -L https://pypi.python.org/pypi/websocket-client/json | jq > data/pypi_libs/websocket-client.json
sleep 1

echo "284/289: websockets"
curl -s -L https://pypi.python.org/pypi/websockets/json | jq > data/pypi_libs/websockets.json
sleep 1

echo "285/289: widgetsnbextension"
curl -s -L https://pypi.python.org/pypi/widgetsnbextension/json | jq > data/pypi_libs/widgetsnbextension.json
sleep 1

echo "286/289: wrapt"
curl -s -L https://pypi.python.org/pypi/wrapt/json | jq > data/pypi_libs/wrapt.json
sleep 1

echo "287/289: yarl"
curl -s -L https://pypi.python.org/pypi/yarl/json | jq > data/pypi_libs/yarl.json
sleep 1

echo "288/289: zero-to-ai"
curl -s -L https://pypi.python.org/pypi/zero-to-ai/json | jq > data/pypi_libs/zero-to-ai.json
sleep 1

echo "289/289: zipp"
curl -s -L https://pypi.python.org/pypi/zipp/json | jq > data/pypi_libs/zipp.json
sleep 1


