from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "endpoints": {
            "predict": "/predict (POST)",
            "predict-batch": "/predict-batch (POST)"
        }
    })

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["features"]
    prediction = model.predict([np.array(data)])
    return jsonify({"prediction": int(prediction[0])})

# NOVO ENDPOINT DE BATCH
@app.route("/predict-batch", methods=["POST"])
def predict_batch():
    # Espera receber um JSON com a chave "batch", contendo uma lista de registos
    data_batch = request.json["batch"]
    
    # O modelo do scikit-learn aceita matrizes 2D diretamente
    predictions = model.predict(data_batch)
    
    # Converte o array numpy do resultado de volta para uma lista de inteiros nativos do Python
    return jsonify({"predictions": [int(p) for p in predictions]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)