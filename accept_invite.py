import boto3

ec2 = boto3.client(service_name = 'ec2')

response = ec2.describe_regions()

all_regions = ([i['RegionName'] for i in response['Regions']])

for i in all_regions:
	try:
			gd = boto3.client(service_name = 'guardduty', region_name = i)
			response = gd.list_invitations()
			
			admin_acc_id = response['Invitations'][0]['AccountId']
			invite_id = response['Invitations'][0]['InvitationId']
			
			response = gd.list_detectors()
			
			detector_id = response['DetectorIds'][0]
			
			response = gd.accept_invitation(
			         DetectorId=detector_id,
			         MasterId=admin_acc_id,
			         InvitationId=invite_id
			)
		print(response)
	except:
		print("Already works or an error")
