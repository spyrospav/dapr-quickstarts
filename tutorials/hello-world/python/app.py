import logging
from dapr.clients import DaprClient
from fastapi import FastAPI, Body
from fastapi.encoders import jsonable_encoder

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
def neworder(order: dict):

    print(order)
    
    with DaprClient() as client:
        client.save_state(DAPR_STORE_NAME, key="orderId", value=order["orderId"])
        print("Persisted state successfully!")
        return 
