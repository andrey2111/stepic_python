import datetime

year, month, day = (int(i) for i in input().split())
date = datetime.date(year, month, day)
delta = datetime.timedelta(days=int(input()))
ans = date+delta

print(ans.year, ans.month, ans.day)
