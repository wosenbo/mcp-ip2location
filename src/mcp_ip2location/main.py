from pathlib import Path
from pydantic import Field
from mcp.server.fastmcp import FastMCP
from qqwry import QQwry

mcp = FastMCP("IP2Location Server")


@mcp.tool()
def lookup_ip(
    ip_addresses: list[str] = Field(..., description="IP addresses to lookup"),
):
    data_file = Path(__file__).parent / "data" / "qqwry.dat"
    q = QQwry()
    q.load_file(str(data_file))
    locations = []
    for ip_address in ip_addresses:
        res = q.lookup(ip_address)
        if res and len(res) == 2:
            location = f"{res[0]} {res[1]}"
        else:
            location = "未知"
        locations.append(location)
    return locations


def main():
    mcp.run()


if __name__ == "__main__":
    main()
