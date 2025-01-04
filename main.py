#pyfort-Lefevre-RoyNoughier-C
#JeanChipo & WarrenOne
#Ce fichier présente l'implémentation de la fonction principale regroupant tout les modules

from fonctions_utiles import *
from epreuve_finale import salle_de_tresor

from epreuves_mathematiques import epreuve_math
from epreuves_logiques import epreuve_logique
from epreuves_hasard import epreuve_hasard
from enigme_pere_fouras import enigme_pere_fouras

################

def jeu():
    """ Fonction principale d'execution du jeu de fort boyard """
    introduction() # affichage des instruction
    liste_joueurs = composer_equipe() # composition des équipes
    cle_gagnee = 0
    while cle_gagnee < 3:
        epreuve = menu_epreuves()
        joueur = choisir_joueur(liste_joueurs)
        print()
        match epreuve:
            case 1:
                reussite = epreuve_math()
                nom_epreuve = "epreuve_math"
            case 2:
                reussite = epreuve_logique()
                nom_epreuve = "epreuve_logique"
            case 3:
                reussite = epreuve_hasard()
                nom_epreuve = "epreuve_hasard"
            case 4:
                reussite = enigme_pere_fouras()
                nom_epreuve = "enigme_pere_fouras"
            case _:
                print("Error: epreuve non atteignable")
                reussite = False
                nom_epreuve = "error"
        if reussite == True:
            cle_gagnee += 1
            print(f"vous venez d'obtenir une clé, vous en posséder donc {cle_gagnee}.\n")
        else:
            print(f"Vous n'avez pas gagné l'épreuve, vous en posséder donc {cle_gagnee}.\n")
        enregistrer_historique(nom_epreuve, joueur["nom"], reussite)
    print("Vous possédez 3 clés, la salle au trésor s'ouvre.")
    nom_equipe = ""
    for i in range(len(liste_joueurs)-1):
        nom_equipe += liste_joueurs[i]["nom"] + ', '
    nom_equipe += liste_joueurs[-1]["nom"]

    if salle_de_tresor() == True:
        print("\nFélicitation, vous avez gagné le jeu du Fort Boyard edition python !")
        enregistrer_historique("salle_de_trésor", f"équipe de {nom_equipe}", True)
    else:
        print("\nQuel dommage, vous avez perdu le jeu du Fort Boyard edition python... \nLa prochaine sera la bonne !")
        enregistrer_historique("salle_de_trésor", f"équipe de {nom_equipe}", False)
    sauter_ligne_historique()

jeu()