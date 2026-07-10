#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeu de Nim
Séverine Hori Maitrehut
"""

def get_list_matches():
    list_matches = []
    for i in range(0,21):
        list_matches.append(0)
    return list_matches

def print_matches(list_matches):
    print_matches_string = "Allumettes disponibles : \n - "
    for indice, valeur in enumerate(list_matches):
        if (valeur == 0):
            print_matches_string += str(indice+1) + " - "
    print(print_matches_string)

def take_match(list_matches, num_player, num_match):
    list_matches[num_match-1] = num_player


if __name__ == '__main__':
    list_matches = get_list_matches()
    print_matches(list_matches)
