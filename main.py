from PIL import Image


def ex001():
"""
    1) Operação Negativo. Considere a imagem em escala de cinza fig1.tif e aplique a função 
    de negativo. Mas antes, crie uma tabela de lookup e faça a transformação aplicando a 
    tabela
"""
    img = Image.open('fig1(2).tif')
    imload = img.load()
    lookup = {}
    for k in range(256):
        lookup[k] = 255 - k
    w, h = img.size
    for i in range(w):
        for j in range(h):
            imload[i,j] = lookup[imload[i,j]]

    img.show()

ex001()
