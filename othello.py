#!/usr/bin/python3

# construction des classes et définitions des méthodes et fonctions nécessaires

import copy

def direction(position, direction):
    '''Retrouver une position adjascente à partir d'une position de départ
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
    
def couleur_adverse(couleur):
    if couleur == 'N':
        return 'B'
    elif couleur == 'B':
        return 'N'


class Plateau(dict):

    #NB_TOT = 4

    def __init__(self):
        self[(3,4)] = Pion((3,4),'B')
        self[(4,3)] = Pion((4,3),'B')
        self[(3,3)] = Pion((3,3),'N')
        self[(4,4)] = Pion((4,4),'N')
        #self.NB_TOT += 1
        
    #def get_pion(self, position):
        #'''Retourne la couleur du pion situé sur une certaine case, si case vide retourne None'''
        #if position in self:
            #return self[position].get_couleur()
        #return None

    def evaluation(self):
        '''Fonction d'évaluation qui sert à calculer le poids d'une feuille dans l'algo min_max
        dans l'exemple, le mec basait son évaluation seulement sur le nombre de pions dudit joueur sur le plateau
        (si le joueur a 3 pions de plus que son adversaire sur le plateau, le poids du coup est de 3)'''
        pass
        
    def nombre_pions(self):
        '''Calcule le nombre de pions de chaque couleur sur le plateau'''
        N = 0
        B = 0
        for pion in self.values():
            if pion.couleur == 'N':
                N += 1
            else:
                B += 1
        return (N,B)
    
    def coup_valide(self, position, couleur):
        '''Pour une case donnée et la couleur du joueur en train de jouer, dit si le joueur peut placer un pion sur la case
        en retournant la liste des pions adverses qui seront retournés (si la liste est vide, la case ne peut pas être jouée par ce joueur)'''
        
        a_retourner = []

        # regarder si la case est bien dans le plateau
        #if not (0 <= case[0] <= 8) or not (0 <= case[1] <= 8):
        #    return (False, a_retourner)

        # regarder si la case est occupée
        if position in self:
            return a_retourner
        
        # SINON on part dans les 8 directions -> on doit avoir dans la ligne/colonne/diago : un ou plusieurs pion adverses > un pion du joueur
        #  -> dans ce cas tous ces pions adverses seront à retourner (ajouter les pions de a_ret à a_retourner)
        for i in range(8):
            a_ret = []
            pos = direction(position, i)

            # regarder si la case voisine est vide (NON), de la couleur du jour (NON)...
            if pos not in self or self[pos].couleur == couleur:
                continue
            
            # ...de la couleur adverse (OUI)
            elif self[pos].couleur != couleur:
                a_ret.append(pos)
                pos = direction(pos,i)

                # on continue dans la même direction...
                while pos in self and self[pos].couleur != couleur:
                    a_ret.append(pos)
                    pos = direction(pos,i)

                # ... jusqu'à tomber sur une case de la même couleur (OUI) -> dans ce cas on ajoute les cases à retourner à a_retourner
                if pos in self and self[pos].couleur == couleur:
                    for _ in a_ret:
                        a_retourner.append(_)

                # ... ou une case vide (ou existe pas) (NON)
                elif pos not in self:
                    continue

        return a_retourner
            
    def coups_possibles(self, couleur):
        '''Pour un joueur (sa couleur), regarde toutes les cases vides du plateau
        et fait la liste de toutes les positions qui peuvent être jouées par ce joueur
        en associant à chaque une liste des pions à retourner pour chaque (coup_valide).
        Si la liste est vide alors le joueur doit passer son tour'''
        cases_possibles = {}
        for i in range(8):
            for j in range(8):
                case = self.coup_valide((i,j), couleur)
                if (i,j) not in self and case:
                    cases_possibles[(i,j)] = case
        return cases_possibles
    
    def retourner_liste(self, liste):
        '''Retourne sur le plateau tous les pions d'une liste de leur position'''
        for pion in liste:
            self[pion].retourner()
        
    def simule_coup(self, position, liste_a_retourner, couleur):
        '''Simule l'état du plateau pour 1 coup sur 1 case
        (sur une copie du plateau, pose le pion et retourne tous les pions qu'il faut)'''
        # copier l'état du plateau
        copie_plateau = copy.deepcopy(self)
        # poser le pion sur le plateau
        copie_plateau[position] = Pion(position, couleur)
        # retourner tous les pions à retourner
        copie_plateau.retourner_liste(liste_a_retourner)
        return copie_plateau


class Pion(object):
    
    def __init__(self, position, couleur):
        self.position = position
        self.couleur = couleur

    #def set_couleur(self):
        #return self.couleur
    
    def retourner(self):
        '''Retourne un seul pion (change sa couleur)'''
        if self.couleur == 'N':
            self.couleur = 'B'
        elif self.couleur == 'B':
            self.couleur = 'N'


class Coup(object):

    def __init__(self, position, couleur, joueur, plateau, pere):
        self.position = position # du pion placé
        self.couleur = couleur # couleur du joueur qui joue ce coup
        self.joueur = joueur # True si IA, False si joueur, puisque qu'on ne cherche qu'à maximiser l'IA        
        self.plateau = plateau # après avoir joué le coup
        self.pere = pere # coup précédent (noeud père dans l'arbre)
        self.fils = [] # références à tous les fils du noeud
        self.poids = 0 # poids du coup
        self.poids_fils = [] # liste avec les poids de tous les fils
    
    def calc_poids(self):
        '''calcul du poids du coup
        quand on tombe sur une feuille, càd un coup dont la liste des fils est vide,
        on calcule son poids et on le met en guise de poids du père.
        après ça, on regarde le poids des autres fils du père et :
        - si le père est true, on prend le plus grand des poids (avec une boucle if > : on remplace le poids)
        - si le père est false, on prend le plus petit des poids
        '''
        pass

    def simulation(self, coup, plateau, couleur):
        '''à partir d'un plateau donné, regarde tous les coups possibles par le prochain joueur (couleur).
        pour chaque coup possible, crée un objet Coup en lui associant l'état du plateau après le coup.
        pour chaque objet Coup, en se basant sur le plateau, faire de même.
        et ça 2 fois (au début on pourra appeler cette fonction 2 fois)'''
        
        copie_plateau = copy.deepcopy(plateau)
        possible = copie_plateau.coups_possibles(couleur)
        fils = []

        if possible[0] :
            copie_plateau = copie_plateau.simule_coup(coup.position, possible[1], coup.couleur, copie_plateau)
            new = Coup(coup.position, coup.joueur, coup.couleur, copie_plateau, coup)
            fils.append(new)

        f = []
        for c in fils:
            pos = c.plateau.coup_valide(c.position, c.couleur)
            if pos:
                c.plateau.set_plateau(self.simule_coup(c.position, pos, c.couleur, c.plateau))
                n = Coup(c.position, c.joueur, c.couleur, c.plateau, c)
                f.append(n)
        
        return f

        
    def minimize(self):
        pass

    def maximize(self):
        pass
    
    def alpha_beta(self):
        pass
    
