#Importation des librairies.
from encodings import utf_8
import requests
from lxml import etree
import time
#import Pygnuplot    #ca marche pas ca la 

#Liste des parkings.
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB',
'FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT', 'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC',
'FR_MTP_SABI','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109',
'FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY']


#Création liste avec des données exploitables definitive.
DATA = []

#Boucle infinie.
x = 2
while x > 1:

#Suppression des ancien fichiers
        file = open("DonnéesPlaces.txt", "w")
        file.close()
        file = open("DonnéesParkings.txt", "w")
        file.close()
        file = open("PlacesTotal.txt", "w")
        file.close()
        file = open("PlacesLibre.txt", "w")
        file.close()
        file = open("DonnéesPourcentages.txt", "w")
        file.close()
        file = open("DonnéesUtilisateur.txt","w")
        file.close()

#Début boucle récupération données
        for i in range (len(parkings)):

#Récupere les données.
            liens="https://data.montpellier3m.fr/sites/default/files/ressources/"+parkings[i]+".xml"
            response=requests.get(liens)

#S'assure que les données reçus soit utilisable en regardant le code status.
            Status = response.status_code
            print(Status)

#Si code status égale à 200, alors il n'y a pas d'erreur les données sont exploité.
            if Status == 200:

#Crée la liste de donnée exploitable temporaires.
                DATA2 = []

#Crée un fichier de données brutes par parking.
                f1=open(parkings[i]+".txt","w", encoding='utf8')
                f1.write(response.text)
                f1.close()

#Met toute les données brutes des parkings dans un seul fichiers.
                f1=open("DonnéesParkings.txt","a", encoding='utf8')
                f1.write(response.text)
                f1.close()

#Recherche dans le fichier XML du parking sont nom.
                tree = etree.parse(parkings[i]+".txt")
                for user in tree.xpath("Name"):
                    print('Nom du parking :',user.text)

#Ajout des données dans la liste DATA2 temporaire.
                    DATA2.append(user.text)

                    f1 = open("DonnéesUtilisateur.txt", "a")
                    f1.write(f"Nom = "+parkings[i]+"\n")
                    f1.close()

#Recherche dans le fichier XML du parking actuel les places total.
                for user in tree.xpath("Total"):
                    Place_Total = user.text
                    print('Nombre total de places :',user.text)

#Ajout des données dans la liste DATA2 temporaire.
                    DATA2.append(user.text)

#Enregistrement des place total dans un ficher exploitable.
                    f1=open("PlacesTotal.txt","a", encoding='utf8')
                    f1.write(user.text+'\n')
                    f1.close()
#Enregistrement des places total dans le .txt utilisateur.
                    f1 = open("DonnéesUtilisateur.txt", "a")
                    f1.write(f"Place aux Total = "+user.text+"\n")
                    f1.close()

#Recherche dans le fichier XML du parking actuel les places libre.
                for user in tree.xpath("Free"):
                    Place_Libres = user.text
                    print('Nombre de places libres :',user.text)

#Ajout des données dans la liste DATA2 temporaire.
                    DATA2.append(user.text)

#Enregistrement des place libre dans un ficher exploitable.
                    f1=open("PlacesLibre.txt","a", encoding='utf8')
                    f1.write(user.text+'\n')
                    f1.close()

#Enregistrement des places libres dans le .txt utilisateur.
                    f1 = open("DonnéesUtilisateur.txt", "a")
                    f1.write(f"Place de libre = "+user.text+"\n")
                    f1.close()
#Listage de toutes les liste avec les données utiles des parkings.
                DATA.append(DATA2)

#Calcul pourcentage de place libre.
                Place_Libres = int(Place_Libres)
                Place_Total = int(Place_Total)
                Pourcentage = str(round((Place_Libres * 100)/Place_Total))
                print("Pourcentage de place libre : "+Pourcentage+" %")

#Enregistrement du pourcentage de place libre dans le .txt utilisateur.
                f1 = open("DonnéesUtilisateur.txt", "a")
                f1.write(f"Pourcentages de libre = "+Pourcentage+" %"+"\n \n")
                f1.close()

#Enregistrement du pourcentage de place libre dans un ficher exploitable.
                f1 = open("DonnéesPourcentages.txt", "a")
                f1.write(f""+Pourcentage+"\n")
                f1.close()
#Si le fichiers XML reçus à un code de status autre que 200 refait une demande, avec une attente de 2 secondes.
            else:
                print('Redemande')
                time.sleep(2)

#Enregistrement des données utiles.
        f1 = open("DATA.txt", "a")
        f1.write(str(DATA))
        f1.close()

 #Affiche la liste de liste des données utiles des parkings.En suite on attend 5 minutes le temps d'avoir la mise à jour du site.
        print(DATA)
        print("Attend 10 secondes")
        time.sleep(10)