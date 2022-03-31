class GrapheD:
    def __init__(self, S = None):
        '''Méthode qui crée un graphe vide ou à partir d'une liste de sommets.
        Entrée :
            S = la liste des sommets du graphe ( None par défaut )
        '''
        if S == None:
            self.graphe = {}
        else:
            self.graphe = {S[i]: [] for i in range(len(S))}

    def getGraphe(self):
        '''Méthode qui renvoie la représentation Python du graphe ( accesseur ).
        '''
        return self.graphe
        

    def ajouteSommet(self, id:str):
        '''Méthode qui ajoute un sommet au graphe.
            Entrée :
                id = l'identifiant ( unique ! ) du sommet dans le graphe
            Lève une exception au cas où l'identifiant existe déjà dans le graphe (erreur-> assert)
        '''
        assert id not in self.graphe, "Le sommet est déjà dans le graphe."
        self.graphe[id] = []
    
    def ajouteArc(self, id1:str, id2:str):
        '''Méthode qui créé un arc entre deux sommets.
        Entrées :
            id1 = identifiant du sommet de départ de l'arc
            id2 = identifiant du sommet de fin de l'arc
        '''    
        assert id1 in self.graphe, "Le sommet de départ n'est pas dans le graphe."
        assert id2 in self.graphe, "Le sommet de fin n'est pas dans le graphe."
        self.graphe[id1] += [id2]
    
    def ajouteArret(self, id1:str, id2:str):
        '''Méthode qui créé une arrête entre deux sommets.
        Entrées :
            id1 = identifiant du sommet de départ de l'arc
            id2 = identifiant du sommet de fin de l'arc
        '''    
        assert id1 in self.graphe, "Le sommet de départ n'est pas dans le graphe."
        assert id2 in self.graphe, "Le sommet de fin n'est pas dans le graphe."
        self.graphe[id1] += [id2]
        self.graphe[id2] +=[id1]


    def suppSommet(self, id:str):
        '''Méthode qui supprime un sommet au graphe.
            Entrée :
                id = l'identifiant ( unique ! ) du sommet dans le graphe
        Lève une exception au cas où l'identifiant n'existe pas dans le graphe
        '''
        assert id in self.graphe, "Le sommet n'est pas dans le graphe."
        del self.graphe[id]
        for i in self.graphe:
            if id in self.graphe[i]:
                self.graphe[i].remove(id)


    def suppArc(self, id1:str, id2:str):
        '''Méthode qui supprime un arc entre deux sommets
        Entrées :
            id1 = identifiant du sommet de départ de l'arc
            id2 = identifiant du sommet de fin de l'arc
        Lève une exception au cas où l'arc n'existe pas dans le graphe
        '''
        assert id1 in self.graphe, "Le sommet de départ n'est pas dans le graphe."
        assert id2 in self.graphe, "Le sommet de fin n'est pas dans le graphe."
        assert id2 in self.graphe[id1], " L'arc n'existe pas dans le graphe."
        self.graphe[id1].remove(id2)

    
    def estVide(self):
        '''Méthode qui détermine si le graphe est vide.
        Sortie :
            booléen VRAI ou FAUX selon le résultat	
        '''
        return self.graphe == None
    
    
    def adjacentsDe(self, id:str):
        '''Méthode qui renvoie la liste des sommets adjacents (voisins ou successeurs ) d'un sommet donné.
        Entrée :
            id = l'identifiant du sommet
        Sortie :
            la liste des sommets adjacents du sommet passé en paramètre
        Lève une exception si le sommet n'existe pas dans le graphe.
        '''
        assert id in self.graphe, "Le sommet n'est pas dans le graphe."
        return self.graphe[id]