import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get all stopped EC2 instances
    instances_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])
    stopped_instance_ids = []

    for reservation in instances_response['Reservations']:
        for instance in reservation['Instances']:
            stopped_instance_ids.append(instance['InstanceId'])

    # Start all stopped instances
    if stopped_instance_ids:
        ec2.start_instances(InstanceIds=stopped_instance_ids)
        print(f"Started EC2 instances: {stopped_instance_ids}")
    else:
        print("No stopped instances to start.")