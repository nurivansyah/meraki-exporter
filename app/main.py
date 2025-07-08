from fastapi import FastAPI

from app.handlers.metrics_handler import metrics_response
from app.services.ip_address_service import get_ip_public

api = FastAPI()


@api.get("/")
def read_root():
    return {"Hello": "World"}


@api.get("/ip-address")
def ip_address():
    return get_ip_public()


@api.get("/metrics")
def metrics():
    return metrics_response()
