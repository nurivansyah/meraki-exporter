from fastapi import FastAPI
from services.ip_address_service import get_ip_public

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/ip-address")
def ip_address():
    return get_ip_public()
