import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Define the expected order of features
EXPECTED_FEATURES = [
    "network_packet_size",
    "login_attempts",
    "session_duration",
    "ip_reputation_score",
    "failed_logins",
    "unusual_time_access"
    # 🔁 Add more if your model used more features
]

# Create and fit a dummy scaler (you should ideally save/load the real one)
scaler = StandardScaler()

# Dummy fit to get shape (you'll override this if you have the real scaler saved)
scaler.fit(np.zeros((10, len(EXPECTED_FEATURES))))  # dummy fit to prevent crash

def preprocess_input(data):
    """
    Takes a dictionary from the frontend and returns a scaled NumPy array.

    Parameters:
    - data: dict {feature_name: value}

    Returns:
    - scaled: numpy array shape (1, n_features)
    """
    try:
        # Ensure all required features are present
        input_vector = [float(data[feature]) for feature in EXPECTED_FEATURES]
        input_array = np.array(input_vector).reshape(1, -1)
        scaled = scaler.transform(input_array)
        return scaled
    except Exception as e:
        raise ValueError(f"Invalid input or missing features: {e}")
