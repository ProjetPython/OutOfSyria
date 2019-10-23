from tkinter import *

fenetre = Tk()
fenetre.title("Out Of Syria")

def jeu():
    fenetre = Tk()
    champ_label = Label(fenetre, text="Aujourd'hui, c'est le grand jour. J'ai réveillé ma famille à 5h du matin afin de m'enfuir.")
    champ_label.pack()
    champ_label = Label(fenetre, text="J'ai pris mon téléphone et des vivres. Il me reste de la place pour un objet")
    champ_label.pack()
    bouton_choix1 = Button(fenetre, text="Prendre une batterie", command =choix1)
    bouton_choix2 = Button(fenetre, text="Prendre des médicaments", command = "")
    bouton_choix3 = Button(fenetre, text="Prendre de l'argent", command = "")
    bouton_choix1.pack()
    bouton_choix2.pack()
    bouton_choix3.pack()

def choix1():
    fenetre = Tk()
    champ_label = Label(fenetre, text="En sortant de chez nous, ma fille me demande quelle trajet allons nous faire. Ma femme essaya de me persuader en voulant partir à Beyrouth pour le bateau et arriver en Grèce.")
    champ_label.pack()
    bouton_choix1 = Button(fenetre, text="Aller en bus en traversant la Syrie", command = "")
    bouton_choix2 = Button(fenetre, text="Aller jusqu'à Beyrouth", command = "")
    bouton_choix3 = Button(fenetre, text="Aller à l'aéroport de Damas", command = avion)
    bouton_choix1.pack()
    bouton_choix2.pack()
    bouton_choix3.pack()

def avion():
    fenetre = Tk()
    champ_label = Label(fenetre, text="On décide d'aller à l'aéroport de Damas. Heuresement que ce n'est pas loin de chez moi. Pour cela, on prends le taxi. Manque de chance, on tombe sur un barrage" )
    champ_label.pack()
    bouton_choix1 = Button(fenetre, text="Essayer de convaincre la police", command = "")
    bouton_choix2 = Button(fenetre, text="Verser un pot-de-vin à la police", command = "")
    bouton_choix3 = Button(fenetre, text="Essayer de forcer le passage", command = "")
    bouton_choix1.pack()
    bouton_choix2.pack()
    bouton_choix3.pack()
    
    

champ_label = Label(fenetre, text='Out Of Syria')
champ_label.pack()
bouton_jeu = Button(fenetre, text='Jouer', command = jeu)
bouton_jeu.pack()
fenetre.mainloop()
