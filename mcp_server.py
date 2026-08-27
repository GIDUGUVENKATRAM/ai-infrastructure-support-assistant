from mcp.server import MCPServer

mcp = MCPServer("fde-support-mcp")


@mcp.tool()
def check_vdi_health(server_name: str) -> str:
    """
    Return simulated health information for a VDI server.
    """
    return (
        f"Server: {server_name}\n"
        "CPU: 94%\n"
        "Memory: 72%\n"
        "Active sessions: 18\n"
        "Status: High CPU detected"
    )


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8001,
        stateless_http=True,
        json_response=True
    )