import sys
import re

pattern = r'\ba+\b'
for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(pattern, 'argh', line, 1, re.IGNORECASE))
