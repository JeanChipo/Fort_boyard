from fonctions_utiles import *
from epreuve_finale import salle_de_tresor

def jeu():
    introduction() # affichage des instruction
    liste_joueurs = composer_equipe() # composition des équipes
    cle_gagner = 0
    while cle_gagner < 3:
        epreuve = menu_epreuves
        choisir_joueur(liste_joueurs)
        print("")
        if epreuve() == True:
            cle_gagner += 1
            print(f"vous venez d'obtenir une clée, vous en pocéder donc {cle_gagner}.\n")
        else:
            print(f"Vous n'avez pas gagner l'épreuve, vous en pocéder donc {cle_gagner}.\n")
    if salle_de_tresor() == True:
        print("\nFélisitation, vous avez gagner le jeu du Fort Boyrad de python")
    else:
        print("\nQuel dommage, vous avez perdue le jeu du Fort Boyrad de python")

jeu()