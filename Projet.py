class Amir():
	"""docstring for ClassName"""
	def __init__(self):
		self.prenom = "Amir"
		self.age =30
		self.ville="Damas"
		self.ptVie=100

def contour(phrase):
	for i in range(len(phrase)+2):
		print("-",end='')
	print()
	print("|"+phrase+"|")
	for i in range(len(phrase)+2):
		print("-",end='')
	print()


def main():
	amir = Amir()
	contour("Je m'appelle "+amir.prenom+" et j'ai "+str(amir.age)+" ans. A cause des conflits qui se trouvent en Syrie, j'ai décidé de m'enfuir avec ma famille")
	
if __name__ == '__main__':
	main()
###############################################################################################################################
print('Vous arrivez devant un barrage militaire.Vous pouvez sois tenter de le passer sois vous cherchez un autre chemin.\n')
print('1:Franchir le barrage')
print('2:Trouver un autre chemin')
choix1 = int(input())
choix = 'batterie'
item = None
if choix1 == 1:
    print('Vous avez décider de franchir le barrage. Malheureuresement vous avez laissé tomber votre ',choix)
    print('Par chance vous trouver une caisse à outils près d\'une maison detruite')
    item ='Caisse à outils' 
else:
    print('Vous jouez la carte de la prudence et vous décidez de trouver un autre itiniraire')
################################################################################################################################
choix1 = None
print('Après avoir roulé pendant plusieurs heures, votre véhicules commence à fumer et s\'arrête.\n')
print('1:Décider de réparer le véhicule')
print('2:Abandonner le véhicule et marcher avec votre famille')

choix1 = int(input())

if choix1 == 1 and item != None:
    print('Vous avez décider de réparer le véhicule il est comme neuf')
    option = 1
    item = None
else:
    option = 0
    choix1 = None
    print('Vous décidez d\'abandonner le véhicule. Malheureusement vous devez abandonner des affaires pour garder la caisse à outils.\n')
    print('1:Abandonner la caisse à outils')
    print('2:Abandonner des valises')
    choix1 = int(input())
    if choix1 == 1:
        item = None
    else :
        item = 'Caisse à outils'
################################################################################################################################
choix1 = None
if option == 1:
    print('Vous approcher avec votre voiture d\'une station de bus,et vous vous demander si le bus serai pas une bonne option')
    print('1: Prendre le bus')
    print('2: Continuer en voiture')
    
    choix1 = int(input())
    if choix1 == 1:
        print('Vous décidez de prendre le bus mais vous perdez toute vos affaires')
        item = None
    else:
        print('Vous décidez de continuer en voiture')
        item = 'Caisse à outils'
else:
    print('Vous avez pas le choix et prenez un bus')
    item = None
###############################################################################################################################
option = 0
choix1 = None
print('Pendant la suite du trajet, vous voyez par la fenêtre un groupe de rebelle local')
print('1: Continuer sur la route')
print('2: Sortir du véhicule et fuir')
choix1 = int(input())
if choix1 == 1:
    print('Vous êtes resté dans le bus mais le groupe de rebelle vous kidnappée vous et votre famille')
    print('Par chance vous récupérer une arme sur un des rebelles')
    item = 'arme'
    choix1 = None
    option +=1
else:
    print('Vous avez sûrement bien fait d\éviter un potentielle affrontement')
    choix1 = None
##############################################################################################################################

def choixRebelle():
    print('Cela fait plusieur jour que vous et votre famille êtes enfermé avec ces rebelles')
    print('1: Tenter de négocier')
    print('2: Obéir à leurs odres et attendre')
    choix = int(input())
    if choix == 1:
        print('Vous tenter une approche avec les rebelles mais ils ont pas l\'air d\être d\'accord')
        print('Vous rester avec votre famille et prier les dieux de vous sortir')
    else:
        print('Vous rester avec votre famille et prier les dieux de vous sortir')
    


if option == 1:
    print('Les rebelles vous ramène à leur camps et vous pouvez sortir uniquement par la force')
    print('1: Les affronter')
    print('2: Rester tranquille et attendre')
    choix1 = int(input())
    if choix1 == 1 :
        print('C\'est un échec, les rebelles vous subtilise votre arme ')
        item = None
    else:
        item = 'armes'
##############################################################################################################################





            
        
    
    
