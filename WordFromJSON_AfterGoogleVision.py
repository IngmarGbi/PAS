#Get Text from JSON post Google Vision

import io
import json

def traitementJSON(file) :

    #Lecture en tant que Txt car format JSON non reconnu
    with open(file) as json_file :
        data = json_file.read()
    #print(data)


    #Traitement du fichier
    blocks = data.split("blocks")[1:]
    for block in blocks :
        print("New Block")
        paras = block.split("paragraphs")[1:]
        for para in paras :
            print("New Para")
            words = para.split("words")[1:]
            for word in words :
                ligne = ""
                for symbol in word.split("symbols")[1:] :
                    ligne += symbol.split('"')[1] #Le 1er est le block de property pour la langue donc 3 mais test act donc 1
                    if "SPACE" in symbol : #Si espace après le symbole
                        ligne+= " "
                print(ligne)
        
traitementJSON('JeuDeTest\\test.json')
