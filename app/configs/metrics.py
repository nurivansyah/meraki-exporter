from prometheus_client import Gauge, REGISTRY, PROCESS_COLLECTOR, GC_COLLECTOR, PLATFORM_COLLECTOR

ip_address = Gauge(
    'ip_address', 
    'Current IP Address Information for each network', 
    ['network', 'interface_name', 'interface_ip', 'public_ip']
)

REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.unregister(GC_COLLECTOR)
REGISTRY.unregister(PLATFORM_COLLECTOR)