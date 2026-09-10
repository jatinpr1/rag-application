import boto3
from fastapi import FastAPI
from app.config import AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "RAG backend is running"}

@app.get("/test-aws-connection")
def test_aws_connection():
    s3_client = boto3.client(
        "s3",
        region_name=AWS_REGION,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    response = s3_client.list_buckets()
    bucket_names = [bucket["Name"] for bucket in response["Buckets"]]
    return {"status": "connected", "buckets": bucket_names}
print("fef")