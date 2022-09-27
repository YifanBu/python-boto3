import boto3

aws_mag_con = boto3.session.Session(profile_name="default")

# iam, ec2 and s3 resource
iam_con_resource = aws_mag_con.resource(service_name='iam', region_name='us-east-1')
ec2_con_resource = aws_mag_con.resource(service_name='ec2', region_name='us-east-1')
s3_con_resource = aws_mag_con.resource(service_name='s3', region_name='us-east-1')

for each_user in iam_con_resource.users.all():
  print(each_user.name)

for each_instance in ec2_con_resource.instances.all():
  print(each_instance.name)

for each_bucket in s3_con_resource.buckets.all():
  print(each_bucket.name)
