"""
Automating the start and stop EC2 Instances for Test Environment

1. Start EC2 Instances at 8 am Mon-Fri
2. Stop EC2 Instances at 5 pm Mon-Fri

Step1: Create an IAM Service Role for Lambda Function → Lambda: Allow Lambda functions to call AWS services on your behalf → AmazonEC2FullAccess

Step2: Write Lambda Function

Step3: Define a trigger → Schedule the job → CloudWatch Event Rules → Event Source: Schedule → Cron Expression: `0 8 ? * MON-FRI *` → Targets: Lambda function → Default, Matched event → Rule Details: name
"""
import json
import boto3

def lambda_handler(event, context):
	ec2_con_re=boto3.resource(service_name="ec2", region_name="us-east-1")
	test_env_filter={"Name": "tag:Env", "Values": ["Test"]}
	for each_in in ec2_con_re.instances.filter(Filters=[test_env_filter]):
		each_in.start()
	return "Success"