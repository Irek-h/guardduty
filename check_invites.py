import boto3

ec2 = boto3.client(service_name = 'ec2')
response = ec2.describe_regions()

all_regions = ([i['RegionName'] for i in response['Regions']])

for i in all_regions:
    try:
        client = boto3.client('guardduty')


        inv = client.list_invitations()

        print("In region ", i, ", there are pending invites: ", inv['Invitations'])

        resp = client.list_detectors()
        detector_id = resp['DetectorIds'][0]

        resp = client.list_members(DetectorId = detector_id)
        member = resp['Members']

        print("In region", i, ", we have those members: ", member)

    except:
        print("DUNNO!")
