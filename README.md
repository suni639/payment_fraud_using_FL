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

```bash
pip install pandas numpy scikit-learn tensorflow