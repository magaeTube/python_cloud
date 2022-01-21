from pyathena import connect
from pyathena.cursor import DictCursor

REGION_NAME = "AWS Region명"
S3_RESULT_PATH = "Query 결과를 저장할 S3 경로"
QUERY = "쿼리문"


def connect_athena():
    cursor = connect(s3_staging_dir=S3_RESULT_PATH, region_name=REGION_NAME).cursor(DictCursor)
    return cursor


def execute_select_query():
    cursor = connect_athena()
    cursor.execute(QUERY)
    result = cursor.fetchall()

    cursor.close()
    return result
