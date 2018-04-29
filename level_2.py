import urllib.request
import re
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
data = re.findall("<!--(.*?)-->", html, re.DOTALL) #ici on ne prend que le contenu dans les commentaires
print('resultat : ' + "".join(re.findall("[a-z]", data[-1]))) #on ne cherche que les alphabets

