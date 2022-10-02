import boto3
import datetime

aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli = aws_mag_con.client(service_name="ec2",region_name="us-east-1")
sts_con_cli=aws_mag_con.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
my_own_id=response.get('Account')
today = datetime.datetime.now()

start_time = str(datetime.datetime(today.year, today.month, today.day, 4, 15, 44))
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
	if each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")==start_time:
		print each_snap.id, each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")