from sklearn.model_selection import train_test_split
import tensorflow as tf

def local_train(data, model):
    """Train the model on local client data."""
    try:
        features, labels = data[:, :-1], data[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2)
        model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))
        return model
    except Exception as e:
        print(f"Error during local training: {e}")
        return None
