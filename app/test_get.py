import requests

data_in = {
            "TV": 12,
            "Radio": 42,
            "Newspaper": 12.8
        }
y = requests.get("http://127.0.0.1:5000/prediction", json= data_in)
print(y.status_code)
print(y.json()["Prediction:"])