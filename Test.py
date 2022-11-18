from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from enum import Enum
import random

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
        index = len(self.answer)
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
        return self.answers

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
        for a in self.options :
            string += '\t' + a 
        return string

class Test:
    
    def __init__(self,  file : str , sourcePDF: str = None):
        if sourcePDF == None:
            self.setQuests(file)
        else:
            images = self.getImages(sourcePDF)
            if self.readImages(images, file):
                self.setQuests(file)
            self.deleteImages(images)

    #separa el archivo <filePDF> en imagenes PNG
    #devuelve una lista con el nombre de las fotos generadas
    def getImages(self, filePDF : str) -> list[str]:
        imageFiles = []
        images = convert_from_path(filePDF, dpi=100)
        for i, page in enumerate(images):
            idx= 'image_'+str(i)+'.jpg' ##or ".png"
            page.save(idx, 'JPEG')
            imageFiles.append(idx)
        return imageFiles

    #elimina los achivos indicados en <images>
    def deleteImages(self, images:list[str]) -> bool:
        return True
    

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
            for linea in f:
                #nos saltamos las lineas iniciales e los distintos test
                if linea.startswith('Answer Sheet'):
                    print('Nueva Parte')
                    continue
                #dividimos la linea en palabras
                #tokens = linea.split[" "]
                #eliminamos los espacios para procesar la linea
                lineaSinEspacios = linea.replace(' ','')
                #print(state)
                match state:
                    case self.State.Init:
                        if lineaSinEspacios[0]== 'Q' and lineaSinEspacios[2] == ')':
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
                        if lineaSinEspacios[0] == '@' : 
                            q.addOption(statement, isCorrect)
                            isCorrect = lineaSinEspacios[1] == '@'
                            statement = linea
                        elif linea.startswith('Explanation:-') :
                            state = self.State.Explanation 
                            e = linea
                        elif lineaSinEspacios[0]== 'Q' and lineaSinEspacios[2] == ')':
                            state = self.State.Statement
                            q.addOption(statement, isCorrect)
                            self.quests.append(q)
                            statement = linea
                        else:
                            statement += ' ' + linea
                    case self.State.Explanation:
                        if lineaSinEspacios[0] == '@' : 
                            state = self.State.Option
                            q.addOption(statement, isCorrect, e)
                            isCorrect = lineaSinEspacios[1] == '@'
                            statement =  linea
                        elif lineaSinEspacios[0]== 'Q' and lineaSinEspacios[2] == ')':
                            state = self.State.Statement
                            q.addOption(statement, isCorrect, e)
                            self.quests.append(q)
                            statement = linea
                        else:
                            e = ' ' + linea  
                

    #seleciona <num> pregntas aleatorias
    def getRandomQuest(self, num : int) -> list[Quest]:
        return random.choices(self.quests, k = num)

    def __str__(self) -> str:
        string = 'Preguntas : \n'
        for q in self.quests:
            string += str(q)
        return string



def main():
    t = Test('test2.md', 'testPdf.pdf')
    r = t.getRandomQuest(4)
    for q in r:
        print(q)

main()