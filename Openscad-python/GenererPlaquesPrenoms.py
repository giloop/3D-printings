#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Appel un script 
"""
# Call system command with unicode
import subprocess
# Write text files with unicode encodings
import codecs
import os
import sys

# Répertoire courant du fichier
repFic = os.path.dirname(os.path.realpath(__file__))

#%% Liste des prénoms à générer
# Liste des prénoms de plaques à générer
lPrenoms = ['Nathan', 'Margot', 'Erika', 'Naoma', 'Yaniss', 'Baptiste', 'Jules', 
            'Neil', 'Ines', u'Lanaïc', 'Lucas', 'Axel', 'Jeanne', 'Pauline', 
            'Emmie', 'Lylou', 'Briana', u'Kéziah','Lyna', 'Julien', 'Gabin', u'Mickaël', 'Lina'];

#%% Appel de openscad pour générer les STL unitaires
# Les commandes générées sont par exemple :
# openscad -o Mickaël.stl -D "prenom=\"Mickaël\"" PlaquePrenom.scad
for nom in lPrenoms:
	outStl = u"{}.stl".format(nom)
	print os.path.join(repFic, outStl)
	if (os.path.exists(os.path.join(repFic, outStl))):
		print u" -> fichier existant : non régénéré"
	else:
		print u" -> fichier non existant"
		strCommand = u"openscad -o {} -D \"prenom=\\\"{}\\\"\" PlaquePrenom.scad".format(outStl, nom)
		print u"{}".format(strCommand)
		subprocess.call(strCommand, shell=True)


#%% Création de fichiers openscad pour arranger les STL
l = 65
h = 20
# Les prénoms 
nbParFic = 12
nbParCol = 6

# Création de fichiers openscad pour arranger les STL
idxFic = 1
for idx,nom in enumerate(lPrenoms):
    print u'{} {}'.format(idx,nom)
    
    nomFic = u"Assemblage-{}.scad".format(idxFic)
    if not(os.path.exists(nomFic)):
        ficTxt = codecs.open(nomFic, "a", encoding='utf-8')
        ficTxt.write(u"union() {\n")
    elif (idx==0):
		print(u"Le fichier {} existe\n!! Effacez les fichiers scad générés avant de relancer le script".format(nomFic))
		sys.exit()
		
    idxCol = idx/nbParCol
    idxLig = idx%nbParCol
    ficTxt.write(u'\ttranslate([{},{},0]) import("{}.stl");\n'.format((l+5)*idxCol, (h+5)*idxLig, nom))

    if (idx>0 and (idx+1)%nbParFic==0):
        # Changement de fichier
        ficTxt.write(u"}")
        ficTxt.close()
        # Creation du STL avec Openscad
        strCommand = u"openscad -o Assemblage-{}.stl {}".format(idxFic, nomFic)
        print u"{}".format(strCommand)
        subprocess.call(strCommand, shell=True)
        # Fichier suivant
        idxFic = idxFic + 1


# Traitement du fichier en cours
if (not(ficTxt.closed)):
    # Changement de fichier
    ficTxt.write(u"}\n")
    ficTxt.close()
    # Creation du STL avec Openscad
    strCommand = u"openscad -o Assemblage-{}.stl {}".format(idxFic, nomFic)
    print "{}".format(strCommand)
    subprocess.call(strCommand, shell=True)

print "Fin"
       

