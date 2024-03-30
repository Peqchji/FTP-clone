def to_ip_comma(ip: str, port: int):
    ip_comma = ip.replace(".", ",")
    port_comma = f"{port//256:d},{port%256:d}"
    return ip_comma + "," + port_comma