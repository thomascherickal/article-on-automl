import boto3
from sagemaker.automl.automl import AutoML

sagemaker_client = boto3.client('sagemaker')
auto_ml = AutoML(
role='your-sagemaker-role-arn',
target_attribute_name='close',
output_path='s3://your-bucket/output/',
problem_type='Regression',
max_candidates=10
)

auto_ml.fit(inputs='s3://your-bucket/nvda_data.csv', wait=True)

predictor = auto_ml.deploy(initial_instance_count=1, instance_type='ml.m5.large')
result = predictor.predict({'open': 280.5, 'high': 285.3, 'low': 279.8, 'volume': 50000000})
print(f"Predicted closing price: {result}")
