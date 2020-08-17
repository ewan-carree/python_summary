"""
Méthodes chaines de caractères : une chaine de caractères est immutables, chaque méthode appliquée dessus ne modifie pas la chaîne d'origine mais renvoie une copie mmodifiée de celle-ci

"""
string = "Hello, world!"

#Majuscules
string = string.upper()
print(string)

#Minuscules
string = string.lower()
print(string)

#Première lettre en majuscule
string = string.capitalize()
print(string)

#Enlever les espaces blancs de chaque coté
string = string.strip()
print(string)

#Renvoyer la position d'un caractère de la chaine
position = string.find('l')
print(position)

#Renvoyer le nombre d'occurence d'un caractère
nb = string.count('l')
print(nb)

#Remplacer un caractère d'une chaine
string = string.replace("world", "dlrow")
print(string)

#Multiplier chaine
string = string*3
print(string)

#Convertir une chaine en tableau
tableau = string.split(' ')
print(tableau)

"""
Compléter des chiffres/nombres pour qu'ils aient tous le même nombre de digit

"""
string = '5'
string = string.zfill(2)
print(string)





"""
Méthodes tableaux/listes : un tableau est mutable, chaque fonction appliquée dessus le modifie directement. Un tableau peut contenir plusieurs types différents

"""
#Obtenir dernier élément d'un tableau dont on ne connait pas la taille
dernier_elem = tableau[-1]
print(dernier_elem)

#Sélectionner des parties de tableau
first_part = tableau[:3]
second_part = tableau[3:]
print(f"first_part : {first_part} and second_part : {second_part}") #Argument directement dans la chaine avec print(f"blabla {arg}")

#Additionner listes
new_tab = first_part + second_part
print(new_tab)

#Multiplier listes:
new_new_tab = new_tab *3
print(new_new_tab)

#Insérer un élément dans une liste à un endroit précis 
tableau[1:1] = 'A'
print(tableau)

#Connaître la position d'un élément dans une liste
position = tableau.index('A')
print(position)

#Convertir tableau en chaine de caractères
string = ' '.join(tableau)
print(string)





"""
Méthodes dictionnaires : les clés peuvent être des string ou des integer

"""
dictionnaire = {"nom":"Jérome", "age":20}

#Obtenir toutes les clés
keys = dictionnaire.keys()
print(keys)

#Obtenir toutes les valeurs associées aux clés
keys = dictionnaire.keys()
print(keys)

#Obtenir un tuple des clés associées à leur valeur
both = dictionnaire.items()
print(both)





"""
Méthodes tuples :

"""





"""
Arguments facultatifs : un argument facultatif n'est pas obligé d'être précisé à l'appel de la fonction. Il est initialisé avec une valeur de base dans la fonction après les arguments obligatoires

"""

def func(age, nom="Jérome"):
	print(f"Tu as {age} ans et tu t'appelles {nom}")

func(20, "Antoine")
func(20)





"""
Gérer les exceptions : permet de ne pas stopper le programme en cas d'erreur mais de corriger cette erreur et continuer

"""

nom = "Jérome"
try:
	key = int(nom)
except ValueError:
	print("Votre nom ne peut pas être convertit en integer")
else: #done if try is ok
	print(f"Key as been validated")
finally: #always done
	print("end ...")

#Si nous ne voulons pas qu'un élément se produise nous pouvons utiliser le mot clé raise : raise Exception("Le problème")

#Créer notre propre exception : La méthode __str__ de la classe est ce qui est appelé pour afficher le message d'erreur
class MonException(Exception):
    """Exception levée dans un certain contexte… qui reste à définir"""
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message
    def __str__(self):
        """On renvoie le message"""
        return self.message





"""
Gérer une boucle : pass/break/continue

"""
#pass est une instruction vide

def func():
	"""
	Ceci est une docstring, elle permet à l'utilisateur d'en savoir plus sur la fonction en faisait help(func)
	"""
	return "j'ai retourne une phrase"

nb = 1
while nb != 20:
	if nb>6:
		break #Sort de la boucle while
	nb+=1
	if nb==5:
		continue #Retourne en haut de la boucle sans éxécuter ce qui suit	
	print(nb)





"""
Vérifier des conditions sur les variables avant de les utiliser :

"""
b = 3
assert isinstance(b, int)





"""
Portée des variables :

"""
a = b = 5
print(f"a = {a} et b = {b}")
def modify(b):
	global a #global permet de modifier une variable se trouvant en dehors d'une fonction
	a*=2
	b*=2

modify(b)
print(f"a = {a} et b = {b}")





"""
True/False : Tout ce qui est différent de 0 peut être considérer comme une condition équivalente à True

"""
a = "Salut"
b = 0
if a:
	print("a fonctionne")
else:
	print("a ne fonctionne pas")

if b:
	print("b fonctionne")
else:
	print("b ne fonctionne pas")











"""
Importer un module d'un autre répertoire dans le répertoire courant

Exemple d'arbre :
Main/
	main.py
	Test/
		tes.py


import sys
sys.path.append("./Test")
import test #le fichier .py servant comme module

"""





"""
Map function : permet d'appliquer efficacement une fonction sur chaque élément d'une liste

"""
liste = [1,2,3]
def map_function(x):
	return x**x
mapped_list = list(map(map_function,liste)) #On ne met pas de () pour la fonction en argument
print(f"before : {liste} and now : {mapped_list}")





"""
Filter function : permet de filtrer efficacement chaque élément d'une liste

"""
def filter_function(x):
	return x%2!=0
filtered_list = list(filter(filter_function,liste))
print(f"before : {liste} and now : {filtered_list}")





"""
List comprehension : équivalent de map et filter function combinées mais en beaucoup plus clair

"""
new_list = [map_function(x) for x in liste if x%2!=0]
print(f"before : {liste} and now : {new_list}")





"""
Astuce pour éviter de devoir utiliser math pour avoir le nombre entier d'une division

"""

print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")





"""
Boucle for enumerate : utile pour avoir chaque élément d'une liste associé à leur position, le tout sous forme d'un tuple

"""
liste = ['a', 'b', 'c']
for index, elem in enumerate(liste):
	print(f"{elem} at position {index}")





"""
Fonction qui acceptent un nombre inconnu de paramètre : def func(*en_tuple, **en_dictionnaire):

"""
def parameters(*args, **kwargs):
	print(f"I received these unnamed args : {args}")
	print(f"I received these named args : {kwargs}")
parameters(1,"azerty",[1,2], couleur="rouge", taille_en_cm=172)
both



"""
Ecrire les nombres longs de façon plus claire
"""
nb = 1_000_000
print(nb)





"""
Conditions if/else plus claire

"""
conditions = False

#Mauvaise solution :

if conditions:
	x=1
else:
	x=0
print(x)

#Bonne solution
x = 1 if conditions else 0
print(x)





"""
Associer des éléments de deux listes : zip()

"""
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heroes = ["Spiderman", "Superman", "Deadpool", "Batman"]
universes = ["Marvel", "DC", "Marvel", "DC"]

for name, hero, universe in zip(names, heroes, universes):
	print(f"{name} is actually {hero} from {universe}")





"""
ignorer une variable unpackée

"""
my_tuple = (1,2)
my_tuple2 = (1,2,3,4,5)
#unpack :
a, b = my_tuple
print(f"{a} and {b}")

#We don't need b :
a, _ = my_tuple
print(a)

#Another exemple :
for _ in range(2):
	print("I d'ont care about i")

#Another exemple :
a, b, *_ = my_tuple2 #On ignore tout ce qui suit les 2 premières variables, le reste est stocké dans une liste
a, b, *c, d = my_tuple2 
print(f"{a}, {b}, {c}, {d}")





"""
Entrer un mpd de façon sécurisée en input :

"""
from getpass import getpass
password = getpass("Password : ")
print(password)





"""
lambda function

"""
def equivalent_lambda(x):
	return x+5
real_lambda = lambda x : x+5
print(f"equivalent_lambda : {equivalent_lambda(5)} and real_lambda : {real_lambda(5)}")





"""
Inspecter le code source d'un élément

"""
import inspect
from queue import Queue
#print(f"Code source : \n{inspect.get_source(Queue)}")





"""
Decorators : utile pour qualifier une fonction ou une classe et effectuer des tests généraux dessus

"""
import time
def timer(func):
	def wrapper(*args, **kwargs):
		start = time.time()
		rv = func(*args, **kwargs)
		total = time.time() - start
		print("Time to execute : "+ str(total))
		return rv
	return wrapper

@timer #on peut chainer plusieurs décorateurs à la suite 
def exemple(x):
	string = "je suis "+str(x)
	return string
result = exemple(5)
print(result)





"""
Generators : utile pour économiser de la mémoire lors de parcours de grandes listes

"""
def square(n):
	num = 0
	while True:
		yield num
		if num == n:
			return
		else:
			num+=1
for i in square(100):
	print(i*i, end = " - ")
print()





"""
Connaitre la mémoire utilisée par une variable

"""
import sys
var = [1]*100
print(f"mémoire utilisée par var : {sys.getsizeof(var)} bytes")










"""
Class

"""
"""
Héritage / Multiple inheritance

"""
class Dog:
	def __init__(self, age):
		self.age = age
class Cat(Dog):
	"""Cat hérite de Dog : elle possède ses fonctions et méthodes"""
	def __init__(self, age, nom):
		super().__init__(age)
		self.nom = nom

#multiple
class Animal(object):
	pass
class DessinAnime(object):
	pass
class Hamtaro(Animal, DessinAnime): #We can add more than two parent classes
	pass






"""
Dunder methods / Surcharge opérateurs

"""
class Point(object):
	def __init__(self, x=0,y=0):
		self.x = x
		self.y = y
		self.conteneur = [1,2,3,4,5,6,7]
		self.__my_private_attr = "Je suis privé"

	def __str__(self):
		print("I'm the class Point")

	def __add__(self, p):
		"""la fonction add surcharge l'opérateur +"""
		return Point(self.x + p.x, self.y + p.y)

#	def __getattr__(self, name):
#		print(f"{name} didn't found")

	def __setattr__(self, name, value):
		"""On modifie la classe mère directement plutôt que seulement appeler setaatr de cette classe et tourner en boucle sur la même méthode"""
		object.__setattr__(self, name, value) #Chaque classe crée hérite de base de la classe object

	def __delattr__(self, name):
		print(f"Deleting {name} ...")

	def __getitem__(self, index):
		return self.conteneur[index]

	def __setitem__(self, index, value):
		self.conteneur[index] = value

	def __contains__(self, value): # 8 in ma_liste  <==>  ma_liste.__contains__(8)
		return True if value in self.conteneur else False

	def __len__(self):
		return len(self.conteneur)

	"""Autres surcharges : 

	__sub__(self,p) : -
	__mul__(self,p) : *
	__truediv__(self, p) : /
	__floordiv__(self, p) : //
	__mod__(self, p) : %
	__pow__(self, p) : **

	__gt__(self,p)  : >
	__ge__(self,p) 	: >=
	__lt__(self,p)  : <
	__le__(self,p)  : <=
	__eq__(self,p) : == 

	__iadd__(self,p) : +=
	__isub__(self,p) : -=
	__imul__(self,p) : *=
	__itruediv__(self, p) : /=	
	"""





"""
Méthodes static/class

"""
class StaticClass:
	nb_class=0
	def __init__(self):
		print("une nouvelle classe vient d'être créée")
		nb_class+=1
	
	@classmethod
	def ma_func(cls): #pas de self, obligatoirement cls
		"""Agit avec les variables de la classe"""
		return cls.nb_class

	@staticmethod
	def ma_func2(arg1, arg2):#pas de self
		"""N'agit pas avec les composants de la classe mais est quand même en lien avec la classe"""
		return arg1 + arg2





"""
See every methods from a class / See every attributs from class

"""
ma_class = Point()
print(dir(ma_class))
print(ma_class.__dict__)
print(ma_class.__my_private_attr)





"""
Property : permet d'offrir des accesseurs et mutateurs pour définir un attribut privé

La méthode donnant accès à l'attribut

La méthode modifiant l'attribut

La méthode appelée quand on souhaite supprimer l'attribut

La méthode appelée quand on demande de l'aide sur l'attribut

"""
class Test(objet):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self._dimension = 2 #Attribut privé

	def _get_dimension(self):
		return self._dimension

	def _set_dimension(self,value):
		self._dimension = value
		
	dimension = property(_get_dimension, _set_dimension) # lorsqu'on appelera objet.dimension, property redirigera vers les accesseurs/mutateurs privés




