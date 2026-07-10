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

def print_matches():
    for indice, valeur in enumerate(list_matches):
        print(f"tab[{indice}] = {valeur}")

if __name__ == '__main__':
    list_matches = get_list_matches()

    print_matches()
