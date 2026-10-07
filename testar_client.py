import requests
import json

features = [5.1, 3.5, 1.4, 0.2]
response = requests.post("http://localhost:8000/predict", json= {"features": features})
print(response.status_code)
print(response.text)

