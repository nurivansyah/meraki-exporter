from fastapi.responses import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from services.ip_address_service import get_ip_public
from configs.metrics import ip_address

def metrics_response():

    network_ips = get_ip_public()

    for nip in network_ips:

        value = 1
        if nip.interface_ip == None:
            value = 0

        ip_address.labels(
            network = nip.network,
            interface_name = nip.interface_name,
            interface_ip = nip.interface_ip,
            public_ip = nip.public_ip
        ).set(value)

    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)