"""
Automatic Mail Alert: When Instance state is reached to Stopped

Step1: Create an IAM Service Role for Lambda Function → EC2, SNS

Step2: Create SNS Topic

Step3: Write Lambda Function

Step3: Define a trigger → CloudWatch Event Rules → Event Source: Event Pattern → Service Name: EC2, Event Type: EC2 Instance State-change Notification, Specific state(s): stopped, Specific instance Id(s) → Targets: Lambda function → Default, Matched event → Rule Details: name
"""
import json
import boto3

def lambda_handler(event, context):
	sns_client=boto3.client('sns', 'us-east-1')
	sns_client.publish(TargetArn=12345, Message="EC2 Stopped")