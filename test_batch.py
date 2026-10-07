import requests

# Um "batch" de 3 registos diferentes para classificar em simultâneo
payload = {
    "batch": [
        [5.1, 3.5, 1.4, 0.2],  # Registo 1
        [6.7, 3.0, 5.2, 2.3],  # Registo 2
        [5.9, 3.0, 5.1, 1.8]   # Registo 3
}

response = requests.post("http://localhost:8000/predict-batch", json=payload)

print(f"Status: {response.status_code}")
print(f"Previsões em Lote: {response.json()}")