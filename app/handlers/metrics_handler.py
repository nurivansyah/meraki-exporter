from fastapi.responses import Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from app.configs.metrics import (
    interface_ip_address,
    interface_ip_address_public,
    ip_address,
)
from app.services.ip_address_service import get_ip_public, ip_to_integer


def metrics_response():
    network_ips = get_ip_public()

    for nip in network_ips:
        value = 1
        if nip.interface_ip is not None:
            interface_ip_address.labels(
                network=nip.network, interface_name=nip.interface_name
            ).set(ip_to_integer(nip.interface_ip))
        else:
            value = 0

        if nip.public_ip is not None:
            interface_ip_address_public.labels(
                network=nip.network, interface_name=nip.interface_name
            ).set(ip_to_integer(nip.public_ip))

        ip_address.labels(
            network=nip.network,
            interface_name=nip.interface_name,
            interface_ip=nip.interface_ip,
            public_ip=nip.public_ip,
        ).set(value)

    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
