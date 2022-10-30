import boto3                                                                                                              
from pprint import pprint                                                                                                 

def lambda_handler(event, context):                                                                                                                                                                                          
	ec2_client=boto3.client(service_name="ec2",region_name="us-east-1")                                                       
	all_regions=[]                                                                                                                                                                                                                    
	for each_region in ec2_client.describe_regions()['Regions']:                                                                       
	  all_regions.append(each_region.get('RegionName'))                                                           
                                                                                                                                        
	for each_region in all_regions:
		print("Working on {}".format(each_region))
		ec2_client=session.client(service_name="ec2", region_name=each_region)
		list_of_volids=[]
		f_prod_bkp={'Name': 'tag:Prod', 'Values':['backup', 'Backup']}
		paginator = ec2_client.get_paginate('describe_volumes')
		for each_page in paginator.paginate(Filters=[f_prod_bkp]):
			for each_vol in each_page['Volumes']:
				list_of_volids.append(each_vol['VolumeId'])
		
		print("The list of volids are: ", list_of_volids)
		if bool(list_of_volids)==False:
			continue                                                                                                      
		#Creating snapshots for volumes one by one                                                                                
		snap_ids=[]                                                                                                               
		for each_volid in list_of_volids:
			print ("Taking snap of {}".format(each_volid))                                                                                                
		  response= ec2_client.create_snapshot(                                                                                      
		    Description='Snap with Lambda',                                                                                       
		    VolumeId=each_volid,                                                                                                  
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