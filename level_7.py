from PIL import Image
import re

img = Image.open("oxygen.png")

colors = []

for x in range(img.width):
    colors.append(img.getpixel((x, img.height / 2)))

colors = colors[::7]

res = []
for r, g, b, a in colors:
    if r == g == b:
        res.append(g)


res = re.findall('(\d{3})',  "".join(map(chr, res)))
print("".join(map(chr, map(int, res))))