import pickle
import urllib.request

resp = pickle.load(urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p"))
res = ''

for line in resp:
    for v in line:
        res += v[0] * v[1]
    res += '\n'

print(res)