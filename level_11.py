from PIL import Image

print('First download the image from http://www.pythonchallenge.com/pc/return/cave.jpg and put it in the current directory')
print("Téléchargez d'abord l'image depuis http://www.pythonchallenge.com/pc/return/cave.jpg et placez-le dans le répertoire courant")
inp = input('ok ? (Taper quelque chose/ Type something) : ')

img = Image.open('cave.jpg')
(width, height) = img.size

even = Image.new('RGB', (width, height))

for w in range(width):
    for h in range(height):
        p = img.getpixel((w,h))
        if (w + h) % 2 == 0:
            even.putpixel((w, h), p)
even.show()

print('evil')