# PowerShell script to deploy the M26 MCP Server to the Cursor IDE.
# Chris Joakim, 3Cloud/Cognizant, 2026

.\.venv\Scripts\Activate.ps1
python --version

$current_dir = (Get-Location).Path
$server_filename = Join-Path $current_dir "m26-mcp-server.py"
Write-Host "Current directory: $current_dir"
Write-Host "Server filename:   $server_filename"

fastmcp install cursor m26-mcp-server.py --project $server_filename
