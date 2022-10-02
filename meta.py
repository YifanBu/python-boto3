# list all regions for ec2
import boto3
aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_re=aws_mag_con.resource(service_name="ec2")

for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
	print(each_item['RegionName'])