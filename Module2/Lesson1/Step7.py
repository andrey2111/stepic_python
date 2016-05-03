parents = {}
used_classes = set()


def check(clas):
    for parent in parents[clas]:
        if parent in used_classes:
            return True
        else:
            if parent in parents:
                return check(parent)

n = int(input())
for i in range(n):
    line = input().split(':')
    if len(line) > 1:
        parents[line[0].strip()] = [parent for parent in line[1].split()]

m = int(input())
for i in range(m):
    clas = input()
    if clas in parents and check(clas):
        print(clas)
    else:
        used_classes.add(clas)
