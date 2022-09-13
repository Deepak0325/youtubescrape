# To upload youtube video directly to amazon S3 bucket whithout downloading it to local system
import pafy
import requests
import boto3
video="your video link here"
v = pafy.new(video)
ur = v.getbest()
watch_url=ur.url
s3 = boto3.resource('s3', aws_access_key_id="Your Access key id here", aws_secret_access_key="Your Secret Access Key here")
bucket_name = 'youvidscraper'
r = requests.get(watch_url, stream=True)
print(r)
key = "youvid"
bucket = s3.Bucket(bucket_name)
bucket.upload_fileobj(r.raw, key)
