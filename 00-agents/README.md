# function calling

## function description
get_weather_tool = {
    "type": "function",
    "name": “get_weather”,
    "description": “get city temperature from known city“,
    "parameters": {
        "type": "object",
        "properties": {
            “city”: {
                "type": "string",
                "description": “city name”
            }
        },
        "required": [“city”],
        "additionalProperties": False
    }
}

set_weather_tool = {
    "type": "function",
    "name": “set_weather”,
    "description": “set city temperature for known city“,
    "parameters": {
        "type": "object",
        "properties": {
            “city”: {
                "type": "string",
                "description": “city name”
            },
			“temp”: {
				“type”: “float”,
				“description”: “known city temperature in celsius”
			},
        },
        "required": [“city”, “temp”],
        "additionalProperties": False
    }
}

## MCP
### start MCP server   
!pip install fastmcp   
call FastMCP in python main function   

Starting MCP server 'Demo 🚀' with transport 'stdio'   

### Protocol

{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_weather", "arguments": {"city": "Berlin"}}}
{"jsonrpc":"2.0","id":3,"result":{"content":[{"type":"text","text":"20.0"}],"structuredContent":{"result":20.0},"isError":false}}

### Client
CallToolResult(content=[TextContent(type='text', text='20.0', annotations=None, meta=None)], structured_content={'result': 20.0}, data=20.0, is_error=False)