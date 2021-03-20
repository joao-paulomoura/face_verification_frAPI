import base64
import json

def run(path):
  img = open(str(path), 'rb') #abrir arquivo
  img_read = img.read() # ler
  img.close() #fechar
  imgBase64 = base64.encodebytes(img_read) #converter
  return imgBase64.decode('utf8')
