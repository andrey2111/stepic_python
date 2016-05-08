import sys
import re

pattern = r'.*?cat.*?cat'

for line in sys.stdin:
    line = line.rstrip()
    if re.search(pattern, line):
        print(line)
