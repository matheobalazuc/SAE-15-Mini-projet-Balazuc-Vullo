import requests                                    #Fournit le protocole http
import time                                        #Fournit un tas de fonction liés au temps
from lxml import etree                             #Fournit la librairie html
from time import sleep                             #On import la fonction "sleep" depuis "temps" 

bike=20
		
for i in range(bike):                                 #Définition de la fonction qui va ouvrir le fichier des données sur le vélo.
	response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")     #Sert à demander une ressource au serveur.
	f1=open("vélo.txt","w", encoding='utf8')       #Ouvre le fichier velo.txt en écriture en utf8
	f1.write(response.text)                        #On écrit dans le fichier en text
	f1.close()                                     #On ferme le fichier
	
	f1=open("vélo_résultat.txt","a", encoding='utf8')                 #Créer la variable tree qui est égal à l'analyse et création de données du fichier contenant toutes les informations sur les vélos dans le fichier velo.txt
	tree = etree.parse("vélo.txt")
	for user in tree.xpath("/vcs/sl/si"):         #Boucle qui va récupérer les données dans le fichier de données des vélos dans les balises html vcs/sl/si .   #Ouvre un fichier texte nommé velo.txt en écriture en utf8
		f1.write(f"Nom de la station : ")                       #Ecrit dans le fichier le temps 
		f1.write(user.get("na"))                   #Ecrit dans le fichier les données de "fr", donc les places disponibles.
		f1.write("\n")
		f1.write(f"Places libres : ")                       #Ecrit dans le fichier le temps 
		f1.write(user.get("fr"))                   #Ecrit dans le fichier les données de "fr", donc les places disponibles.
		f1.write("\n")
		f1.write(f"Places occupées : ")                       #Ecrit dans le fichier le temps 
		f1.write(user.get("av"))                   #Ecrit dans le fichier les données de "fr", donc les places disponibles.
		f1.write("\n")
		f1.write(f"Nombre de places totales : ")                       #Ecrit dans le fichier le temps 
		f1.write(user.get("fr"))                   #Ecrit dans le fichier les données de "fr", donc les places disponibles.
		f1.write("\n") 
		f1.write("\n")                            #Permet d'aller à la ligne dans l'écriture du fichier
		  
		                       #On ferme le fichier
                                  #On utilise la fonction parse
	