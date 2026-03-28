# Chat: Azure Cosmos DB Cursor plugin / MCP

## User request

`/add-plugin azure-cosmosdb`

## Assistant response (summary)

### Done

Global MCP config (`~/.cursor/mcp.json`) was updated to include the **Azure Cosmos DB** server entry from [AzureCosmosDB/cosmosdb-cursor-plugin](https://github.com/AzureCosmosDB/cosmosdb-cursor-plugin) (same as its `.mcp.json`), next to the existing `m26-mcp-server`:

- **`azure-cosmosdb`** — `url` `${COSMOSDB_MCP_SERVER_URL}/mcp` with `Authorization: Bearer ${COSMOSDB_MCP_JWT_TOKEN}`

### What `/add-plugin` is

That path is a **Cursor product** action (Marketplace / plugin install), not something the chat agent can run. To install the full plugin (rules + saved prompt + MCP wiring Cursor expects):

1. Open [Cursor Marketplace → Azure Cosmos DB](https://cursor.com/marketplace/azure-cosmos-db) and click **Install**, or search **“Azure Cosmos DB”** in the Marketplace panel.

Rules work as soon as the plugin is installed; they do not need MCP.

### For live DB tools (MCP)

The MCP block only works after you:

1. Deploy the [Azure Cosmos DB MCP Toolkit](https://github.com/AzureCosmosDB/MCPToolKit) (`azd up` or their README quick start).
2. Set environment variables **where Cursor inherits them** (e.g. shell profile or macOS `launchctl` for GUI apps), then restart Cursor:
   - `COSMOSDB_MCP_SERVER_URL` — toolkit base URL (no `/mcp`; the config appends `/mcp`).
   - `COSMOSDB_MCP_JWT_TOKEN` — short-lived token from `az account get-access-token` per the [plugin README](https://github.com/AzureCosmosDB/cosmosdb-cursor-plugin).

After a restart, use **Cursor Settings → Tools & MCP** to confirm `azure-cosmosdb` loads; approve/enable it if prompted.

If you want this project-only instead of global, the MCP entry can be moved to the workspace `.cursor/mcp.json` pattern Cursor supports for multi-root setups.

## References

- [Cursor Marketplace — Azure Cosmos DB](https://cursor.com/marketplace/azure-cosmos-db)
- [Introducing the Azure Cosmos DB Plugin for Cursor](https://devblogs.microsoft.com/cosmosdb/introducing-the-azure-cosmos-db-plugin-for-cursor/)
- [cosmosdb-cursor-plugin (GitHub)](https://github.com/AzureCosmosDB/cosmosdb-cursor-plugin)
- [MCPToolKit (GitHub)](https://github.com/AzureCosmosDB/MCPToolKit)
