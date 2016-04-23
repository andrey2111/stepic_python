classes = {} # класс : [прямые предки]


def isin(parent, child):
    if parent == child:
        return True
    if classes.get(child) is None:
        return False
    if parent in classes[child]:
        return True
    else:
        for i in classes[child]:
            if isin(parent, i):
                return True

n = int(input())
for i in range(n):
    s = input().split(':')
    if len(s) > 1:
        classes[s[0].strip()] = [c for c in s[1].split()]
    else:
        classes[s[0].strip()] = None

q = int(input())
for j in range(q):
    query = input().strip().split()
    if isin(query[0], query[1]):
        print('Yes')
    else:
        print('No')

print(classes)
