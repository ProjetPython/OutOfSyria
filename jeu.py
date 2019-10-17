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

