
from pydantic import BaseModel, IPvAnyAddress
from typing import List
from configs.meraki import session, organization_id

class UplinkIPAddress(BaseModel):
    network: str
    interface_name: str
    interface_ip: IPvAnyAddress|None
    public_ip: IPvAnyAddress|None

def get_ip_public():
    ip_address_list: List[UplinkIPAddress] = []
    
    network = {net["id"]: net["name"] for net in session.organizations.getOrganizationNetworks(
        organization_id, 
        total_pages='all'
    )}

    appliances = session.appliance.getOrganizationApplianceUplinkStatuses(
        organization_id, 
        total_pages='all'
    )

    for device in appliances:
        network_name = f'{network[device["networkId"]]}'

        for uplink in device["uplinks"]:
            ip_address_list.append(
                UplinkIPAddress(
                    network=network_name,
                    interface_name=uplink["interface"],
                    interface_ip=uplink["ip"],
                    public_ip=uplink["publicIp"]
                )
            )
        
    return ip_address_list