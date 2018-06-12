import cv2
import PIL.ImageGrab
from matplotlib import pyplot as plt
import time as t
from PIL import Image
from pytesseract import image_to_string
import numpy as np

def TelaInput():
    # TIRA O PRINT
    t.sleep(3)
    im =PIL.ImageGrab.grab()
    im.show()

    im=Image.open("print.jpg")

    # SEPARA O QUADRADO
    im2 = im.crop((709, 467, 1194, 952))
    dx=121
    dy=121

    # SEPARA OS 16 QUADADROS
    quadrados=[]
    for j in range(1,5):
        for i in range(1,5):
            quadrado=im2.crop((1+(i-1)*dx,1+(j-1)*dy,i*dx,j*dy))
            quadrado=np.array(quadrado)
            quadrados.append(quadrado)

    # LISTA QUE SALVA O VALOR DE CADA QUADRADO
    q=[]
    for i in range(len(quadrados)):
        i=1
        q.append(i)

    # LE POR COR
    vazio=[205,192,180]
    dois=[238,228,218]
    quatro=[237,224,200]
    oito=[242,177,121]
    for i in range(len(quadrados)):
        if comparador(quadrados[i][10,10],vazio):
            q[i]=0
        elif  comparador(quadrados[i][10,10],dois):
            q[i]=2
        elif comparador(quadrados[i][10,10],quatro):
            q[i]=4
        elif  comparador(quadrados[i][10,10],oito):
            q[i]=8

    # PINTA OS QUADRADOS
    for a in range(len(quadrados)):
        if q[a]==1:
            quadrado=np.array(quadrados[a])
            fundo=[]
            for i in quadrado[10,10]:
                fundo.append(i)
            for i in range(7,114):
                for j in range(7,114):
                    if comparador(quadrados[a][i,j],fundo):
                        quadrados[a][i,j]=[255,255,255]
                    else:
                        quadrados[a][i,j]=[0,0,0]

    # LE POR PYTESSERACT
    for i in range(len(quadrados)):
        if q[i]==1:
            q[i]=int(image_to_string(quadrados[i]))

    return q


def comparador(pixel1,pixel2):
    resposta=[]
    resposta.append(np.isclose(pixel1[0],pixel2[0],rtol=0.05))
    resposta.append(np.isclose(pixel1[1],pixel2[1],rtol=0.05))
    resposta.append(np.isclose(pixel1[2],pixel2[2],rtol=0.05))
    true=[True,True,True]
    if resposta==true:
        return True
    else:
        return False
