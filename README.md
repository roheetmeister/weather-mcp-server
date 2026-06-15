# Weather MCP Server

A Model Context Protocol (MCP) server that exposes real-time US weather data to AI assistants. Built with FastMCP (Python) and powered by the National Weather Service (NWS) public API.

## What We Built

An MCP server with two tools that any MCP-compatible AI client can call:

| Tool | Description | Input |
|------|-------------|-------|
| `get_alerts` | Active weather alerts for a US state | Two-letter state code (e.g. `CA`, `NY`) |
| `get_forecast` | 5-period weather forecast for a location | `latitude`, `longitude` (floats) |

Both tools hit the free, no-auth-required `api.weather.gov` API and return human-readable text.

## What We Were Achieving

The goal was to learn how to build an MCP server from scratch — the standard protocol that lets AI models (Claude, etc.) call external tools and data sources. This project demonstrates:

- **How to expose functions as MCP tools** using the `@mcp.tool()` decorator with FastMCP
- **How to connect an MCP server to a real external API** (NWS) with async HTTP calls
- **How to test an MCP server without Claude for Desktop** — using the MCP Inspector UI and a Python test client

## Project Structure

```
weather/
├── weather.py        # MCP server — tool definitions and NWS API calls
├── test_server.py    # Python test client — calls tools programmatically
├── .mcp.json         # Claude Code config — registers this server locally
├── pyproject.toml    # uv project config and dependencies
└── .python-version   # Python version pin
```

## How to Run

### Start the server (stdio mode)
```bash
uv run weather.py
```

### Test with the MCP Inspector (browser UI)
```bash
npx @modelcontextprotocol/inspector uv run weather.py
```
Open the printed URL (e.g. `http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=...`) and use the Tools tab to call tools interactively.

### Test with the Python client
```bash
uv run test_server.py
```
Lists available tools, then calls `get_alerts` for California and `get_forecast` for New York City.

### Use inside Claude Code
A `.mcp.json` is included. Restart Claude Code from this directory and the `weather` server will be available as a tool in conversation.

## Dependencies

- [`mcp[cli]`](https://github.com/modelcontextprotocol/python-sdk) — FastMCP server framework and client
- [`httpx`](https://www.python-httpx.org/) — async HTTP client for NWS API calls
