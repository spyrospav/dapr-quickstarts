import logging
import requests
import sys
import os
from dapr.clients import DaprClient
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Order(BaseModel):
    orderId: str

DAPR_STORE_NAME = "statestore"
logging.basicConfig(level = logging.INFO)

app = FastAPI()

@app.get("/health")
def healthcheck():
    return "200"

@app.get('/order')
def order():
    with DaprClient() as client:
        response = client.get_state(DAPR_STORE_NAME, key="orderId")
        return response

@app.post('/neworder', status_code=200)
def neworder(order: Order):

    _order = jsonable_encoder(order)
    print("Got a new order! Order ID: {}".format(_order["orderId"]))

    with DaprClient() as client:
        response = client.save_state(DAPR_STORE_NAME, key="orderId", value=_order["orderId"])
        print("Persisted state successfully!")
        return 
