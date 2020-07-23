import adc

def measure():
    mcp = adc.MCP3208()
    ch = 0
    res = mcp.get(ch)
    print(f"{res} V")

if __name__ == "__main__":
    measure()