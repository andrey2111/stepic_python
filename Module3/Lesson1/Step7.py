s = input()
t = input()
ans = 0
while t in s:
    ans += 1
    s = s[s.find(t)+1:]
print(ans)
