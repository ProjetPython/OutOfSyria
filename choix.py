from contour import *
from amir import *
import time
def choix1(amir):
	print("Aujourd'hui, c'est le grand jour. J'ai réveillé ma famille à 5h du matin afin de m'enfuir.")
	print("J'ai pris mon téléphone et des vivres. Il me reste de la place pour un objet")
	print()
	print("1) Prendre une batterie")
	print("2) Prendre des médicaments")
	print("3) Prendre de l'argent")
	print()
	choix = input("Votre choix : ")
	print()
	if(choix == "1") : 
		amir.batterie = True
		print("Une batterie de secours peux me servir.")
	if(choix == "2") :
		amir.medicaments = True
		print("Prendre des médicaments peux s'avérer utile.")
	if(choix == "3") :
		amir.argent = True
		print("Avoir de l'argent peux nous aider à la frontière")
	print()
	

def choix2(amir):
	print("En sortant de chez nous, ma fille me demande quelle trajet allons nous faire. Ma femme essaya de me persuader en voulant partir à Beyrouth pour le bateau et arriver en Grèce.")
	print()
	print("1) Aller en bus en traversant la Syrie")
	print("2) Aller jusqu'à Beyrouth")
	print("3) Aller à l'aéroport de Damas")
	print()
	choix = input("Votre choix : ")
	print()
	if(choix == "1") : 
		amir.bus = True
		print("Prendre le bus est la solution la plus sécurisée")
	if(choix == "2") :
		amir.bateau = True
		print("Prendre le bateau est la solution la plus rapide pour fuir le pays")
	if(choix == "3") :
		amir.avion = True
		print("J'espère qu'on aura pas de problème à la douane")
	print()

def choix3(amir):
	if(amir.avion):
		print("On décide d'aller à l'aéroport de Damas. Heuresement que ce n'est pas loin de chez moi. Pour cela, on prends le taxi. Manque de chance, on tombe sur un barrage")
		print()
		print("1) Essayer de convaincre la police")
		print("2) Verser un pot-de-vin à la police")
		print("3) Essayer de forcer le passage")
		print()
		choix = input("Votre choix : ")
		if(choix == "1"):
			print()
		if(choix == "2" and amir.argent):
			print("J'ai donné l'argent que j'avais mis de côté. Maintenant, je n'ai plus un sou")
			amir.argent=False
		if(choix == "2" and not amir.argent):
			print("")

from random import *
def choixBateau(amir):
	if(amir.bateau):
		print ("On décide de prendre le bateau")
		print ("On peut prendre le bateau qui part à Athènes ou on pourrait rejoindre des amis que je connais, mais il y aurait une tempète")
		print ("Où, prendre le bateau qui part à Chypres et rejoindre mes amis plus tard")
		print()
		print("1) Prendre le bateau qui part à Chypre")
		print("2) Prendre le bateau qui part à Athènes")
		choix = input("Votre choix : ")
		hasard = [0, 1]

		if choix == '1':
			print ("Nous avons pris le bateau pour Chypres donc nous rejoindrons nos amis plus tard")
			amir.bateau_chypre=True
		if choix == '2':

			print ("Nous avons pris le bateau pour Athenes!")
			chance = choice(hasard)
			if chance == 0:
				print("Pas de chance, vous avez perdu !!!")
			if chance == 1:
				print("Vous avez de la chance, vous allez arriver en grece !!!")
				amir.bateau_athenes = True

def arriveGrece(amir):
	if amir.bateau_athenes == True:
		print("Nous avons reussi à fuire la Syrie !!!")
		print("Allons rejoindre nos amis")
		print("")


def arriveChipre(amir):
	if (amir.bateau_chypre):
		print("Al Hamdoulillah, nous avons fuit la Syrie")