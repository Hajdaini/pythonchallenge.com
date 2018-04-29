import urllib.request
import re
import zipfile

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/channel.html").read().decode()
data = re.findall("<--(.*?)-->", html, re.DOTALL) #ici on ne prend que le contenu dans les commentaires
print(''.join(data))

print('First download the zip file from http://www.pythonchallenge.com/pc/def/channel.html and put it in the current directory')
print("Téléchargez d'abord le fichier zip depuis http://www.pythonchallenge.com/pc/def/channel.html et placez-le dans le répertoire courant")
inp = input('ok ? (Taper quelque chose/ Type something) : ')


f = zipfile.ZipFile("channel.zip") # The class for reading and writing ZIP files.
print(f.read("readme.txt").decode("utf-8"))

first_value = '90052'

resp = f.read(first_value + ".txt").decode()
next_value = "".join(re.findall("\d", resp))

res = ''

while True:
    try :
        resp = f.read(next_value + ".txt").decode()
        res += (f.getinfo(next_value + ".txt").comment.decode("utf-8"))
    except :
        break
    print(resp)
    next_value = "".join(re.findall("\d", resp))

print(res)