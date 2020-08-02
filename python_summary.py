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
values = dictionnaire.values()
print(values)

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
finally:
	key = 0

#Si nous ne voulons pas qu'un élément se produise nous pouvons utiliser le mot clé raise : raise Exception("Le problème")





"""
Gérer une boucle : pass/break/continue

"""
#pass peret de ne rien faire
def func():
	"""
	Ceci est une docstring, elle permet à l'utilisateur d'en savoir plus sur la fonction en faisait help(func)
	"""
	pass

nb = 1
while nb != 10:
	if nb>10:
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
Compléter des chiffres/nombres pour qu'ils aient tous le même nombre de digit

"""
string = '5'
string = string.zfill(2)
print(string)





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


