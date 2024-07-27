# Azure AutoML for Stock Prediction

This script demonstrates how to use Azure AutoML for building a regression model to predict stock closing prices.

## Importing Necessary Libraries

```python
from azureml.core import Workspace, Dataset, Experiment
from azureml.train.automl import AutoMLConfig
```

azureml.core provides core functionalities for interacting with Azure Machine Learning. This includes managing workspaces, datasets, experiments, and more.

AutoMLConfig from azureml.train.automl is a configuration object used to define the settings for an AutoML experiment. This object allows you to specify the task, data, metrics, and other parameters for the automated 
machine learning process.

### Connecting to Azure Machine Learning Workspace
```python
ws = Workspace.from_config()
```

This line connects to your Azure Machine Learning workspace. The from_config() function reads the configuration from the config.json file, which should be present in the same directory as your script or notebook. This file contains the details of your workspace, such as subscription ID, resource group, and workspace name.

### Loading and Preparing Data

```python
dataset = Dataset.Tabular.from_delimited_files('https://your-storage-account.blob.core.windows.net/your-container/nvda_data.csv')
```

This line loads the dataset from a CSV file stored in an Azure Blob Storage container. The Dataset.Tabular.from_delimited_files() function is used to load tabular data from various sources, including local files and cloud storage.

Replace "https://your-storage-account.blob.core.windows.net/your-container/nvda_data.csv" with the actual URL of your dataset in Azure Blob Storage.

### Configuring AutoML Experiment

```python
automl_config = AutoMLConfig(
task='regression',
primary_metric='normalized_root_mean_squared_error',
training_data=dataset,
label_column_name='close',
n_cross_validations=5,
max_concurrent_iterations=4,
iterations=10,
experiment_timeout_minutes=60
)
```

* task: Specifies the type of machine learning problem. In this case, it's 'regression' as we're predicting a continuous value (stock closing price).
* primary_metric: Defines the primary metric to evaluate models. Here, it's 'normalized_root_mean_squared_error', a common metric for regression tasks.
* training_data: Points to the dataset to be used for training. This is the dataset object we created earlier.
* label_column_name: Specifies the column in the dataset containing the target variable (the value we're predicting), which is 'close' in this case.
* n_cross_validations: Sets the number of cross-validation folds to use. Cross-validation helps assess the model's performance on unseen data.
* max_concurrent_iterations: Limits the maximum number of iterations (model training runs) to execute in parallel.
* iterations: Specifies the total number of iterations to run. AutoML will try different algorithms and hyperparameters during these iterations.
* experiment_timeout_minutes: Sets a time limit for the experiment.

### Running the AutoML Experiment

```python
experiment = Experiment(ws, "NVDA-stock-prediction")
run = experiment.submit(automl_config, show_output=True)
```

Creates an Experiment object to track the AutoML run. This helps organize and manage multiple experiments within your workspace.

Submits the AutoML experiment for execution. The show_output=True argument displays the training progress and logs.

### Retrieving the Best Model and Making Predictions

```python
best_run, fitted_model = run.get_output()
prediction = fitted_model.predict({'open': [280.5], 'high': [285.3], 'low': [279.8], 'volume': [50000000]})
print(f"Predicted closing price: {prediction[0]}")
```

Retrieves the best-performing model from the experiment. AutoML automatically selects the model with the highest score based on the primary_metric.

Uses the best model to make predictions on new data. The input data should have the same features as the training data.

Prints the predicted closing price.

## Necessary Instructions to Make it Run on the Cloud

* Azure Subscription: Ensure you have an active Azure subscription.

* Azure Machine Learning Workspace: Create an Azure Machine Learning workspace in your subscription. This workspace provides the environment and resources for running machine learning experiments.

* Compute Resources: Set up compute resources (e.g., Azure Machine Learning Compute Instance, Compute Cluster) within your workspace. These resources provide the computational power for training and deploying models.

* Data Storage: Upload your dataset (nvda_data.csv) to an Azure Blob Storage container. Make sure the storage account and container are accessible from your workspace.

### Environment Setup:

### Install the Azure Machine Learning SDK:
```bash 
pip install azureml-core azureml-train-automl
```

Configure your development environment to connect to your Azure Machine Learning workspace. This typically involves setting up authentication using the Azure CLI or creating a service principal.

### Update Script with Your Information:

* Replace "https://your-storage-account.blob.core.windows.net/your-container/nvda_data.csv" with the actual URL of your dataset.
* Ensure that your config.json file contains the correct details for your Azure Machine Learning workspace.

### Run the Script: 

Execute the script in an environment connected to your Azure Machine Learning workspace. This could be a Jupyter notebook running in an Azure Machine Learning Compute Instance, a Python script executed on a Compute Cluster, or your local machine with the Azure ML SDK configured.
