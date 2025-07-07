from flask import Flask, render_template, request, jsonify
import numpy as np
from utils.preprocess import preprocess_input
from model.predict_logistic import predict_logistic

app = Flask(__name__)

# Load weights and bias from saved/ folder
weights = np.load('saved/logistic_weights.npy')
bias = np.load('saved/logistic_bias.npy')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json  # Get data from frontend
        features = preprocess_input(data)  # Preprocess into proper array
        prediction = predict_logistic(features, weights, bias)  # Predict (0 or 1)

        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
