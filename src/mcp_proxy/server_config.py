from dataclasses import dataclass
from mcp.client.stdio import StdioServerParameters


@dataclass
class ServerConfig:
    """Configuration for a proxied server."""

    stdio_params: StdioServerParameters
    tools: list[str] | None = None
