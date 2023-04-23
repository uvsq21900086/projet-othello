#!/usr/bin/python3

def direction(position, direction):
    '''retrouver une position adjascente à partir d'une position de départ
    0 1 2
    7 P 3
    6 5 4'''
    if direction == 0: 
        return (position[0]-1, position[1]+1)
    if direction == 1: 
        return (position[0], position[1]+1)
    if direction == 2: 
        return (position[0]+1, position[1]+1)
    if direction == 3: 
        return (position[0]+1, position[1])
    if direction == 4: 
        return (position[0]+1, position[1]-1)
    if direction == 5: 
        return (position[0], position[1]-1)
    if direction == 6: 
        return (position[0]-1, position[1]-1)
    if direction == 7: 
        return (position[0]-1, position[1])

def fonction2():
    '''convertir les positions (a1) de plateau en coordonnées (0,0)
    UTILE ???'''
    pass


class Plateau(dict):

    NB_TOT = 4

    def __init__(self):
        self[(3,4)] = Pion('B')
        self[(4,3)] = Pion('B')
        self[(3,3)] = Pion('N')
        self[(4,4)] = Pion('N')
        self.NB_TOT += 1
        
    def get_pion(self, position):
        '''Retourne la couleur du pion situé sur une certaine case, si case vide retourne None'''
        if position in self:
            return self[position].get_col()
        return None
        
    def nombre_pions(self):
        '''Calcule le nombre de pions de chaque couleur sur le plateau'''
        N = 0
        B = 0
        for pion in self.values():
            if pion.couleur == 'B':
                B += 1
            else:
                N += 1
        return (N,B)
    
    def coup_possible(self, case, col):
        '''pour une case donnée et la couleur du joueur en train de jouer, dit si le joueur peut placer un pion ici et quels pions adverses seront retournés
        appeler cette fonction sur toutes les cases vides du plateau ???'''
        
        a_retourner = []

        # regarder si la case est bien dans le plateau
        #if not (0 <= case[0] <= 8) or not (0 <= case[1] <= 8):
        #    return (False, a_retourner)

        # regarder si la case est occupée
        if case in self:
            return (False, a_retourner)
        
        # on part dans les 8 directions : on doit avoir dans la ligne/colonne/diago un ou plusieurs pion adverses > un pion du joueur, dans ce cas tous ces pions adverses seront à retourner
        #   il ne faut pas que la case voisine soit vide ou avec un pion de la couleur du joueur
        for i in range(8):
            a_ret = []
            pos = direction(case, i)

            # regarder si la case voisine est vide (NON), de la couleur du jour (NON), de la couleur adverse (OUI)
            if pos not in self or self[pos].couleur == col:
                continue

            elif self[pos].couleur != col:
                a_ret.append(pos)
                pos = direction(pos,i)

                # continue dans la même direction jusqu'à tomber sur une case vide (ou existe pas) ou même couleur
                while pos in self and self[pos].couleur != col:
                    a_ret.append(pos)
                    pos = direction(pos,i)

                if pos in self and self[pos].couleur == col:
                    for _ in a_ret:
                        a_retourner.append(_)

                else:
                    continue

        if a_retourner == []:
            return (False, [])
        else:
            return (True, a_retourner)
            
    def fonction3(self, col):
        '''pour un joueur, regarde toutes les cases vides du plateau et fait la liste de tous les coups qui peuvent être joués par ce joueur (coup_possible)
        si la liste est vide alors le joueur doit passer son tour'''
        cases_possibles = {}
        for i in range(8):
            for j in range(8):
                case = self.coup_possible((i,j), col)
                if (i,j) not in self and case[0] == True:
                    cases_possibles[(i,j)] = case[1]
        return cases_possibles

    def retourner_all(self, liste):
        '''retourne tous les pions de la liste'''
        for pion in liste:
            self[pion].retourner()


class Pion(object):
    
    def __init__(self, col):
        self.couleur = col
        
    def get_col(self):
        return self.couleur
    
    def retourner(self):
        if self.couleur == 'N':
            self.couleur = 'B'
        else:
            self.couleur = 'N'
 
 
class Graphe(object):

    def __init__(self):
        pass
    
    def simule_coup(self):
        '''simule l'état du plateau pour 1 coup sur 1 case'''
    pass
        
    def min_max(self):
        pass
    
    def alpha_beta(self):
        pass
    
 
class Coup(object):

    def __init__(self):
        pass
