####Create Security Group using boto3

import boto3

ec2 = boto3.resource('ec2')

sec_group = ec2.create_security_group(
    GroupName='BotoTest', Description='BotoTest sec group', VpcId='vpc-b77ea4ca')
sec_group.authorize_ingress(
    
    CidrIp='0.0.0.0/0',
    IpProtocol='icmp',
    FromPort=-1,
    ToPort=-1
)
sec_group.authorize_ingress(
    
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=80,
    ToPort=80
)

sec_group.authorize_ingress(
    CidrIp='0.0.0.0/0',
    IpProtocol='tcp',
    FromPort=22,
    ToPort=22
)
