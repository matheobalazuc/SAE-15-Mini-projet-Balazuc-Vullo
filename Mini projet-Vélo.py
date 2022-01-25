import requests 
from lxml import etree
from time import sleep

def makerequest():
	response=response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
	f1=open("velo.txt","w", encoding='utf8')
	f1.write(response.text)
	f1.close()
	
def parse():
	tree = etree.parse("velo.txt")
	for user in tree.xpath("/vcs/sl/si"):
		print('Nom de la station: ' ,(user.get('na')))
		print('Nombre de vélos libres : ' ,int(user.get('fr')))

for i in range(3):
	makerequest()
	parse()
	time.sleep(10)
