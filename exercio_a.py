# -*- coding: utf-8 -*-
"""exercio_a.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MLjJf-gQmvDHmYqmgPuux49dbBCWHTm1
"""

from google.colab.patches import cv2_imshow
import cv2
import numpy as np

imagem = cv2.imread("/content/1.jpg")

verde = (0, 255, 0)
azul = (255, 0, 0)

cv2.rectangle(imagem, (960, 1090), (1140, 1310), verde, 3)
fonte = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(imagem, "Carro", (970, 1070), fonte, 2,(verde), 2, cv2. LINE_AA)


cv2.rectangle(imagem, (1760, 1150), (2150, 1410), verde, 4)
cv2.putText(imagem, "Carro", (1810, 1110), fonte, 2,(verde), 2, cv2. LINE_AA)

cv2.rectangle(imagem, (1525, 1120), (1687, 1590), azul, 4)
cv2.putText(imagem, "Pessoa", (1530, 1110), fonte, 1,(azul), 2, cv2. LINE_AA)
# dando cada pixe em cada linha
#for i in range(0, imagem.shape[0]):
#  for j in range(0,imagem.shape[1]):
#    for h in range(0,3):
#      print(imagem[i][j][h])


# dando tamos de altura e largura e quantidade de cores.
print(imagem.shape[0])
print(imagem.shape[1])
print(imagem.shape[2])



cv2_imshow(imagem)


cv2.waitKey(0)
cv2.imwrite("exercio_a.jpg", imagem)