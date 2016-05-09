import sys

for line in sys.stdin.readlines():
    try:
        if int(line.strip(), base=2) % 3 == 0:
            print(line.strip())
    except ValueError:
        pass