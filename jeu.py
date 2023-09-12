#!/usr/bin/python3

# toutes les fonctions/instructions qui permettent le déroulement du jeu

import othello as oth

def attribution_col():
    '''tire à pile ou face quel joueur aura quelle couleur (le noir commence toujours)
    renvoie au hasard True ou False : si c'est True, l'IA commence, sinon le joueur commence'''
    return True

# 1 on décide qui commence (who = True ou False)
who = attribution_col()

# 2 on met en place le plateau
plateau = oth.Plateau()

# 3 on définit quels coups sont faisables par le joueur noir
coups_de_depart = {(2,4):[(3,4)] , (3,5):[(3,4)] , (4,2):[(4,3)] , (5,3):[(4,3)]} # pion posé : pion retourné
liste_coups_depart = []

# 4 pour chaque coup du dictionnaire, on fait la simulation du plateau et on crée un objet Coup (qu'on append à la liste)
for coup in coups_de_depart.items():
    copie_plateau = plateau.simule_coup(coup[0], coup[1], 'N')
    liste_coups_depart.append(oth.Coup(coup[0], 'N', who, copie_plateau, None))

# pour chaque Coup de liste_coups_depart, on regarde les coups jouables par l'adversaire
for coup in liste_coups_depart:



#coup_actuel = référence au coup actuel, càd là où on en est dans la partie



if __name__ == '__main__':
    pass

