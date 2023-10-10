#####Importations#####

###Importation du module interface###
import interface

###Importations de modules de une seule fonction de fractale###
import sierpinski
import carré
import dragon

###Importation de module de plusieures fonctions de fractales###
import vonkoch



##### Programme exemple #####

###Initialisation du module graphique###
interface.init()

###Ajout de boutons###
#Pour des modules de une fonction
interface.add(sierpinski.sierpinski,"Sierpinski")
interface.add(carré.imbrique,"Imbriqué")
interface.add(dragon.dragoncurve,"Dragon")
#Pour des modules de plusieurs fonctions
interface.add(vonkoch.flocon,"Flocon de Vonkoch")
interface.add(vonkoch.vonKoch,"Vonkoch Simple")

###Affichage###
interface.start()
