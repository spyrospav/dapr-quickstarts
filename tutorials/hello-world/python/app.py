import logging
import os
import uvicorn
from dapr.clients import DaprClient
from fastapi import FastAPI
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr_app = DaprApp(app)

DAPR_STORE_NAME = "statestore"
dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
port = os.getenv("APP_PORT", 3000)

logging.basicConfig(level = logging.INFO)

@app.get("/health")
def healthcheck():
    return "200"

@app.get('/order')
async def order():
    with DaprClient() as client:
        response = client.get_state(DAPR_STORE_NAME, key="orderId")
        return response

@app.post('/neworder', status_code=200)
async def neworder(order: dict):

    print(order)
    
    with DaprClient() as client:
        client.save_state(DAPR_STORE_NAME, key="orderId", value=order["ORDERID"])
        print(client.get_state(DAPR_STORE_NAME, key="orderId"))
        print("Persisted state successfully!")
        return client.get_state(DAPR_STORE_NAME, key="orderId")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=port)
