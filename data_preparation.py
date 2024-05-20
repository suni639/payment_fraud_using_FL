import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

def load_and_preprocess_data(file_path):
    """Load and preprocess the dataset."""
    data = pd.read_csv(file_path)
    
    # Select features and labels
    features = data.drop('isFraud', axis=1)
    labels = data['isFraud'].values
    
    # One-hot encode categorical features
    features = pd.get_dummies(features, columns=['type', 'nameOrig', 'nameDest'])
    
    # Scale numerical features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)
    
    return features_scaled, labels

def split_data(features, labels, num_clients):
    """Split the dataset into `num_clients` parts."""
    data = np.hstack((features, labels.reshape(-1, 1)))
    np.random.shuffle(data)
    split_data = np.array_split(data, num_clients)
    return split_data
