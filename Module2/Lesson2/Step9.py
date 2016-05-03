import simplecrypt
from urllib import request

encrypted = request.urlopen('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').read()
passwords = request.urlopen('https://stepic.org/media/attachments/lesson/24466/passwords.txt').read().strip().split()

for password in passwords:
    try:
        print(simplecrypt.decrypt(password, encrypted))
    except simplecrypt.DecryptionException:
        pass
