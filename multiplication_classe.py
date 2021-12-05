from math import*
import random
class Multiplication(object):
    
    def __init__(self):
        
        nombreDePoint=0
        
    def choisirUneTable(self):
        
        test=0
        while not test:
            try:
                self.reponse = int(input("Choisis une table: "))
                test=1
            except:
                print("Il faut mettre un chiffre!")
                
    def calculer(self):
        
        multiplicateur=random.randint(1,10)
        self.calcul = self.reponse*multiplicateur
        reponsejoueur= input("Calcule "+str(self.calcul))

exo=Multiplication()
exo.choisirUneTable()
exo.calculer()
