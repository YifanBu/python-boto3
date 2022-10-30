"""
Automate Copy of EBS Snapshots between Regions

For Disaster Recovery Purpose:  back up data and log files across different geographical locations at regular intervals to minimize data loss and recovery time.
"""
import boto3
from pprint import pprint

source_region='us-east-1'
dest_region='us-east-2'

session=boto3.session.Session(profile_name="default")
ec2_source_client=session.client(service_name="ec2",region_name=source_region)
sts_client = session.client(service_name='sts',region_name="us-east-1")
account_id=sts_client.get_caller_identity().get('Account')
bkp_snap=[]
f_bkp={"Name":"tag:backup","Values":['yes']}
for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[accountid],Filters=[f_bkp]).get('Snapshots')):
	bkp_snap.append(each_snap.get('SnapshotId'))

ec2_dest_client=session.client(service_name="ec2",region_name=dest_region)

for each_source_snapid in bkp_snap:
	print("Taking backup for id of {} into a {}".format(each_source_snapid, dest_region))
	ec2_dest_client.copy_snapshot(
		Description='Disaster Recovery',
		SourceRegion=source_region,
    SourceSnapshotId=each_source_snapid,
	)

print("EBS Snapshot copy to desitination region is completed")
for each_source_snapid in bkp_snap:
	print("Deleting old tags for {}".format(each_source_snapid))
	ec2_source_client.delete_tags(
		Resources=[each_source_snapid],
		Tags=[
		{
		'Key':'backup',
		'Value': 'yes'
		}
		]
	)
	print("Creating new tags for {}".format(each_source_snapid))
	ec2_source_client.create_tags(
		Resources=[each_source_snapid],
		Tags=[
		{
		'Key':'backup',
		'Value': 'completed'
		}
		]
	)