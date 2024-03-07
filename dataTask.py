import json

def sauvegarder_dictionnaire_json(dictionnaire, TP.json):
   with open(TP.json,"w") as fichier_json:
	json.dump(dictionnaire,fichier json)

def changer_fichier_json(TP.json):
   with open(TP.json,"r") as fichier:
	return json.load(fichier)

def supprimer_base_de_donnees(TP.json):
   import os
   if os.path.exists(TP.json)
	print("base de donner est supprime")
