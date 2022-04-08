import boto3

ec2 = boto3.client(service_name = 'ec2')
response = ec2.describe_regions()

all_regions = ([i['RegionName'] for i in response['Regions']])

for i in all_regions:
    try:
        gd = boto3.client(service_name = 'guardduty', region_name = i)

        response = gd.list_detectors()
        detector_id = response['DetectorIds'][0]

        response = gd.delete_detector(DetectorId = detector_id)
        print(response)
    except:
        print("Didn't exist in the first place")
