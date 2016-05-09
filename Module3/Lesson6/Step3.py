import requests
import sys

url = 'http://numbersapi.com/{}/math?json=true'
with open('dataset_24476_3.txt') as inf:
    for line in inf:
        number = int(line)
        res = requests.get(url.format(number))
        if res.json()['found']:
            print('Interesting')
        else:
            print('Boring')
