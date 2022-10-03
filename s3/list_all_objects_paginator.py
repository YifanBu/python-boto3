import boto3

session = boto3.session.Session(profile_name='default')

s3_client = session.client(service_name="s3", region_name="us-east-1")

count = 1

bucket_name = 'my-angular-website-29-09-22'

paginator = s3_client.get_paginator('list_objects')
for each_page in paginator.paginate(Bucket=bucket_name):
    for each_object in each_page['Contents']:
      print(count, each_object['Key'])
      count=count+1