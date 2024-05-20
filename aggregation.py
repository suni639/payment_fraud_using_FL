import numpy as np

def average_weights(models):
    """Average the weights of the models."""
    new_weights = list()
    for weights in zip(*[model.get_weights() for model in models]):
        new_weights.append(np.mean(weights, axis=0))
    return new_weights

def decentralized_aggregation(client_models):
    """Aggregate client models in a decentralized manner."""
    try:
        new_weights = average_weights(client_models)
        for model in client_models:
            model.set_weights(new_weights)
        return client_models
    except Exception as e:
        print(f"Error during aggregation: {e}")
        return client_models
