
# CUSTOM_LOGISTICREGRESSION_MODEL_AI

This project is a complete end-to-end AI-powered Cybersecurity Intrusion Detection System built using a custom implementation of Logistic Regression in pure NumPy, without using high-level machine learning libraries like PyTorch or scikit-learn for modeling. It includes:

- A fully functioning backend using Flask
- A clean HTML/CSS/JS frontend for user interaction
- A trained binary classifier for detecting network intrusions
- Preprocessing pipeline
- Live prediction interface

## Dataset

The dataset used is the Cybersecurity Intrusion Detection Dataset from Kaggle:

Dataset Link on Kaggle: https://www.kaggle.com/datasets/aungpyaeap/cybersecurity-intrusion-detection-dataset  
Filename: `cybersecurity_intrusion_data.csv`

## Objective

To detect whether a given session or user behavior is part of a cyber attack (binary classification: 0 = Normal, 1 = Attack), based on extracted behavioral features.

## Model Technique

A custom logistic regression model was implemented from scratch using the following:

- NumPy
- Sigmoid activation function
- Gradient descent (with configurable learning rate and iterations)
- Manual normalization using StandardScaler
- Prediction using: sigmoid(np.dot(X, weights) + bias)

No LogisticRegression from scikit-learn or high-level PyTorch/TensorFlow was used.

## Features (Columns Used)

The following columns were selected and used for training and prediction:

1. network_packet_size
2. login_attempts
3. session_duration
4. ip_reputation_score
5. failed_logins
6. unusual_time_access (binary: 0 = normal time, 1 = odd hour access)

## Architecture

- app.py: Main Flask backend, handles routing and prediction API
- model/predict_logistic.py: Handles math behind logistic regression inference
- utils/preprocess.py: Normalizes and arranges features
- static/: Contains CSS and JavaScript files
- templates/: Contains index.html for user interaction
- saved/: Stores trained weights and bias (logistic_weights.npy, logistic_bias.npy)

## Model Evaluation Metrics

After training on the dataset and testing on a validation split, the following results were observed:

- Accuracy: 0.7366
- Precision: 0.7179
- Recall: 0.6721
- F1 Score: 0.6943

## Running the Application

### 1. Clone the repository

```
git clone https://github.com/Ahmadjamil888/CUSTOM_LOGISTIC_REGRESSION_AI_MODEL_CYBER_THREATS.git
cd cyber-defense-app
```

### 2. (Optional) Create virtual environment

```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install requirements

```
pip install pandas
pip install numpy
pip install sklearn
pip install matplotlib.pyplot
```

### 4. Start the Flask server

```
python app.py
```

### 5. Open your browser

Visit: http://127.0.0.1:5000/  
Fill the form to test whether a session is classified as normal or an intrusion.

## File Structure

```
CUSTOM_LOGISTICREGRESSION_MODEL_AI/
├── app.py
├── model/
│   └── predict_logistic.py
├── utils/
│   └── preprocess.py
├── saved/
│   ├── logistic_weights.npy
│   └── logistic_bias.npy
├── static/
│   ├── css/style.css
│   └── js/main.js
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## Note

This project uses a simplified subset of features. For production-level use, additional anomaly detection, session logging, protocol analysis, and richer feature engineering are recommended.

## License

This project is released under the MIT License.
