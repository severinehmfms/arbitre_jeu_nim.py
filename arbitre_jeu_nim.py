#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeu de Nim
Séverine Hori Maitrehut

La liste des allumettes est une liste simple
Pour chaque indice (attention indice 0 = allumette 1), la valeur est de 0 si l'allumette est disponible
la valeur est de 1 si l'allumette a été enlevée par le joueur 1
la valeur est de 2 si l'allumette a été enlevée par le joueur 2

La liste des joueurs est aussi un tableau simple avec comme valeur le nom du joueur
"""

def init_list_matches():
    """ Fonction qui initialise la liste des allumettes, toutes disponibles au début du jeu"""
    list_matches = []
    for i in range(0,21):
        list_matches.append(0)
    return list_matches

def get_nb_availables_matches(list_matches):
    """ Fonction qui renvoie le nombre d'allumettes disponibles"""
    return list_matches.count(0)

def print_matches(list_matches):
    """Fonction qui affiche la liste des allumettes passée en paramètre - dans notre cas la liste des allumettes disponibles"""
    print_matches_string = "Allumettes disponibles : \n - "
    for indice, valeur in enumerate(list_matches):
        if (valeur == 0):
            print_matches_string += str(indice+1) + " - "
    print(print_matches_string)

def take_match(list_matches, num_player, num_match):
    """Fonction qui simule l'enlèvement d'une allumette par un joueur : on met à 1 la case si c'est le premier joueur qui l'a enlevée, 2 sinon"""
    list_matches[int(num_match)-1] = int(num_player)

# TODO
def is_entry_player_ok(saisie):
    """Fonction qui teste si les prénoms des utilisateurs sont corrects"""
    cleaned_saisie = saisie.strip()
    if not cleaned_saisie.isalpha():
        return False
    return True

# TODO
def is_entry_matches_ok(saisie):
    """entre 1 et 4 numéros d'allumettes,
    espacés par des espaces. Chaque numéro d'allumette doit être entre 1 et 21, et doit faire partie des allumettes restantes"""
    return True

# TODO Numérique un ou deux obligatoirement.
def is_entry_starts_ok(saisie):

    return True

def get_matches_input(num_player):
    """Fonction qui demande à l'utilisateur de saisir les allumettes qu'il souhaite enlever (entre 1 et 4 numéros d'allumettes,
    espacés par des espaces. Chaque numéro d'allumette doit être entre 1 et 21, et doit faire partie des allumettes restantes"""
    input_matches = input("Saisir les allumettes à retirer (num de l'allumette, séparés par un espace) : ")
    while not is_entry_matches_ok(input_matches.strip()):
        input_matches = input("Saisie incorrecte. Merci de recommencer : ")
    return input_matches

def get_players_input(num_player):
    input_player = input(f"Saisir le nom de l'utilisateur {num_player} : ")
    while not is_entry_player_ok(input_player.strip()):
        input_player = input("Saisie incorrecte. Merci de recommencer : ")
    return input_player

def get_who_starts_input(player1, player2):
    starts_input = input(f"Qui commence ? ({player1} tapez 1, ou {player2} tapez 2 : ")
    while not is_entry_starts_ok(starts_input):
        starts_input = input("Saisie incorrecte. Merci de recommencer : ")
    #On enlève 1 pour s'adapter à notre tableau
    return int(starts_input)

if __name__ == '__main__':
    print("Jeu de Nim")

    list_matches = init_list_matches()
    print_matches(list_matches)
    players = []
    players.append(get_players_input(1))
    players.append(get_players_input(2))
    print(players)
    who_plays = get_who_starts_input(players[0], players[1])
    list_matches_played = []

    while get_nb_availables_matches(list_matches) > 0:
        print(f"Au tour de {players[int(who_plays)-1]} de jouer.")
        matches_plays = get_matches_input(who_plays)
        list_matches_played = matches_plays.split()
        # TODO On récupère les allumettes jouées par le joueur et on les traite
        for match in list_matches_played:
            print(f"Le joueur {players[int(who_plays)-1]} a choisi l'allumette numéro {match}")
            take_match(list_matches, who_plays, match)
        if get_nb_availables_matches(list_matches)!=0:
            #On change de joueur
            who_plays = 2 if who_plays == 1 else 1
        #On affiche les allumettes
        print_matches(list_matches)

    print(f"{players[int(who_plays)-1]} a enlevé la dernière allumette et a perdu !")