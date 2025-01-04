#pyfort-Lefevre-RoyNoughier-C
#JeanChipo & WarrenOne
#Ce fichier présente l'implémentation de l'epreuve finale

import json
from random import choice

def salle_de_tresor() -> bool: # épreuve de la salle du trésor
    """
    :return: True si le joueur gagne, False sinon
    """
    with open("./data/indicesSalle.json", 'r', encoding='utf-8') as file:  # récupère le dictionnaire qui est dans le fichier JSON
        dico_fichier = json.load(file)

    jeu_tv = dico_fichier["Fort Boyard"]
    annee = jeu_tv[choice(list(jeu_tv.keys()))]  # prend une année aléatoire
    emission = annee[choice(list(annee.keys()))]  # prend une émission aléatoire
    mot_code = emission["MOT-CODE"]  # stocke le mot à trouver
    indices = emission["Indices"]  # stocke les indices dans une liste
    win = False  # initialisation de la victoire

    # affichage des instructions et des indices
    print("Dans l'épreuve finale, vous devrez, avec 3 mots d'indice, trouver le mot à deviner.")
    print(f"Les trois indices sont :\n{indices[0]}\n{indices[1]}\n{indices[2]}")

    for i in range(3):  # boucle des trois tentatives
        reponse = input("Entrez le mot-code qui correspond aux indices : ")  # demande à l'utilisateur sa réponse

        if reponse.lower() == mot_code.lower():  # si le mot est le même que celui à trouver, on dit que le joueur a gagné et on arrête le jeu
            win = True
            print("Bien joué, vous avez trouvé le bon mot !")
            break
        elif i != 2:  # sinon, on affiche que le joueur n'a pas trouvé le bon mot et on lui dit combien de tentatives il lui reste
            print(f"Mauvaise réponse\nIl vous reste {2 - i} tentative(s).")
        else:  # et s'il ne lui reste plus de tentatives, on lui dit qu'il a perdu
            print("Mauvaise réponse\nVous avez perdu.")

    return win