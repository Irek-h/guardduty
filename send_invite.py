import boto3

ec2 = boto3.client(service_name = 'ec2')
response = ec2.describe_regions()

all_regions = ([i['RegionName'] for i in response['Regions']])

for i in all_regions:
    try:
        gd = boto3.client(service_name = 'guardduty', region_name = i)
        
        response = gd.list_detectors()
        detector_id = response['DetectorIds'][0]

        response = gd.create_members(
                DetectorId = detector_id,
                AccountDetails=[
                    {
                        'AccountId': 'ACCID',
                        'Email': 'EMAIL'
                    },
                ]
        )

        print(response)

        response = gd.invite_members(
                DetectorId = detector_id,
                AccountIds=['ACCID']
                )

        print(response)
    except:
        print("Member")
