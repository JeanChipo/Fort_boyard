from fonctions_utiles import *
from epreuve_finale import salle_de_tresor

def jeu():
    introduction() # affichage des instruction
    liste_joueurs = composer_equipe() # composition des équipes
    cle_gagner = 0
    while cle_gagner < 3:
        epreuve = menu_epreuves()
        choisir_joueur(liste_joueurs)
        if epreuve() == True:
            cle_gagner += 1
    salle_de_tresor()

jeu()