import urllib.request
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
first_value = '12345'

resp = urllib.request.urlopen(url + first_value).read().decode()
next_value = "".join(re.findall("\d", resp))

print('Laisse ce programme tourner pendant 3 à 5 mins')
print('Let this programm run for 3 or 5 mins')

inp = input('ok ? (Taper quelque chose/ Type something) : ')

while True:
    resp = urllib.request.urlopen(url + next_value).read().decode()
    print(resp)
    if  re.search("(\d)", resp) == None:
        break
    next_value = "".join(re.findall("\d", resp))

resp = urllib.request.urlopen(url + str(int(next_value) /2 )).read().decode()
next_value = "".join(re.findall("\d", resp))

while True:
    resp = urllib.request.urlopen(url + next_value ).read().decode()
    print(resp)
    if  re.search("(\d)", resp) == None:
        break
    next_value = "".join(re.findall("\d", resp))