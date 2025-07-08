from prometheus_client import (
    GC_COLLECTOR,
    PLATFORM_COLLECTOR,
    PROCESS_COLLECTOR,
    REGISTRY,
    Gauge,
)

ip_address = Gauge(
    "ip_address",
    "Current IP Address Information for each network",
    ["network", "interface_name", "interface_ip", "public_ip"],
)

interface_ip_address = Gauge(
    "interface_ip_address",
    "Current IP address of each WAN Interface",
    ["network", "interface_name"],
)

interface_ip_address_public = Gauge(
    "interface_ip_address_public",
    "Current Public IP address of each WAN Interface",
    ["network", "interface_name"],
)

REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(GC_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)

