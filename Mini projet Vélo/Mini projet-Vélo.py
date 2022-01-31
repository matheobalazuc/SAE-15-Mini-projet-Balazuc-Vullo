import requests                                    #Fournit le protocole http
import time                                        #Fournit un tas de fonction liés au temps
from lxml import etree                             #Fournit la librairie html
from time import sleep                             #On import la fonction "sleep" depuis "temps" 

		

def makerequest():                                 #Définition de la fonction qui va ouvrir le fichier des données sur le vélo.
	response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")     #Sert à demander une ressource au serveur.
	f1=open("velo.txt","w", encoding='utf8')       #Ouvre le fichier velo.txt en écriture en utf8
	f1.write(response.text)                        #On écrit dans le fichier en text
	f1.close()                                     #On ferme le fichier
	
def parse():                                       #Définition de la fonction parse qui va écrire dans un fichier texte tous les parkings vélos avec l'heure avec le nombre de place à coté disponibles. 
	tree = etree.parse("velo.txt")                 #Créer la variable tree qui est égal à l'analyse et création de données du fichier contenant toutes les informations sur les vélos dans le fichier velo.txt
	for user in tree.xpath("/vcs/sl/si"):          #Boucle qui va récupérer les données dans le fichier de données des vélos dans les balises html vcs/sl/si .
		temps=time.time()                          #Créer la variable temps qui est égal au nombre de seconde passés depuis le 1er Janvien 1970.
		temps=time.ctime(temps)                    #Créer la fonction temps qui est égal à la date au format texte d'aujourd'hui (.c)
		f1=open("velo.txt","a", encoding='utf8')   #Ouvre un fichier texte nommé velo.txt en écriture en utf8
		f1.write(f"Place libres à {temps} :")                       #Ecrit dans le fichier le temps 
		f1.write(user.get("fr"))                   #Ecrit dans le fichier les données de "fr", donc les places disponibles.
		f1.write("\n")                             #Permet d'aller à la ligne dans l'écriture du fichier
		f1.close()                                 #On ferme le fichier.

for i in range(3):                #Boucle qui se repetera 2 fois et qui fera les 2 fonctions citées au dessus. 
	print("Test" ,i)              #On affiche test chaque fois que la fonction marche et recommence.
	makerequest()                 #On utilise la fonction makerequest
	parse()                       #On utilise la fonction parse
	time.sleep(3600)                 #Signifie le nombre de secondes que le programme va attendre avant de recommencer.
