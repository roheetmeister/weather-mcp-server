import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "weather.py"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")

            print("\n--- Testing get_alerts for CA ---")
            result = await session.call_tool("get_alerts", {"state": "CA"})
            print(result.content[0].text[:500])

            print("\n--- Testing get_forecast for NYC ---")
            result = await session.call_tool("get_forecast", {"latitude": 40.7128, "longitude": -74.0060})
            print(result.content[0].text[:500])


if __name__ == "__main__":
    asyncio.run(main())
