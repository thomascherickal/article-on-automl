from azureml.core import Workspace, Dataset, Experiment
from azureml.train.automl import AutoMLConfig

ws = Workspace.from_config()
dataset = Dataset.Tabular.from_delimited_files('https://your-storage-account.blob.core.windows.net/your-container/nvda_data.csv')

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

experiment = Experiment(ws, "NVDA-stock-prediction")
run = experiment.submit(automl_config, show_output=True)

best_run, fitted_model = run.get_output()
prediction = fitted_model.predict({'open': [280.5], 'high': [285.3], 'low': [279.8], 'volume': [50000000]})
print(f"Predicted closing price: {prediction[0]}")
