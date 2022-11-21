from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from enum import Enum
import random
from os import remove
import os 
import re

class Quest:

    #guarda una pregunta tipo test
    def __init__(self, statement:str):
        self.statement = statement
        self.options = []
        self.explanations = []
        self.answer= []

    #anyade una opcion a la pregunta 
    #<statement> = texto
    #<isCorrets> = True = pertenece al conjunto de respuestas, else False 
    #<explanation> = justificacion de <isCorrect>
    def addOption(self, statement: str, isCorrect : bool, explanation:str='' ):
        index = len(self.options)
        self.options.append(statement)
        self.explanations.append(explanation)
        if isCorrect :
            self.answer.append(index)
    
    #devuelve el enunciado de la pregunta
    def getStatement(self):
        return self.statement

    #devuelve las opciones de la pregunta
    def getOptions(self):
        return self.options

    #devuelve un array con los incies de las opciones correctas
    def getAnwsers(self):
        return self.answer

    #devuelve answer es el conjunto de respuestas correctas
    #<answer> = conjunto de opciones seleccionadas
    #Pre : 0 <= <answer.len <= self.options.len>
    def answerTest(self, answer: list[int]):
        if len(answer) != len(self.answer):
            return False
        for i in answer:
            if not (i in self.answer):
                return False
        return True
    
    def __str__(self) -> str:
        string = self.statement 
        for i,a in enumerate(self.options ):
            string += '\t' + str(i) + ') ' + a 
        ##string += "Anwer :" + str(self.answer) 
        return string

class Test:
    
    def __init__(self,  file : str , sourcePDF: str = None, sourceDir: str = None):
        images = []
        if sourcePDF == None  and sourceDir == None:
            self.setQuests(file)
        elif sourcePDF != None:
            images = self.getImages(sourcePDF)
            if self.readImages(images, file):
                self.setQuests(file)
            self.deleteImages(images)
        else: 
            for file in os.listdir(sourceDir):
                images += self.getImages(file)
            if self.readImages(images, file):
                self.setQuests(file)
            self.deleteImages(images)

    #separa el archivo <filePDF> en imagenes PNG
    #devuelve una lista con el nombre de las fotos generadas
    def getImages(self, filePDF : str) -> list[str]:
        try:
            imageFiles = []
            images = convert_from_path(filePDF, dpi=100)
            for i, page in enumerate(images):
                idx= 'image_' + filePDF + '_' +str(i)+'.jpg' ##or ".png"
                page.save(idx, 'JPEG')
                imageFiles.append(idx)
            print(filePDF +" se convirtio en imagenes correctamente")
            return imageFiles
        except:
            print ("Error al leer " + filePDF)
            return []

    #elimina los achivos indicados en <images>
    def deleteImages(self, images:list[str]) -> bool:
        try : 
            for img in images:
                remove(img)
            return True
        except :
            return False
    

    #escribe el texto incluido en las imagenes contnidas en  <images> y 
    def readImages(self, images : list[str], file : str) -> bool:
        try:
            f=open(file, 'w')
            for img in images:
                text=str(pytesseract.image_to_string(Image.open(img)))
                f.write(text)
            f.close()
            return True
        except:
            return False

    class State(Enum):
        Init = 0
        Statement = 1
        Option = 2
        Explanation = 3

    def setQuests( self, file:str ) -> list[Quest]:
            print('Comienzo de lectura')
            state = self.State.Init
            self.quests : list[Quest] = []
            f= open(file, 'r')
            print('Archivo abierto')
            patronPregunta = re.compile(r'Q[0-9]*\)')
            for linea in f:
                #nos saltamos las lineas iniciales e los distintos test
                if linea.startswith('Answer Sheet'):
                    #print('Nueva Parte')
                    continue
                if not linea.strip():
                    continue
                #dividimos la linea en palabras
                #tokens = linea.split[" "]
                #eliminamos los espacios para procesar la linea
                lineaSinEspacios = linea.replace(' ','')
                #print(state)
                match state:
                    case self.State.Init:
                        if patronPregunta.search(lineaSinEspacios) != None:
                            statement = linea
                            state = self.State.Statement
                        else: 
                            print('Entrada Inesperada: ' + linea)
                    case self.State.Statement: 
                        if lineaSinEspacios[0] == '@' :
                            state = self.State.Option
                            q = Quest(statement)
                            isCorrect = lineaSinEspacios[1] == '@'
                            statement = linea
                        else :
                            statement += linea
                    case self.State.Option:
                        
                        if patronPregunta.search(lineaSinEspacios) != None:
                            state = self.State.Statement
                            statement = statement.replace('@', ' ').lstrip()
                            q.addOption(statement, isCorrect)
                            self.quests.append(q)
                            statement = linea
                        elif lineaSinEspacios[0] == '@' : 
                            statement = statement.replace('@', ' ').lstrip()
                            q.addOption(statement, isCorrect)
                            isCorrect = lineaSinEspacios[1] == '@'
                            statement = linea
                        elif linea.startswith('Explanation:-') :
                            state = self.State.Explanation 
                            e = linea
                        else:
                            statement += ' ' + linea
                    case self.State.Explanation:
                        if patronPregunta.search(lineaSinEspacios) != None:
                            state = self.State.Statement
                            statement = statement.replace('@', ' ').lstrip()
                            q.addOption(statement, isCorrect, e)
                            self.quests.append(q)
                            statement = linea
                        
                        elif lineaSinEspacios[0] == '@' : 
                            state = self.State.Option
                            statement = statement.replace('@', ' ').lstrip()
                            q.addOption(statement, isCorrect, e)
                            isCorrect = lineaSinEspacios[1] == '@'
                            statement =  linea
                        else:
                            e = ' ' + linea  
                

    #seleciona <num> pregntas aleatorias
    def getRandomQuest(self, num : int) -> list[Quest]:
        if num > len(self.quests):
            num =len(self.quests)
            print("El test solo contiene ", num, " preguntas")
        return random.choices(self.quests, k = num)

    def getQuests(self) -> list[Quest]:
        return self.quests

    def __str__(self) -> str:
        string = 'Preguntas : \n'
        for q in self.quests:
            string += str(q)
        return string



def main():

    t = Test('test2.md')    
    acertadas = 0
    totales = 20
    r = t.getRandomQuest(totales)
    for q in r:
        print(q)
        respuesta = input("Introduce las corretas separadas por un espacio: ")
        aux = respuesta.split(" ")
        aux2 = []
        for i in aux:
            aux2.append( int(i))
        if q.answerTest(aux2) :
            print("Correcto")
            acertadas += 1
        else: 
            print(aux2)
            print("Las respuestas son : ", q.getAnwsers())
        print ("------------------------")

    print('Test finalizado: ', ((acertadas*100)/totales) , '%')

main() 