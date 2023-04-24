#!/usr/bin/python3

# toutes les fonctions/instructions qui permettent le déroulement du jeu

import othello as oth

def attribution_col():
    '''tire à pile ou face quel joueur aura quelle couleur (le noir commence toujours)'''
    pass

plateau = oth.Plateau()

coups_de_depart = {(2,4):(3,4) , (3,5):(3,4) , (4,2):(4,3) , (5,3):(4,3)}
for coup in coups_de_depart.items():
    oth.Arbre.simule_coup(coup[0], coup[1], 'N', plateau)

