import requests
import json
import sys
import operator

client_id = '1a1d948b543e58119b2d'
client_secret = '2abc37a3deb70eec60a2a230dfa26866'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
url = "https://api.artsy.net/api/artists/{}"
artists = {}

with open('dataset_24476_4.txt') as inf:
    for line in inf:
        r = requests.get(url.format(line.strip()), headers=headers)
        artists[r.json()['sortable_name']] = r.json()['birthday']

for artist in sorted(artists.items(), key=operator.itemgetter(1)):
    print(artist[0])
