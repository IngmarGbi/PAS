#Get text directly from Image

# pour exécuter python testVisionText.py receipt.jpg 
#Receipt : file original


import argparse
from enum import Enum
import io
from google.cloud import vision
from PIL import Image, ImageDraw
from QuickSort_Vertixes import *
    

def render_doc_test(file) :
    with io.open(file, 'rb') as image_file:
        content = image_file.read()
        
    image = vision.Image(content = content)
    response = client.text_detection(image=image)
    res = response.text_annotations
    xMax = res[0].bounding_poly.vertices[2].x
    yMax = res[0].bounding_poly.vertices[2].y
    
    varX = 5*xMax/100
    varY = 5*yMax/100
    
    #print(res)
    '''
    print('Texts:')

    
    for text in res[1:]:
        print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
            for vertex in text.bounding_poly.vertices ])
        print('bounds: {}'.format(','.join(vertices)))
    '''

    print("Reformation")
    
    #Reformation du Tableau
    #BESOIN DE TRIER LES VERTIXES
    data = res[1:]
    '''
    #test comparaison de 2 vertixes
    
    print("Data10 : "+str(data[9].bounding_poly.vertices[0].x)+","+str(data[9].bounding_poly.vertices[0].y))
    print("Data11 : "+str(data[10].bounding_poly.vertices[0].x)+","+str(data[10].bounding_poly.vertices[0].y))
    print("Data13 : "+str(data[12].bounding_poly.vertices[0].x)+","+str(data[12].bounding_poly.vertices[0].y))
    print(compare(data[9],data[10]))
    print(compare(data[9],data[12]))
    print(compare(data[10],data[12]))
    
    #Test sur 
    
    #data = sort(data)
    '''
    bubbleSort(data,varX,varY)
    '''
    print(len(data))


    for text in data:
        print('\n"{}"'.format(text.description))
        vertices = (['({},{})'.format(vertex.x, vertex.y)
            for vertex in text.bounding_poly.vertices ])
        print('bounds: {}'.format(','.join(vertices)))
    '''

    
    tab = []
    ligne = []
    for text in data:
        #Si détection de texte vide
        if text.description == "" :
            continue
        #Si début de nouvelle ligne
        if len(ligne) == 0 :
            ligne.append(text.description)
            #Mémoire du dernier mot détecté
            lastText = text
        else :
            #Ajout côte à côte
            if abs(text.bounding_poly.vertices[0].y - lastText.bounding_poly.vertices[1].y) < varY and abs(text.bounding_poly.vertices[0].x - lastText.bounding_poly.vertices[1].x) < varX :
                ligne[-1] += " "+text.description
                lastText = text
                continue
            #Ajout même ligne mais plus loin
            if  abs(text.bounding_poly.vertices[0].y - lastText.bounding_poly.vertices[1].y) < varY and abs(text.bounding_poly.vertices[0].x - lastText.bounding_poly.vertices[1].x) > varX :
                ligne.append(text.description)
                lastText = text
                continue
            #nouvelle ligne
            tab.append(ligne)
            ligne = [text.description]
            lastText = text
    for row in tab :
        for item in row :
            print(item,end="   ")
        print("")
    print("\nInscription dans le fichier Output.csv")
    import csv

    with open("Output.csv", "w",encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(tab)
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('detect_file', help='The image for text detection.')
    args = parser.parse_args()

    client = vision.ImageAnnotatorClient()
    render_doc_test(args.detect_file)
