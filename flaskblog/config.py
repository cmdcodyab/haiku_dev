
#from boto.s3.connection import S3Connection
import os

class Config:
    #s3 = S3Connection(os.environ['S3_KEY'], os.environ['S3_SECRET'])
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    MAIL_USE_TLS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = 'mod.haiku@gmail.com'
    MAIL_PASSWORD = 'P8F3kTUPh'