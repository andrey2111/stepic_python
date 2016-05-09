s = input()
a = input()
b = input()
ans = 0
if a in s and a in b:
    print('Impossible')
else:
    while a in s:
        s = s.replace(a, b)
        ans += 1
    print(ans)
