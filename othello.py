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


class Plateau(dict):

    def __init__(self):
        self[(3,4)] = Pion('B')
        self[(4,3)] = Pion('B')
        self[(3,3)] = Pion('N')
        self[(4,4)] = Pion('N')
    
    def get_pion(self, position):
        '''Retourne la couleur du pion situé sur une certaine case, si case vide retourne None'''
        if position in self:
            return self[position].get_col()
        return None
        
    def nombre_pions(self):
        '''calcule le nombre de pions de chaque joueur sur le plateau'''
    
    def coup_valide(self):
        '''pour une case donnée et la couleur du joueur en train de jouer, dit si le joueur peut placer un pion ici et quels pions adverses seront retournés
        appeler cette fonction sur toutes les cases vides du plateau ???'''
        # regarder si la case est bien dans le plateau
        # regarder si la case est prise
        # on part dans les 8 directions : on doit avoir dans la ligne/colonne/diago un ou plusieurs pion adverse - un pion du joueur, dans ce cas tous ces pions adverses seront à retourner
        #   il ne faut pas que la case voisine soit vide ou avec un pion de la couleur du joueur
    
    def fonction3(self):
        '''pour un joueur, regarde toutes les cases vides du plateau et fait la liste de tous les coups qui peuvent être joués par ce joueur (coup_valide)
        si la liste est vide alors le joueur doit passer son tour'''
        
    def retourner_all(self, liste):
        '''retourne tous les pions de la liste'''



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
    
    def simule_coup(self):
        '''simule l'état du plateau pour 1 coup sur 1 case'''
        
    def min_max(self):
    
    
    def alpha_beta(self):
    
    
 
class Coup(object):



