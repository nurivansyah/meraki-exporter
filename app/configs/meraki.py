from meraki import DashboardAPI
import os

session = DashboardAPI(suppress_logging=True)
organization_id = os.environ['ORGANIZATION_ID']