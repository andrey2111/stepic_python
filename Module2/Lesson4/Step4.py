lines = []

with open('input.txt') as inf:
    for line in inf:
        lines.append(line)

with open('output.txt', 'w') as ouf:
    for i in range(len(lines)):
        ouf.write(lines.pop())
