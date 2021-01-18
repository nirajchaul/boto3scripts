##creates key pair for the default region and prints private key

import boto3

ec2 = boto3.client('ec2')
key = ec2.create_key_pair(KeyName='BotoGeneratedKey')
print(key["KeyMaterial"])