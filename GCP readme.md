
# Google Cloud AutoML Tables for Stock Prediction

This script demonstrates using Google Cloud AutoML Tables to create a regression model for predicting stock closing prices.

## Importing Necessary Libraries

```python
from google.cloud import automl_v1beta1 as automl
```


This line imports the automl_v1beta1 library from Google Cloud AutoML. This library provides functions to interact with the AutoML Tables service, enabling you to create datasets, train models, and make predictions.

### Initializing AutoML Tables Client
```python
client = automl.TablesClient(project='your-project-id', region='us-central1')
```

This line initializes the AutoML Tables client. You need to provide your Google Cloud project ID and the region where you want to create your AutoML resources.

Replace 'your-project-id' with your actual Google Cloud project ID.

### Creating a Dataset
```python
dataset = client.create_dataset('NVDA_stock_prediction')
```

This line creates a dataset named 'NVDA_stock_prediction' in your AutoML Tables instance. This dataset will hold the data used for training the model.

### Importing Data into the Dataset
```python
client.import_data(dataset, {'gcs_source': {'input_uris': ['gs://your-bucket/nvda_data.csv']}})
```

This line imports data from a CSV file stored in a Google Cloud Storage (GCS) bucket into the created dataset.

* Replace 'gs://your-bucket/nvda_data.csv' with the actual GCS URI of your dataset.
### Training a Model

```python
model = client.create_model('NVDA_prediction_model', dataset=dataset, train_budget_milli_node_hours=1000)
model.wait()
```

This code block creates and trains a model named 'NVDA_prediction_model' using the data in the specified dataset.


```python
train_budget_milli_node_hours=1000 sets the training budget in milli-node hours. AutoML will stop training after consuming this budget or achieving satisfactory performance.
```

### Making a Prediction
```python
prediction = client.predict(model, {'open': 280.5, 'high': 285.3, 'low': 279.8, 'volume': 50000000})
print(f"Predicted closing price: {prediction.tables.value}")
```

* This code block uses the trained model to make a prediction on new data.
* The input data should have the same features as the training data.
* The predicted closing price is extracted from the prediction response and printed.

## Necessary Instructions to Make it Run on the Cloud

* Google Cloud Project: Ensure you have an active Google Cloud project with billing enabled.

* Enable AutoML API: Enable the AutoML Tables API for your project.

* Google Cloud Storage Bucket: Create a GCS bucket to store your dataset (nvda_data.csv).

* Upload Dataset: Upload your dataset to the GCS bucket.

* Authentication: Set up authentication for your environment to access Google Cloud services. This can be done using the Google Cloud SDK or service account credentials.

* Install Libraries: Install the necessary libraries:

```bash
pip install google-cloud-automl
```

* Update Script with Your Information:

Replace 'your-project-id' with your actual Google Cloud project ID.
Replace 'gs://your-bucket/nvda_data.csv' with the actual GCS URI of your dataset.

### Run the Script: 
Execute the script in an environment where the Google Cloud SDK is configured and authenticated.
