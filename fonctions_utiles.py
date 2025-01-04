#pyfort-Lefevre-RoyNoughier-C
#JeanChipo & WarrenOne
#Ce fichier présente l'implémentation des fonctions utiles qui gèrent les joueurs, les épreuves, et l'enregistrement des résultats du jeu

def bold(text:str)->str:
    return "\033[1m" + text + "\033[0m"

def introduction()->None:
    """Affiche le script d'introduction de fort boyard."""
    print(
        bold("🎙️ Denis brognard :") +'\n'
        "Salut tout le monde, et bienvenue dans l’incroyable aventure de Fort Boyard ! \n"
        "Aujourd’hui, nos candidats vont devoir se dépasser pour relever des défis et, surtout, \n"
        "décrocher leur ticket pour la fameuse Salle du Trésor. \n"
        "Rien ne sera facile, mais avec un peu de courage et de stratégie, tout est possible. \n"
        '\n' +
        bold("💡 Les règles, c’est simple :") +'\n'
        "Votre équipe doit gagner 3 clés pour ouvrir les portes de la Salle du Trésor. \n"
        "Pour ça, vous allez affronter différentes épreuves – certaines demanderont de la force, \n"
        "d’autres de la réflexion, et parfois... un brin de folie. À chaque défi, un joueur est choisi pour y aller. \n" 
        "Et si vous réussissez, hop, une clé pour l’équipe ! \n",
        '\n' +
        bold("🔑 Trois clés, et après ?") +'\n'
        "Une fois les trois clés en poche, les portes de la Salle du Trésor s’ouvrent. \n"
        "Mais attention, ce n’est que le début : la vraie chasse au trésor ne commencera qu’une fois à l’intérieur. \n" 
        "Alors, chaque clé compte, et chaque épreuve est un pas de plus vers la victoire. \n",
        '\n' +
        bold("🎉 Allez, c’est parti !") +'\n'
        "Prenez une grande inspiration, serrez les coudes, et donnez tout. \n" 
        "Le Fort est rempli de surprises – certaines sympas, d’autres... un peu moins. \n" 
        "Mais une chose est sûre : vous allez vivre une aventure que vous n’oublierez pas de sitôt ! \n"
        "Prêts ? Alors, que l’aventure commence ! \n"
        )

def composer_equipe()->list[dict]:
    """
    Permet de composer une équipe de 1 à 3 joueurs.
    :return: une liste de dictionnaire contenant le nom, la profession, si le joueur est le leader de l'équipe, et le nombre de clé qu'il a gagné
    """
    liste_joueurs = []
    n = input("Combien de joueurs se joindront à l'aventure ? (PS: le bateau ne peut accueillir que 3 joueurs max) : ")
    while not '1' <= n <= '3':  # On ne convertit pas encore n en entier, car si l'utilisateur fait un retour à la ligne il y a une erreur
        n = input("Le bateau doit transporter entre 1 et 3 joueurs. \n"
                  "Merci de saisir un nombre de joueur valide : ")

    leader_present = False
    for i in range(int(n)):
        print(f"Joueur n°{i+1}, nous avons besoin de quelques informations sur vous.")
        nom = input("Quel est votre nom ? \n> ")
        while len(nom) == 0:
            nom = input("Vous n'avez pas de nom ? \n> ")

        profession = input("Quel est votre profession ? \n> ")
        while len(profession) == 0:
            profession = input("Vous faites forcement quelque chose dans la vie ! \n> ")

        if not leader_present :
            leader = input("Etes-vous le leader de l'équipe (V/F) ? \n> ")
            while leader != "V" and leader != "F":
                leader = input("Merci de saisir 'V' ou 'F' : ")
            match leader:
                case "V":
                    liste_joueurs.append({"nom":nom, "profession":profession, "est_leader":True, "cles_gagnees":0})
                    leader_present = True
                case "F":
                    liste_joueurs.append({"nom":nom, "profession":profession, "est_leader":False, "cles_gagnees":0})
                    leader_present = False
        else:   # si il y a déjà un leader, on ne redemande pas
            liste_joueurs.append({"nom": nom, "profession": profession, "est_leader": False, "cles_gagnees": 0})

    if not leader_present:
        print(liste_joueurs[0]["nom"] + ", vous êtes le leader de l'équipe puisque personne ne s'est porté volontaire.")
        liste_joueurs[0]["est_leader"] = True

    return liste_joueurs

def menu_epreuves():
    """
    affiche le menu des épreuves permettant à l'utilisateur de choisir parmi différents types d'épreuves disponibles
    :return: None si l'utilisateur choisi l'épreuve 1, 2 ou 3 / si il choisi l'énigme du père fouras, True si il répond correctement et False sinon
    """
    print(
        "1. Épreuve de Mathématiques \n"
        "2. Épreuve de Logique \n"
        "3. Épreuve du hasard \n"
        "4. Énigme du Père Fouras \n")
    choix = input("A quelle épreuve voulez-vous jouer ? : ")
    while not '1' <= choix <= '4':
        choix = input("Merci de choisir un entier entre 1 et 4 : ")
    print()
    return int(choix)

def choisir_joueur(equipe)->dict:
    """
    permet à l'utilisateur de sélectionner un joueur de l'équipe pour participer à une épreuve
    :param equipe: une liste de dictionnaire contenant les joueurs
    :return: un dictionnaire contenant le joueur choisi
    """
    for i in range(len(equipe)):
        if equipe[i]["est_leader"]:
            print(f"{i+1}. {equipe[i]['nom']} ({equipe[i]['profession']}) - Leader")
        else:
            print(f"{i+1}. {equipe[i]['nom']} ({equipe[i]['profession']}) - Membre")

    if len(equipe) == 1:
        print(f"L'équipe n'est composée que de {equipe[0]['nom']}, il doit donc participer à l'épreuve.")
        return equipe[0]

    n = input("Entrez le numéro du joueur: ")
    while not '1' <= n <= str(len(equipe)):
        n = input(f"Merci de saisir un entier entre 1 et {len(equipe)} : ")
    return equipe[int(n)-1]

################
## Historique ##
################

def enregistrer_historique(nom_epreuve:str, nom_joueur:str, resultat:bool)->None:
    """
    Fonction servant à enregistrer un historique
    :param nom_epreuve: Le nom de l'épreuve
    :param nom_joueur: Le nom du joueur
    :param resultat: Le resultat - True si le joueur gagne, False sinon
    :return: None
    """
    enregistrement = {"nom_epreuve":nom_epreuve, "nom_joueur":nom_joueur, "resultat":resultat}
    with open("./output/historique.txt", 'a', encoding="utf-8") as historique:
        historique.write(str(enregistrement) + '\n')

def sauter_ligne_historique()->None:
    """ Saute une ligne dans l'historique pour differencier les parties """
    with open("./output/historique.txt", 'a', encoding="utf-8") as historique:
        historique.write('\n')

sauter_ligne_historique()