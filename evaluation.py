import pandas as pd
from sklearn.preprocessing import StandardScaler
import tensorflow as tf

def evaluate_model(model, file_path):
    """Evaluate the aggregated model."""
    try:
        data = pd.read_csv(file_path)
        # Select features and labels
        features = data.drop('isFraud', axis=1)
        labels = data['isFraud'].values
        
        # One-hot encode categorical features
        features = pd.get_dummies(features, columns=['type', 'nameOrig', 'nameDest'])
        
        # Scale numerical features
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)
        
        loss, accuracy = model.evaluate(features_scaled, labels)
        print(f'Final model accuracy: {accuracy}')
        return accuracy
    except Exception as e:
        print(f"Error during evaluation: {e}")
        return None
