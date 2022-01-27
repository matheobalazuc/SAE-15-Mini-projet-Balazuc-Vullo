import requests #requests est un module python permettant d'utiliser le protocole http
from lxml import etree #pour importer le librairie html

parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] #voici la liste des différents parkings

for i in parkings: #pour un nombre quelconque (i) dans la liste des parkings 
	response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/" +i+ ".xml") #resquest.get est utilisée pour demander une ressource au serveur
	f1=open("FR_MTP_COME.txt","w", encoding='utf8') #ouverture du fichier avec un encoding utf8 qui est un codage de caractères informatiques permettant de coder l'ensemble des caractères internationaux
	f1.write(response.text) #écriture du fichier en text
	f1.close()
	tree = etree.parse("FR_MTP_COME.txt") #fonction pour analyser et créer des données XML.
	for user in tree.xpath("Name"): #le programme récupère les données dans la variable "Name"(nom du parking) du fichier .txt
		print('Nom du parking :',user.text) #le programme affiche les données dans la variable "Name"(nom du parking) du fichier .txt
	for user in tree.xpath("Free"): #le programme récupère les données dans la variable "Free"(place libre) du fichier .txt
		print('Nombre de places libres :',user.text) #le programme affiche les données dans la variable "Free"(place libre) du fichier .txt
