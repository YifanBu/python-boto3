import boto3

session = boto3.session.Session(profile_name='default')

s3_resource = session.resource(service_name="s3", region_name="us-east-1")
for each_bucket in s3_resource.buckets.all():
  print(each_bucket.name)

s3_client = session.client(service_name="s3", region_name="us-east-1")
for each_bucket in s3_client.list_buckets().get('Buckets'):
  print(each_bucket.get('Name'))