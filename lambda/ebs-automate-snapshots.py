"""
Automate Snapshots for EBS using Lambda & Cloudwatch

Step1: Create an IAM Service Role for Lambda Function → Lambda: Allow Lambda functions to call AWS services on your behalf → AmazonEC2FullAccess

Step2: Write Lambda Function

Step3: Define a trigger → CloudWatch Event → Create a new rule → Rule name → Rule type: Schedule expression: rate(1 day)
"""

import boto3                                                                                                              
from pprint import pprint                                                                                                 

def lambda_handler(event, context):                                                                                                                                                                                          
	ec2_re=boto3.resource(service_name="ec2",region_name="us-east-1")                                                       
	vol_ids=[]                                                                                                                
	#colleting volume Ids                                                                                                     
	for each_vol in ec2_re.volumes.filter(Filters=[]):                                                                        
	  #print each_vol.id                                                                                                   
	  vol_ids.append(each_vol.id)                                                                                          
                                                                                                                          
	print('All volume ids are: ',vol_ids)                                                                                      
                                                                                                                          
	#Creating snapshots for volumes one by one                                                                                
	snap_ids=[]                                                                                                               
	for each_vo_id in vol_ids:                                                                                                
	  response= ec2_re.create_snapshot(                                                                                      
	    Description='Snap with Lambda',                                                                                       
	    VolumeId=each_vo_id,                                                                                                  
	    TagSpecifications=[                                                                                                   
           {                                                                                                              
            'ResourceType': 'snapshot',                                                                                   
             'Tags': [                                                                                                    
                {                                                                                                         
                    'Key': 'Delete-on',                                                                                   
                    'Value':'90'                                                                                          
                 }                                                                                                        
                      ]                                                                                                   
          }                                                                                                               
       ]                                                                                                                  
     )                                                                                                                    
   snap_ids.append(response.id)                                                                                           
                                                                                                                          
	print snap_ids                                                                                                            
	#Creating waiter using client                                                                                             
	ec2_cli=boto3.client(service_name="ec2",region_name="us-east-1")                                                        
	waiter = ec2_cli.get_waiter('snapshot_completed')                                                                         
	waiter.wait(SnapshotIds=snap_ids)