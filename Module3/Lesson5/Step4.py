import json


def find(name, parents):
    for parent in parents:
        childs[parent].add(name)
        for d in data:
            if d['name'] == parent:
                if d['parents']:
                    find(name, d['parents'])
                else:
                    childs[d['name']].add(name)



js = '[{"name": "dfgre", "parents": ["gsdfgre"]}, {"name": "hsdgreg", "parents": ["dfgre", "gsd"]}, {"name": "gsd", "parents": ["dfgre"]}, {"name": "gsdfgre", "parents": []}]'
data = json.loads(js)
childs = {}

for d in data:
    childs[d['name']] = set()
    childs[d['name']].add(d['name'])
for d in data:
    #print(str(d['name'])+' : '+str(d['parents']))
    find(d['name'], d['parents'])

for i in sorted(childs):
    print(str(i) + ' : ' + str(len(childs[i])))
