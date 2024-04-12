import boto3
from pprint import pprint

client = boto3.client('sts')
res = client.get_caller_identity()

pprint(res)
# pretty print

print(res["UserId"],res["Account"],res["Arn"])
# 정보 추출

if res["Arn"].endswith("root"):
	print("root 계정을 사용중입니다.")
else:
	print("root가 아닌 계정을 사용중입니다.")