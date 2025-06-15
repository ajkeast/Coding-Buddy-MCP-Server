from mcp.server.fastmcp import FastMCP
from tools.sql_tools import SQLTools

# Initialize the MCP server
mcp = FastMCP("CodingBuddy")

# Instantiate toolsets
sql_tools = SQLTools()

# Register SQL tools
mcp.tool()(sql_tools.list_databases)
mcp.tool()(sql_tools.list_tables)
mcp.tool()(sql_tools.execute_query)
mcp.tool()(sql_tools.get_table_schema)

# Run the server
if __name__ == "__main__":
    # The transport is the protocol used to communicate with the server.
    # In this case, we are using the standard input/output (stdio) protocol.
    # This is the default transport for MCP servers.
    # Other transports include HTTP, WebSocket, and TCP.
    mcp.run(transport="stdio")
