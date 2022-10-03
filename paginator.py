import boto3

session=boto3.session.Session(profile_name='default')

count = 1

'''
iam_client=session.client('iam')
paginator = iam_client.get_paginator('list_users')
for each_page in paginator.paginate():
  for each_user in each_page['Users']:
    print (count, each_user['UserName'])
    count = count + 1
'''

ec2_client = session.client('ec2')
paginator = ec2_client.get_paginator('describe_instances')
for each_page in paginator.paginate():
  print(each_page)
