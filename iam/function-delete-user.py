import boto3

client = boto3.client('iam')

def del_user(client, username):
    if not username:
        raise Exception(f"{username} 잘못된 사용자 이름입니다.")
    try:
        client.delete_user(UserName=username)
    except client.exceptions.NoSuchEntityException:
        return True,None # return Tuple
    except Exception as e:
        return False, e

del_user(client,"")