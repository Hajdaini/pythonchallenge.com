import urllib.request
import re

html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

data = re.findall("<!--(.*?)-->", html, re.DOTALL)
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", data[-1])))

