import boto3

ec2 = boto3.client(service_name = 'ec2')
response = ec2.describe_regions()

all_regions = ([i['RegionName'] for i in response['Regions']])

for i in all_regions:
    try:
        gd = boto3.client(service_name = 'guardduty', region_name = i)

        response = gd.create_detector(Enable=True)

        print("In region ", i, " response is", response)

    except:
        print("Already enabled or thrown an error")
