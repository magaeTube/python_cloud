import boto3

PROFILE_NAME = "AWS Profile 정보가 담겨있는 이름"
REGION_NAME = "AWS Region명"
INSTANCE_ID = "EC2 인스턴스 ID"


def start_ec2_instance():
    session = boto3.Session(profile_name=PROFILE_NAME)
    ec2 = session.resource("ec2", region_name=REGION_NAME)

    instance = ec2.Instance(INSTANCE_ID)
    instance.start()
    instance.wait_until_running()


def stop_ec2_instance():
    session = boto3.Session(profile_name=PROFILE_NAME)
    ec2 = session.resource("ec2", region_name=REGION_NAME)

    instance = ec2.Instance(INSTANCE_ID)
    instance.stop()
    instance.wait_until_stopped()
