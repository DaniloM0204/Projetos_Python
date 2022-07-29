#Para esse projeto sera necessário instalar os pips abaixo

# 1º
# pip install PyQRCode
# pip install pypng

# 2º
# pip install pyzbar
# pip install pillow


# Primeira parte gerando um QrCode

import pyqrcode
import png

# Na linha do link, pode colocar o link que achar mais viável, como uma página do instagram ou como eu fiz, com a minha do github

link = "Insira aqui seu link"
qr_code = pyqrcode.create(link)
qr_code.png("formato necessariamente precisa ser .png", scale = 5)

# Segunda parte vai ser o decodificador de Qr_Code

from pyzbar.pyzbar import decode
from PIL import Image

# Ao realizar a primeira parte do código poderá fazer essa pra complementar

decodeQR =  decode(Image.open("Insira aqui seu arquivo PNG"))
print(decodeQR[0].data.decode('ascii'))

# O decodificador vai enviar um link via terminal para você acessar, no caso pode utilizar qualquer Qr_Code salvo, por isso futuramente irei atualizar para receber um arquivo png, assim facilitando o processo


