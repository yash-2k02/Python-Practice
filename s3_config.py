import boto3
from botocore.config import Config as BotoConfig
from env_config import settings

s3_client = boto3.client(
    "s3",
    endpoint_url=settings.tebi_endpoint,
    aws_access_key_id=settings.tebi_access_key,
    aws_secret_access_key=settings.tebi_secret_key,
    region_name='global',
    config=BotoConfig(signature_version="s3v4")
)

