# My Coding Buddy MCP Server

This is my personal MCP (Model Context Protocol) server that acts as my coding companion, helping me build better software faster. It connects to various coding clients and provides me with powerful tools to streamline my development workflow. By leveraging the Model Context Protocol, originally developed by Anthropic and adopted by major tech companies (Microsoft, xAI, Google, and OpenAI), I can interact with my codebase more efficiently and focus on building great software.

## Overview

This MCP server is my personal coding assistant that helps me:

- Save time by automating repetitive tasks
- Get instant access to my codebase and tools
- Make better coding decisions with AI assistance
- Focus on building features rather than setup
- Seamlessly integrate with my favorite development environments:
  - VS Code
  - Cursor
  - OpenAI Codex
  - Google Gemini
  - Claude Code
  - And other MCP-compatible clients

## Setup

1. Create and activate the virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1 # On Windows
   source venv/bin/activate # On macOS/Linux
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

MCP servers can be configured to run in various environments. Here's an example configuration for Cursor (which can be adapted for other clients):

```json
{
  "mcpServers": {
    "server-name": {
      "command": "python",
      "args": ["mcp-server.py"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

This configuration can be placed in:

- Project-specific: `.cursor/mcp.json` in your project directory
- Global: `~/.cursor/mcp.json` in your home directory

## Features

- My personal coding assistant that understands my workflow
- Tool integration for faster development
- Cross-platform compatibility
- Support for multiple coding clients
- Extensible architecture for custom tool development
- Flexible authentication options (API keys, OAuth)
- Project-specific and global configuration support

## Usage

My coding buddy automatically helps me by:

1. Understanding my project context and requirements
2. Providing relevant tools and suggestions when needed
3. Executing commands and managing my development environment
4. Showing me detailed responses and execution results
5. Learning from my preferences to provide better assistance

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues for feature requests and bug reports.

## Learn More

For more detailed information about the MCP protocol, visit the official MCP documentation.
