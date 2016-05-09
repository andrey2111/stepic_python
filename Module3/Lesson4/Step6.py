import requests
import re


def find(a, b):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', a)
    for url in urls:
        c = requests.get(url).text
        urlsc = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', c)
        if b in urlsc:
            return 'Yes'
    return 'No'


A = requests.get(input()).text
B = input()

print(find(A, B))
