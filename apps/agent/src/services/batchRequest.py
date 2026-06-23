import requests

def sendBatch(batch):
    response = requests.post(
        "http://localhost:3000/event/batch",
        json=batch
    )
    print(response.status_code)