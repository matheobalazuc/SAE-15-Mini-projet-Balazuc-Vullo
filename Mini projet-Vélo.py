import requests
from lxml import etree
response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
print(response.text)

velo=['TAM_MMM_VELOMAG']
for i in velo:
	response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/" +i+ ".xml")
	print(response.text)

response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/TAM_MMM_VELOMAG.xml")
print(response.text)
f1=open("TAM_MMM_VELOMAG.txt","w", encoding='utf8')
f1.write(response.text)
f1.close()
tree = etree.parse("TAM_MMM_VELOMAG.txt")
	for user in tree.xpath("na"):
		print('Nom de la station de vélo',user.text)
#for user in tree.xpath("av"):
	#print('Nombre total de places :',user.text)
	for user in tree.xpath("fr"):
		print('Nombre de places libres :',user.text)