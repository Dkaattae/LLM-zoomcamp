from fastmcp import Client
import asyncio

async def main():
    async with Client("weather_server.py") as mcp_client:
        response = await mcp_client.call_tool("get_weather", {"city": "Berlin"})
        print(response)

if __name__ == "__main__":
    test = asyncio.run(main())