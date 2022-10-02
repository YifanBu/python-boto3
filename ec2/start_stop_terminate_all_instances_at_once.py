import boto3
aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
'''
all_instances_ids=[]
for each_instance in ec2_con_re.instances.all():
	all_instances_ids.append(each_instance.id)
#print(dir(ec2_con_re.instances))
waiter=ec2_con_cli.get_waiter('instance_running')
print("Starting all instances ......")
ec2_con_re.instances.start()
waiter.wait(InstanceIds=all_instances_ids)
print("your all instances are up and running")
'''
'''
non_prod_servers_id=[]
f1={"Name": "tag:Name", "Values":['Non_Prod']}
for each_instance in ec2_con_re.instances.filter(Filters=[f1]):
	non_prod_servers_id.append(each_instance.id)

print(non_prod_servers_id)

print("----------------------------")
'''

non_prod_servers_id=[]
f1={"Name": "tag:Name", "Values":['Non_Prod']}
for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
	for each_instance in each_item['Instances']:
		non_prod_servers_id.append(each_instance['InstanceId'])
print(non_prod_servers_id)

print("Starting instances with ids of : ",non_prod_servers_id)
ec2_con_cli.start_instances(InstanceIds=non_prod_servers_id)
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=non_prod_servers_id)
print("Your np instances are up and running....")