import requests

data_in = {
            "TV": 12,
            "Radio": 42,
            "Newspaper": 12.8
        }

#y = requests.get("http://127.0.0.1:5000/prediction", json= data_in)
y = requests.get("http://localhost:5000/prediction", json= data_in)
print(y.status_code)
print(y.json()["Prediction:"])


# SHOULD PRINT
#200
#11.624140288748038