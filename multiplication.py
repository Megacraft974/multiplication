# -*- coding: utf-8 -*-


from tkinter import *




#---------------------------------------------------------------------------------------------------------------





def page_accueil():#affiche la page d'accueil

    # Cree la fenetre
    fen1 = Tk()
    
    # Insere une photo
    can = Canvas(fen1,bg="dark grey",height=500,width=500)
    photo = PhotoImage(file ='12.gif')
    item = can.create_image(256,256,image = photo)
    can.pack(side =LEFT)

    # Insere un bouton 'Jouer'
    bou1 = Button(fen1, text="Jouer",command = page_acueil2)
    bou1.pack(side =TOP, padx =3, pady =3)

    #Insere un bouton 'Changer les paramètres'
    bou2 = Button(fen1, text="Changer les paramètres",command = page_acueil3)
    bou2.pack(side =TOP, padx =3, pady =3)

    #Insere un bouton 'Quitter'
    bou3 = Button(fen1,text="Quitter",command = fen1.destroy)
    bou3.pack(side =BOTTOM, padx =3, pady =3)

    #Recommencez jusqu'a ce que la souris clique
    fen1.mainloop()




#-------------------------------------------------------------------------------------------------------------------





    

def reglages():#affiche la page de réglages
    #Cree la fenetre
    fen2 = Tk()

    
    #Insere une phrase
    tex1 = Label(fen2,text = "Quelle table veut tu réviser ?",fg = "blue")
    tex1.pack(side = TOP, padx =3, pady =3)
    
    #Insere un espace de saisie
    table = Entry(fen2)
    table.pack(side = TOP, padx =3, pady =3)
    
    #Insere un bouton 'Retour'
    bou4 = Button(fen2, text="Retour",command = page_accueil)
    bou4.pack(side = BOTTOM, padx =3, pady =3)
    
    #Insere un bouton 'Valider'
    bou5 = Button(fen2,text="Valider",command = "")
    bou5.pack(side = BOTTOM, padx =3, pady =3)

    #agrandissement de la fenetre
    fen2.geometry("500x500")

    
    #Recommencez jusqu'a ce que la souris clique
    fen2.mainloop()




#--------------------------------------------------------------------------------------------------------------------------


class page_de_jeu(object):
    
    
    def phrase(question):
        #Insere une phrase
        tex2 = Label(self.fen3,text = "Calcule ... x ... .",fg = "blue")
        tex2.pack(side = TOP)
        

    def affiche(self):      #Affiche le jeu
        
        #Cree la fenetre
        fen3 = Tk()

        
        #Insere une phrase
        self.phrase()
        
        #Insere un espace de saisie
        message = Entry(fen3)
        message.pack(side = TOP, padx =3, pady =3)
        
        #Insere un bouton 'Valider'
        bou6 = Button(fen3,text="Valider",command = "")
        bou6.pack(side = BOTTOM, padx =3, pady =3)

        bou9 = Button(fen3,text="suivant",command = score)
        bou9.pack(side = BOTTOM,padx =3, pady =3)

        #agrandis la fenetre
        
        
        #Recommencez jusqu'a ce que la souris clique
        fen3.mainloop()


        





#-------------------------------------------------------------------------------------------------------------------------------








    

def score():#Affiche les score
    
    #Cree la fenetre
    fen4 = Tk()
    
    #Insere une photo
    #can = Canvas(fen4,bg="dark grey",height=500,width=500)
    #photo = PhotoImage(file ='12.gif')
    #item = can.create_image(256,256,image = photo)
    #can.pack(side =RIGHT)
    
    #Insere une phrase
    tex3 = Label(fen4,text = "Tu as eu ... bonnes réponses",fg ="green")
    tex3.pack(side = TOP, padx =3, pady =3)
    
    #Insere une phrase
    tex4 = Label(fen4,text = "Tu as eu ... mauvaises réponses",fg ="red")
    tex4.pack(side = TOP, padx =3, pady =3)
    
    #Insere une phrase
    tex3 = Label(fen4,text = "C'est bien ou très biens ...",fg ="blue")
    tex3.pack(side = TOP, padx =3, pady =3)
    
    #Insere un bouton
    bou7 = Button(fen4,text = "Rejouer",command = page_accueil)
    bou7.pack(side= BOTTOM, padx =3, pady =3)
    
    #Insere un bouton
    bou8 = Button(fen4,text = "Quitter",command =fen4.destroy)
    bou8.pack(side = BOTTOM ,padx =3, pady =3)
    
    #Recommencez jusqu'a ce que la souris clique
    fen4.mainloop()



    


#----------------------------------------------------------------------------------------------------------------------------------

def page_acueil2():

    reglages()

    fen1.destroy()
#-----------------------------------------------------------------------------------------------------------------------------------


def page_acueil3():

    page_de_jeu()

    fen1.destroy()
#------------------------------------------------------------------------------------------------------------------------------------

def reglages2():

    page_acueil()

    fen2.destroy()



#MaFenetre = page_de_jeu()
#MaFenetre.affiche()


