from contour import *
from amir import *
from choix import *

def main():
	amir = Amir()
	contour("Je m'appelle "+amir.prenom+" et j'ai "+str(amir.age)+" ans. A cause des conflits qui se trouvent en Syrie, j'ai décidé de m'enfuir avec ma famille")
	choix1(amir)
	choix2(amir)
	choix3(amir)
	choixBateau(amir)
if __name__ == '__main__':
	main()

