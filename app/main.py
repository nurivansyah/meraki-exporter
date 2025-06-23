from fastapi import FastAPI
from handlers.metrics_handler import metrics_response
from services.ip_address_service import get_ip_public

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ip-address")
def ip_address():
    return get_ip_public()


@app.get("/metrics")
def metrics():
    return metrics_response()
