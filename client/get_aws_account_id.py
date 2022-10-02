import re
# Use STS to get AWS account info
import boto3
from pprint import pprint

aws_mag_con = boto3.session.Session(profile_name="default")

sts_con_client = aws_mag_con.client(service_name='sts', region_name='us-east-1')

response = sts_con_client.get_caller_identity()

pprint(response)