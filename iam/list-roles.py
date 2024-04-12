import boto3
from datetime import datetime, timezone, timedelta

# 프로그램 실행시간 기준
now = datetime.now(timezone.utc)
print(now)


client = boto3.client('iam')
roles = client.list_roles()["Roles"] # This operation does not return the RoleLastUsed attribute

# iterator = client.get_pagenator("list_roles").pagenate()
# roles = [role for roles in iterator for role in roles["Roles"]]

for role in roles:
    name = role["RoleName"]
    r = client.get_role(RoleName=name)["Role"] #  To view all of the information for a role, see GetRole.
    last_used_date = r["RoleLastUsed"].get("LastUsedDate")

    if not last_used_date: # None
        print(name, "400일 내 사용 기록이 없음")
    elif (now - last_used_date) > timedelta(days=90):
        print(name, f"90일 내 사용 기록 없음 | {last_used_date}")
    else:
        print(name, f"90일 내 사용 기록 있음 | {last_used_date}")