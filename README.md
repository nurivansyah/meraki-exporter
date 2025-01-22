# Meraki Exporter

This project is a custom exporter for Prometheus which will act as bridge to retrieve data from Cisco Meraki API.
More about Meraki-related please refer to the official documentation from Cisco.

To use this project you should prepare a Meraki Dashboard API Key and Organization ID which later needed to be set in the `.env` file and run following command:
```
uv sync
uv run --env-file .env fastapi dev app/main.py
```

Metrics available:
- `ip_address`: Current IP Address Information for each network
