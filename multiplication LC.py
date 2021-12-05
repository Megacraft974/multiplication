############################
# programme permettant de  #
# reviser ses tables de    #
# multiplications (1 a 10) #
############################

import random
from math import *
#from fichier1 import *
compteur = 0                                     
#la machine demande au joueur quelle table il veut reviser
#la machine verifie que ce marchand de tapis de joueur n'a pas esayer de planter le programme avec une lettre
Test = 0                                                                                           
while not Test:                                                                                    
    try:                                                                                           
        table = int(input ("Quelle table veux tu reviser ? La table de: "))                                                                          
        Test = 1                                                                                   
    except ValueError :                                                                            
        print("Marchand de tapis! Il faut saisir un chiffre!")
#tant que la table que le joueur veut reviser est 1 la machine lui dit de prendre une autre table
while (table == "1"):                                                                             
    print ("Sapajou ! Tu te fiches de ma tete ou quoi ?Tu vas pas reviser la table de 1 ?")         
    table = input ("Ecris une autre table.")                                                      
#la machine traduit la table (lettre) en chiffre    
table = int(table)                                                                                
#la machine repetera en dix fois le programme pour calculer une multiplication
for x in range(1,10):                                                                             
    #la machine genere un chiffre au hasard
    multiplicateur = random.randint(2,10)                                                         
    #la machine calcule le resultat de l'operation
    resultat = table*multiplicateur                                                               
    
    message = "Calcule "+ str(table) +" x "+ str(multiplicateur) + " = "                          
    #la machine demande au joueur de calculer le resultat de la multiplication
    #la machine verifie que cet espece de marchand de tapis n'a pas essayer de planter le programme
    Test = 0                                                                                      
    while not Test:                                                                               
        try:                                                                                      
            resultatdujoueur = int(input (message))                                               
            Test = 1                                                                              
        except ValueError :                                                                       
            print("Bachibouzouk ! Il faut saisir un chiffre.")                                    
    #la machine compare son resultat et celui du joueur           
    if resultat == resultatdujoueur:                                                              
        #la machine compte les points du joueur
        compteur = compteur + 1                                                                   
#la machine affiche les points du joueur         
notedespointsdujoueur = ["Tu aurais pu faire mieux.", "C'est pas bien du tout.", "Ca ira.", "C'est bien.", "C'est tres bien!"]  
print("Tu as eu ",compteur," points.") 


while(compteur < 2):
    compteur = compteur + 1
compteur2 = int((compteur/2)-1)
print(notedespointsdujoueur[compteur2])

#ecrire_fichier(compteur,"score.txt")
