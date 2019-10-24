from tkinter import *
from random import *

fenetre = Tk()
fenetre.title("Out Of Syria")

class OutOfSyria():

    def __init__(self):
        
        self.argent = 0
        self.item = 0
        self.arme = 0
        
    def aleatoire(self):
        hasard = [0,1]
        chance = choice(hasard)
        if chance == 0:
            fenetre = Tk()
            champ_label1 = Label(fenetre, text="Une tempête éclate et vous et votre famille périssez")
            champ_label1.pack()
            champ_label2 = Label(fenetre, text="Game Over ")
            champ_label2.pack()
            bouton_fin = Button(fenetre, text="Revenir au menu", command = partie.accueil)
            bouton_fin.pack()
        
    
    def jeu(self):
        fenetre = Tk()
        champ_label = Label(fenetre, text="Aujourd'hui, c'est le grand jour. J'ai réveillé ma famille à 5h du matin afin de m'enfuir.")
        champ_label.pack()
        champ_label = Label(fenetre, text="J'ai pris mon téléphone et des vivres. Il me reste de la place pour un objet")
        champ_label.pack()
        bouton_choix1 = Button(fenetre, text="Prendre une batterie", command = partie.choix)
        bouton_choix2 = Button(fenetre, text="Prendre des médicaments", command = partie.choix)
        bouton_choix3 = Button(fenetre, text="Prendre de l'argent", command = partie.choix)
        bouton_choix1.pack()
        bouton_choix2.pack()
        bouton_choix3.pack()


    def choix(self):
        fenetre = Tk()
        champ_label = Label(fenetre, text="En sortant de chez nous, ma fille me demande quelle trajet allons nous faire. Ma femme essaya de me persuader en voulant partir à Beyrouth pour le bateau et arriver en Grèce.")
        champ_label.pack()
        bouton_choix1 = Button(fenetre, text="Aller en bus en traversant la Syrie", command = "")
        bouton_choix2 = Button(fenetre, text="Aller jusqu'à Beyrouth", command = partie.bateau)
        bouton_choix3 = Button(fenetre, text="Aller à l'aéroport de Damas", command = partie.avion)
        bouton_choix1.pack()
        bouton_choix2.pack()
        bouton_choix3.pack()

    def bateau(self):
        fenetre = Tk()
        champ_label = Label(fenetre, text="On décide de prendre le bateau")
        champ_label.pack()
        champ_label2 = Label(fenetre, text="On peut prendre le bateau qui part à Athènes ou on pourrait rejoindre des amis que je connais, mais il y aurait une tempète")
        champ_label.pack()
        champ_label3 = Label(fenetre, text="Où, prendre le bateau qui part à Chypres et rejoindre mes amis plus tard")
        champ_label.pack()
        bouton_choix1 = Button(fenetre, text="Prendre le bateau qui part à Chypre", command = "")
        bouton_choix2 = Button(fenetre, text="Prendre le bateau qui part à Athènes", command = partie.aleatoire)
        bouton_choix1.pack()
        bouton_choix2.pack()


    def avion(self):
        fenetre = Tk()
        champ_label = Label(fenetre, text="On décide d'aller à l'aéroport de Damas. Heuresement que ce n'est pas loin de chez moi. Pour cela, on prends le taxi. Manque de chance, on tombe sur un barrage" )
        champ_label.pack()
        bouton_choix1 = Button(fenetre, text="Essayer de convaincre la police", command = "")
        bouton_choix2 = Button(fenetre, text="Verser un pot-de-vin à la police", command = "")
        bouton_choix3 = Button(fenetre, text="Essayer de forcer le passage", command = "")
        bouton_choix1.pack()
        bouton_choix2.pack()
        bouton_choix3.pack()
        
    
    def accueil(self):
        champ_label = Label(fenetre, text='Out Of Syria')
        champ_label.pack()
        bouton_jeu = Button(fenetre, text='Jouer', command = partie.jeu)
        bouton_jeu.pack()
        fenetre.mainloop()

partie = OutOfSyria()    
partie.accueil()
