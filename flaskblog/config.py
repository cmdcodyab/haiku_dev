
import os
from boto.s3.connection import S3Connection


class Config:
    s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])