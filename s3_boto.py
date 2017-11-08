""" A s3 client implementation using the boto package. """

import boto
from boto.s3.connection import Location
from boto.s3.key import Key

credential_file = 'credentials.csv'

with open(credential_file) as f:
    content = f.read()

user_details = content.split['\n'][1].split(',')
access_id, access_key = user_details[2:4]

# create the connection
conn = boto.connect_s3(access_id, access_key)

#create bucket
conn.create_bucket('korla007.example.com')

# to display buckets.
buckets = conn.get_all_buckets()
print ([bucket.name for bucket in buckets])

# get a specific bucket
get_bucket = 'ahaankorla.example.com'
bucket = conn.get_bucket(get_bucket)

print ([k.name for k in bucket.list()])

## For uploading and downloading use key
