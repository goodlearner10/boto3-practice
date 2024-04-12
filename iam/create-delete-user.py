import boto3

client = boto3.client('iam')

username = "theo"

try:
    res = client.create_user(UserName=username)
    print(f"{username} 사용자가 생성되었습니다.")
except client.exceptions.EntityAlreadyExistsException:
    print(f"{username} 사용자가 이미 존재합니다.")

try:
    client.delete_user(UserName=username)
    print(f"{username} 사용자가 삭제되었습니다.")
except client.exceptions.NoSuchEntityException:
    print(f"{username} 사용자가 존재하지 않습니다.")