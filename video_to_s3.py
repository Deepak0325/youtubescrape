"""import pafy
import requests
import boto3
video="https://www.youtube.com/watch?v=KNTz0N10lzg"
v = pafy.new(video)
ur = v.getbest()
watch_rul=ur.url
print(watch_rul)
s3 = boto3.resource('s3', aws_access_key_id="Your Access key id here", aws_secret_access_key="Your Secret Access Key here")
bucket_name = 'youvidscraper'
r = requests.get(watch_rul, stream=True)
print(r)
key = "youvid"
bucket = s3.Bucket(bucket_name)
bucket.upload_fileobj(r.raw, key)"""
