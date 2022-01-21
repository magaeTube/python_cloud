import boto3

PROFILE_NAME = "AWS Profile 정보가 담겨있는 이름"
REGION_NAME = "AWS Region명"
BUCKET_NAME = "S3 버킷명"
LOCAL_FILE_NAME = "로컬 파일명(전체경로)"
UPLOAD_FILE_NAME = "업로드할 버킷 파일명(전체경로)"
DOWNLOAD_FILE_NAME = "다운로드할 버킷 파일명(전체경로)"


def check_bucket():
    session = boto3.Session(profile_name=PROFILE_NAME)
    s3 = session.client("s3", region_name=REGION_NAME)
    # s3 = boto3.resource("s3")
    for bucket in s3.bucket.all():
        print(bucket.name)


def upload_to_bucket():
    session = boto3.Session(profile_name=PROFILE_NAME)
    s3 = session.client("s3", region_name=REGION_NAME)
    # s3 = boto3.client("s3")
    s3.upload_file(LOCAL_FILE_NAME, BUCKET_NAME, UPLOAD_FILE_NAME)


def download_from_bucket():
    session = boto3.Session(profile_name=PROFILE_NAME)
    s3 = session.client("s3", region_name=REGION_NAME)
    # s3 = boto3.client("s3")
    s3.download_file(BUCKET_NAME, DOWNLOAD_FILE_NAME, LOCAL_FILE_NAME)
