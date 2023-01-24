import pyqrcode
from PIL import Image

link = input('Introdusca el url: ')
qr_code = pyqrcode.create(link)
qr_code.png('Codigo QR.png', scale=10)
Image.open('Codigo QR.png')

print('QR generado! revisar en la carpeta')
