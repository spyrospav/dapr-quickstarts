## Installation of FastAPI

To install fastAPI we need both fastAPI and uvicorn:
```sh
python3 -m pip install fastapi "uvicorn[standard]"
```

## Run the Python app with Dapr

Open a new terminal and run:

```sh
dapr run --app-id app --app-port 3000 --dapr-http-port 3501 python3 app.py --config ./components/config.yaml --components-path ./components/
```

## Post messages to the service

You can send requests to the service by running the following:

```sh
curl -X POST -s http://localhost:3501/neworder -H "Content-Type: application/json" -H "dapr-app-id: pythonapp" -d @sample.json
```

You can also run the publisher Python app by running the following command in a new terminal:

```sh
dapr run --app-id pythonapp python3 publisher.py --config ./components/config.yaml --components-path ./components/
```

which posts a new `orderId` every second.

## Retrieve state

You can retrieve the state by accessing the `order` endpoint by simply running:

```sh
curl -X GET -s http://localhost:3501/order -H "Content-Type: application/json" -H "dapr-app-id: pythonapp"
```