import requests
import glob
import matplotlib.pyplot as plt
import numpy as np
import convertBase64 as cv64
import json


# REALIZAR A VERIFICAÇÃO DE FACE NA API
def post_face_verification(img_1, img_2):
  body = {
    "image_b641": img_1,
    "image_b642": img_2
  }
  return requests.post('http://35.237.84.73/frapi/verify/images', json=body)


# BUSCANDO O PAR DE IMAGENS PARA ANALISE
def get_path_img(line):
  if int(line[1]) < 10: # PRIMEIRA IMAGEM
    img1 = f'./lfw/{line[0]}/{line[0]}_000{line[1]}.jpg'
  elif int(line[1]) < 100:
    img1 = f'./lfw/{line[0]}/{line[0]}_00{line[1]}.jpg'
  elif int(line[1]) < 1000:
    img1 = f'./lfw/{line[0]}/{line[0]}_0{line[1]}.jpg'
  
  if len(line) == 3: # SEGUNDA IMAGEM LIFE
    if int(line[2]) < 10:
      img2 = f'./lfw/{line[0]}/{line[0]}_000{line[2]}.jpg'
    elif int(line[2]) < 100:
      img2 = f'./lfw/{line[0]}/{line[0]}_00{line[2]}.jpg'
    elif int(line[2]) < 1000:
      img2 = f'./lfw/{line[0]}/{line[0]}_0{line[2]}.jpg'
  else:# SEGUNDA IMAGEM SPOOF
    if int(line[3]) < 10:
      img2 = f'./lfw/{line[2]}/{line[2]}_000{line[3]}.jpg'
    elif int(line[3]) < 100:
      img2 = f'./lfw/{line[2]}/{line[2]}_00{line[3]}.jpg'
    elif int(line[3]) < 1000:
      img2 = f'./lfw/{line[2]}/{line[2]}_0{line[3]}.jpg'

  return img1, img2


# RETORNA UMA LISTA COM TODOS OS SCORE
def get_similarity_score(file_dataset):
  print(file_dataset)
  list_life = np.loadtxt(file_dataset, dtype=str)[0:10]
  score = []
  loading = ''
  for line in list_life:
    print(loading+'|', end="", flush=True)
    img1, img2 = get_path_img(line)
    img1_b64 = cv64.run(img1)
    img2_b64 = cv64.run(img2)
   
    response = post_face_verification(img1_b64, img2_b64)
    if response.status_code == 200:
      score.append(response.json()["similarity_score"])


  print('\n-----------------------------')
  print(f'TOTAL DE RESPOSTAS: {len(score)}')
  return score
