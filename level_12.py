from PIL import Image

print('First download the zip file from http://www.pythonchallenge.com/pc/return/cave.jpg and put it in the current directory')
print("Téléchargez d'abord le fichier zip depuis http://www.pythonchallenge.com/pc/return/cave.jpg et placez-le dans le répertoire courant")
inp = input('ok ? (Taper quelque chose/ Type something) : ')

data = open('evil2.gfx', 'rb').read()
print(data)

for i in range(5):
    open(str(i) + '.jpg','wb').write(data[i::5])
    try:
        Image.open(str(i) + '.jpg').show()
    except:
        print('Problem to open ' + str(i) + '.jpg')
        print('Problème d\'ouverture de ' + str(i))

print('disproportional')