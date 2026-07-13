#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

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
    for _ in range(0, 21):
        list_matches.append(0)
    return list_matches


def get_nb_availables_matches(list_matches):
    """ Fonction qui renvoie le nombre d'allumettes disponibles"""
    return list_matches.count(0)


def is_available_match(num_match, list_matches):
    """ Fonction qui renvoie True si le numéro de l'allumette est disponible """
    if list_matches[num_match-1] != 0:
        return False
    return True


def print_matches(list_matches):
    """Fonction qui affiche la liste des allumettes passée en paramètre (liste des allumettes disponibles)"""
    print_matches_string = "Allumettes disponibles : \n - "
    for indice, valeur in enumerate(list_matches):
        if valeur == 0:
            print_matches_string += str(indice+1) + " - "
    print(print_matches_string)


def take_match(list_matches, num_player, num_match):
    """Fonction qui simule l'enlèvement d'une allumette par un joueur :
    on met à 1 la case si c'est le premier joueur qui l'a enlevée, 2 sinon"""
    list_matches[int(num_match)-1] = int(num_player)


def is_entry_player_ok(saisie):
    """Fonction qui vérifie si la saisie du prénom du joueur est correcte"""
    cleaned_saisie = saisie.strip()
    if " " in cleaned_saisie or not cleaned_saisie.isalpha():
        return False
    return True


def is_entry_matches_ok(saisie, list_matches):
    """Fonction qui vérifie si la saisie du joueur concernant les numéros des allumettes à enlever est correcte"""
    """Saisie attendue : entre 1 et 4 numéros d'allumettes, espacés par des espaces. 
       Chaque numéro d'allumette doit être entre 1 et 21, et doit faire partie des allumettes restant disponibles"""
    cleaned_saisie = saisie.strip()

    # Expression régulière pour la forme déjà de la saisie (aide chatgpt pour cette expression régulière)
    pattern = r"^(?:[1-9]|1\d|2[01])(?: (?:[1-9]|1\d|2[01])){0,3}$"
    if not re.fullmatch(pattern, cleaned_saisie):
        return False

    elements = cleaned_saisie.split()
    for element in elements:
        # On vérifie si le numéro de l'allumette est bien entre 1 et 21
        if not (1 <= int(element) <= 21):
            return False

        # On vérifie si cette allumette fait partie des allumettes disponibles
        if not is_available_match(int(element.strip()), list_matches):
            print(f"Vous avez entré un numéro d'allumette non disponible : {element.strip()}")
            return False
    return True


def is_entry_starts_ok(saisie):
    """ Fonction qui vérifie la saisie du joueur pour savoir qui joue en premier
        Valeur attendue : Numérique, 1 ou 2 obligatoirement
    """
    cleaned_saisie = saisie.strip()
    if not cleaned_saisie.isdigit():
        return False
    if int(cleaned_saisie) != 1 and int(cleaned_saisie) != 2:
        return False
    return True


def get_matches_input(list_matches):
    """Fonction qui demande au joueur de saisir les allumettes à enlever (entre 1 et 4 numéros d'allumettes,
    espacés par des espaces. Chaque numéro doit être entre 1 et 21, et doit faire partie des allumettes restantes"""
    input_matches = input("Saisir les allumettes à retirer (num de l'allumette, séparés par un espace) : ")
    while not is_entry_matches_ok(input_matches, list_matches):
        input_matches = input("Saisie incorrecte. Merci de recommencer : ")
    return input_matches


def get_players_input(num_player):
    """Fonction qui demande au joueur de saisir son nom"""
    input_player = input(f"Saisir le nom du joueur {num_player} : ")
    while not is_entry_player_ok(input_player):
        input_player = input("Saisie incorrecte. Merci de recommencer : ")
    return input_player


def get_who_starts_input(player1, player2):
    """Fonction qui demande au joueur quel joueur va commencer la partie"""
    starts_input = input(f"Qui commence ? ({player1} tapez 1, ou {player2} tapez 2) : ")
    while not is_entry_starts_ok(starts_input):
        starts_input = input("Saisie incorrecte. Merci de recommencer : ")
    # On enlève 1 pour s'adapter à notre tableau
    return int(starts_input)


if __name__ == '__main__':
    print("******************** Jeu de Nim ***********************")

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
        matches_plays = get_matches_input(list_matches)
        list_matches_played = matches_plays.split()
        # On récupère les allumettes jouées par le joueur et on les traite
        for match in list_matches_played:
            print(f"Le joueur {players[int(who_plays)-1]} a choisi l'allumette numéro {match}")
            take_match(list_matches, who_plays, match)
        if get_nb_availables_matches(list_matches) > 0:
            # On change de joueur
            who_plays = 2 if who_plays == 1 else 1
        # On affiche les allumettes
        print_matches(list_matches)

    print(f"{players[int(who_plays)-1]} a enlevé la dernière allumette et a perdu !")