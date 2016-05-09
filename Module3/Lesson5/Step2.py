import csv
from collections import Counter

types = {}
with open('Crimes.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2].split()[0].split('/')[2] == '2015':
            if row[5] not in types:
                types[row[5]] = 1
            else:
                types[row[5]] += 1
print(Counter(types).most_common(1))
