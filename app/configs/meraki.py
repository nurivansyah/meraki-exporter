import os

from dotenv import load_dotenv
from meraki import DashboardAPI

load_dotenv()

session = DashboardAPI(suppress_logging=True)
organization_id = os.getenv("ORGANIZATION_ID")

