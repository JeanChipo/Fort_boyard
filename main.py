from fonctions_utiles import *

#####################

def jeu():
    introduction()
    equipe = composer_equipe()
    nb_cles = 0

    for i in range(len(equipe)):
        nb_cles += equipe[i]["cles_gagnees"]

    while nb_cles < 3:
        menu_epreuves()
        choisir_joueur(equipe)
