#boto3 supooert 2 stuff: resource & client
import boto3
import logging

botocore ##exceptions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = boto3.client('s3', region_name = 'eu-west-1')

response = client.create_bucket( Bucket = 'dilys-boto3-abc',
                                CreateBucketConfiguration = {'LocationConstraint': 'eu-west-1'} )

logger.info(response)