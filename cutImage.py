import numpy as np
import cv2
def cut():
    # img = cv2.imread(join(dirname(realpath(__file__)), pathImage)
    img = cv2.imread('uploads/img.png') 
    imgGry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thrash = cv2.threshold(imgGry, 240 , 255, cv2.CHAIN_APPROX_NONE)
    contours , hierarchy = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    #positions é uma lista contendo dicionarios compostos por quatro elementos, posição no eixo y da borda superior e da 
    #inferior e a posição no eixo x da borda lateral esquerda e direita
    positions = []
    #cada contour representa todo o contorno das figuras encontradas
    for contour in contours:
        matrizX = []
        matrizY = []
        approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
        if len(approx) == 4 :
            for i in range(len(contour)):
                c = contour[i][0]
                matrizX.append(c[0])
                matrizY.append(c[1])
            beginY = min(matrizY)
            beginX = min(matrizX)
            endY = max(matrizY)
            endX = max(matrizX)
            positions.append({'bx': beginX, 'by': beginY, 'ex': endX, 'ey': endY})
                
    #aqui eu estou pegando as posições de cada figura(começo e fim no eixo x e y) e pegando qual a maior largura encontrada
    #entre elas
    widths = []
    for i in positions:
        width = i['ex'] - i['bx']
        widths.append(width)
    bigWidth = max(widths)

    #agora estou filtrando os elementos encontrados para apenas aqueles cuja largura se aproxima da maior largura encontrada
    #evitando que sejam impressas pequenas figuras detectadas
    positionsFilted = []
    for i in positions:
        width = i['ex'] - i['bx']
        if(width > (bigWidth - 8) and width <= bigWidth):
            positionsFilted.append(i)

    #o teste é composto por 100 duplas de perguntas, cada dupla sendo um retângulo, se por ventura o número de triângulos 
    #detectados for diferente de 100 o usuário terá que fornecer outra imagem
    if len(positionsFilted) != 100:
        print('ocorreu um erro ao analizar a imagem')
        return False
    else:    
        print('análise feita com sucesso')
        index = 0
        #aqui eu percorro a lista já filtrada e crio a imagem de cada elemento encontrado
        for i in positionsFilted:
            img2 = img[i['by']:i['ey'], i['bx']:i['ex']]
            cv2.imwrite('output/out{}.jpg'.format(index), img2)
            index =  index + 1
        return True
