"""
Assigning Secondary IP of Master to Slave when Master down

Define a trigger → CloudWatch Event Rules → Event Source: Event Pattern → Service Name: EC2, Event Type: EC2 Instance State-change Notification, Any state: stopped, Specific instance Id(s) → Targets: Lambda function → Default, Matched event → Rule Details: name
"""
import json
import boto3

def lambda_handler(event , context):
	master_id=""
	slave_id-""
	secondary_ip=""
	ec2_resource=boto3.resource('ec2','us-east-1')
	primary_instance=ec2_resource.Instance(master_id)
	if primary_instance.state['Name'] == "running":
		print("Master is up running no need of any modifications")
	else:
		secondary_instance=ec2_resource.Instance(clave_id)
		pnetwork_interface_Info=primary_instance.network_interfaces_attribute[0]
		snetwork_interface_Info=secondary_instance.network_interfaces_attribute[0]
		pnw_interface_id=pnetwork_interface_Info['NetworkInterfaceId']
		snw_interface_id=snetwork_interface_Info['NetworkInterfaceId']
		ec2_client=boto3.client("ec2", "us-east-1")
		ec2_client.unassign_private_ip_addresses(
			NetworkInterfaceId=pnw_interface_id,
			PrivateIpAddresses=[secondary_ip]
		)
		ec2_client.assign_private_ip_addresses(
			AllowReassignment=True
			NetworkInterfaceId=snw_interface_id,
			PrivateIpAddresses=[secondary_ip]
		)
return None

