import profile
import re
from urllib import response
import boto3

aws_mag_con = boto3.session.Session(profile_name="default")

# iam, ec2 and s3 client
iam_con_client = aws_mag_con.client(service_name="iam", region_name="us-east-1")
ec2_con_client = aws_mag_con.client(service_name="ec2", region_name="us-east-1")
s3_con_client = aws_mag_con.client(service_name="s3", region_name="us-east-1")

# list iam users
response_iam = iam_con_client.list_users()
for each_item in response_iam['Users']:
  print(each_item['UserName'])

# describe ec2 instance ids
response_ec2 = ec2_con_client.describe_instances()
for each_item in response_ec2['Reservations']:
  for each_instance in each_item['Instances']:
    print(each_instance['InstanceId'])