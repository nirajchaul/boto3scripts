import boto3

ec2 = boto3.resource('ec2')
##ec2 = boto3.resource('ec2', region_name='us-west-1')
##change imageid and keyname as they are region specific

instances = ec2.create_instances(
    ImageId='ami-0be2609ba883822ec',
    MinCount=1,
    MaxCount=2,
    InstanceType='t2.micro',
    KeyName='DevOpsAutomationKey'
)

 