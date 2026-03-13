"""
FastMCP 2 Client program for the m26-mcp/server.py
Chris Joakim, 3Cloud/Cognizant, 2026

This client connects to the MCP server and invokes all available endpoints:
- All tools (9 tools)
- All resources (2 resources)
"""

import asyncio
import json
import os
from fastmcp import Client

# HTTP server URL - matches server.py default port 8000
SERVER_URL = "http://127.0.0.1:8157/mcp"
client = Client(SERVER_URL)


async def invoke_tools():
    """Invoke all available tools from the server."""
    print("\n" + "=" * 80)
    print("INVOKING TOOLS")
    print("=" * 80)

    # 1. miles_to_kilometers
    print("\n1. miles_to_kilometers(10.0):")
    result = await client.call_tool("miles_to_kilometers", {"miles": 10.0})
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")

    # 2. miles_to_yards
    print("\n2. miles_to_yards(10.0):")
    result = await client.call_tool("miles_to_yards", {"miles": 10.0})
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")

    # 3. kilometers_to_miles
    print("\n3. kilometers_to_miles(10.0):")
    result = await client.call_tool("kilometers_to_miles", {"kilometers": 10.0})
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")

    # 4. kilometers_to_yards
    print("\n4. kilometers_to_yards(10.0):")
    result = await client.call_tool("kilometers_to_yards", {"kilometers": 10.0})
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")

    # 5. hhmmss_to_seconds
    print("\n5. hhmmss_to_seconds('01:01:01'):")
    result = await client.call_tool("hhmmss_to_seconds", {"hhmmss": "01:01:01"})
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")

    # 6. hhmmss_to_hours
    print("\n6. hhmmss_to_hours('01:01:01'):")
    result = await client.call_tool("hhmmss_to_hours", {"hhmmss": "01:01:01"})
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")

    # 7. calculate_speed
    print(
        "\n7. calculate_speed(distance_value=26.2, distance_unit='m', elapsed_time_hhmmss='3:47:30'):"
    )
    result = await client.call_tool(
        "calculate_speed",
        {"distance_value": 26.2, "distance_unit": "m", "elapsed_time_hhmmss": "3:47:30"},
    )
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")
    #write_json_file("tmp/calculate_speed.json", result.data)

    # 8. calculate_age
    print("\n8. calculate_age('1960-10-01', '2025-10-01'):")
    result = await client.call_tool(
        "calculate_age", {"yyyy_mm_dd_1": "1960-10-01", "yyyy_mm_dd_2": "2025-10-01"}
    )
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")
    write_json_file("tmp/calculate_age.json", result.data)

    # 9. calculate_run_walk
    print(
        "\n9. calculate_run_walk(run_hhmmss='2:30', run_ppm='9:16', walk_hhmmss='0:45', walk_ppm='17:00', miles=31.0):"
    )
    result = await client.call_tool(
        "calculate_run_walk",
        {
            "run_hhmmss": "2:30",
            "run_ppm": "9:16",
            "walk_hhmmss": "0:45",
            "walk_ppm": "17:00",
            "miles": 31.0,
        },
    )
    print(f"   Result: {result}")
    print(f"   Data:   {result.data}")
    #write_json_file("tmp/calculate_run_walk.json", result.data)


async def access_resources():
    """Access all available resources from the server."""
    print("\n" + "=" * 80)
    print("ACCESSING RESOURCES")
    print("=" * 80)

    # 1. health://status
    print("\n1. Reading resource 'health://status':")
    try:
        result = await client.read_resource("health://status")
        print(f"   Result: {result}")
        print(f"   Text:   {result[0].text}")
        write_json_file("tmp/health-status.json", json.loads(result[0].text))
    except Exception as e:
        print(f"   Error: {e}")

    # 2. server://info
    print("\n2. Reading resource 'server://info':")
    try:
        result = await client.read_resource("server://info")
        print(f"   Result: {result}")
        print(f"   Text:   {result[0].text}")
        write_json_file("tmp/server-info.json", json.loads(result[0].text))
    except Exception as e:
        print(f"   Error: {e}")


async def list_server_capabilities():
    """List all server capabilities (tools, resources, prompts)."""
    print("\n" + "=" * 80)
    print("SERVER CAPABILITIES")
    print("=" * 80)

    print("\nPinging the server:")
    ping_result = await client.ping()
    print(f"   Ping: {ping_result}")

    print("\nListing available tools:")
    tools = await client.list_tools()
    print(f"   Found {len(tools)} tools:")
    for tool in tools:
        print(f"      - {tool.name}: {tool.description}")

    print("\nListing available resources:")
    resources = await client.list_resources()
    print(f"   Found {len(resources)} resources:")
    for resource in resources:
        print(f"      - {resource.uri}: {resource.name if hasattr(resource, 'name') else 'N/A'}")

    print("\nListing available prompts:")
    prompts = await client.list_prompts()
    print(f"   Found {len(prompts)} prompts:")
    for prompt in prompts:
        print(f"      - {prompt.name if hasattr(prompt, 'name') else prompt}")


async def main():
    """Main function to run all client operations."""
    print("=" * 80)
    print("FastMCP 2 Client for m26-mcp/server.py")
    print("=" * 80)
    print(f"Connecting to server at: {SERVER_URL}")

    async with client:
        # First, list server capabilities
        await list_server_capabilities()

        # Access all resources
        await access_resources()

        # Invoke all tools
        await invoke_tools()

        print("\n" + "=" * 80)
        print("CLIENT EXECUTION COMPLETE")
        print("=" * 80)


def write_json_file(filename: str, data):
    if data is not None:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)


if __name__ == "__main__":
    print(f"Starting client: {os.path.basename(__file__)}")
    asyncio.run(main())
