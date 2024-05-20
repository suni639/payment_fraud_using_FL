# payment_fraud_using_FL
This project demonstrates the implementation of a decentralized federated learning model for fraud detection. The dataset is split across 20 clients, each of which trains a local model on their data. The models are then aggregated in a decentralized manner to form a global model.

## Project Structure
    ```css
    federated_learning_project/
    │
    ├── data_preparation.py
    ├── model_definition.py
    ├── local_training.py
    ├── aggregation.py
    ├── evaluation.py
    ├── utils.py
    ├── main.py
    ├── README.md
    ├── LICENSE
    ├── .gitignore
    └── requirements.txt

### Files Description

- **data_preparation.py**: Contains functions for loading, preprocessing, and splitting the dataset.
- **model_definition.py**: Defines the Keras model architecture.
- **local_training.py**: Implements local training logic for each client.
- **aggregation.py**: Contains the logic for decentralized aggregation of model updates.
- **evaluation.py**: Includes functions to evaluate the final aggregated model.
- **utils.py**: Provides utility functions such as setting up logging.
- **main.py**: The main script that integrates all modules and runs the federated learning process.
- **README.md**: This readme file.

## Installation

### Prerequisites

- Python 3.6 or higher
- Pip (Python package installer)

### Install Dependencies
    ```powershell
    pip install pandas numpy scikit-learn tensorflow

## Usage
- **Prepare the Dataset**: Ensure the fraud detection dataset is available at the specified filepath
- **Run the Federated Learning Process**: Execute the main.py script to start the federated learning process
    ```powershell
    python main.py

## Code Overview

### Data Preparation
The dataset is loaded, preprocessed (e.g., scaled), and split into parts for each client.
    ```python
    from data_preparation import load_and_preprocess_data, split_data

    # Load and preprocess the dataset
    features, labels = load_and_preprocess_data(r'C:\Users\sunil\OneDrive\Documents\Coding\Projects\payment_fraud_using_FL\payment_fraud_dataset.csv')

    # Split the dataset into parts for each client
    data_split = split_data(features, labels, num_clients=20)

### Model Definition
Defines the Keras model architecture used by each client.
   ```python
   from model_definition import create_keras_model

    input_shape = features.shape[1]
    model = create_keras_model(input_shape)

### Local Training
Each client trains its local model on its subset of data.
    ```python
    from local_training import local_train

    client_model = local_train(client_data, model)

### Aggregation
Aggregates the models from each client in a decentralized manner.
    ```python
    from aggregation import decentralized_aggregation

    client_models = decentralized_aggregation(client_models)

### Evaluation
Evaluates the final aggregated model on the full dataset.
    ```python
    from evaluation import evaluate_model

    evaluate_model(client_models[0], r'C:\Users\sunil\OneDrive\Documents\Coding\Projects\payment_fraud_using_FL\payment_fraud_dataset.csv')

### Contributions
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Instructions to Run the Project
1. Download or clone the repository to your local machine.
2. Navigate to the project directory in your terminal or PowerShell.
3. Install the required dependencies using the provided requirements.txt file:
    ```powershell
    pip install -r requirements.txt
4. Ensure the dataset is located at the specified path: C:\Users\sunil\OneDrive\Documents\Coding\Projects\payment_fraud_using_FL\payment_fraud_dataset.csv.
5. Run the main script to start the federated learning process:
    ```powershell
    python main.py