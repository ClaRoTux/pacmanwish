import graphe as gr
import filedynamique as f
import PileDynamique as p
from math import inf

def parcours_largeur(g, s):
    file = f.FileDynamique()
    marque ={i : False for i in g}
    parcours = []
    marque[s] = True
    file.enfiler(s)
    while file.estVide() != True:
        u = file.defiler()
        for v in g[u]:
            if marque[v] == False:
                marque[v] = True
                file.enfiler(v)
        parcours +=[u]
    return parcours

def parcours_profondeur(g,s):
    pile = p.PileDynamique()
    marque ={i : False for i in g}
    parcours = []
    marque[s] = True
    pile.empiler(s)
    while pile.est_vide() != True:
        u = pile.depiler()
        for v in g[u]:
            if marque[v] == False:
                marque[v] = True
                pile.empiler(v)
        parcours +=[u]
    return parcours

def parcours_recursif_profondeur(g, u, marque, parcours):
    marque[u] = True
    parcours+=[u]
    for v in g[u]:
        if marque[v] == False:
            parcours_recursif_profondeur(g,v,marque,parcours)
    return parcours

def contient_cycle(G):
    '''Fonction qui détermine si un graphe non-orienté contient un cycle.
    Entrée :
        G = objet de type GrapheD
    Sortie :
        booléen True si le graphe contient un cycle, False sinon
    '''
    sommet =[]
    for cle in G:
        sommet += cle
    s = sommet[0]
    pile = p.PileDynamique()
    marque ={i : False for i in g}
    parcours = []
    marque[s] = True
    pile.empiler(s)
    while pile.est_vide() != True:
        u = pile.depiler()
        for v in g[u]:
            if v in parcours:
                return True
            if marque[v] == False:
                marque[v] = True
                pile.empiler(v)
        parcours +=[u]
    return False


def chemin(s: str, pred: dict)->str:
    '''Fonction qui reconstruit le chemin depuis un sommet jusqu'à la racine du parcours,
    en utilisant le dictionnaire des prédécesseurs de chaque sommet dans le parcours.
    Entrées :
        s = l'étiquette du sommet considéré
        pred = le dictionnaire associant à chaque sommet l'étiquette de son prédécesseur dans le parcours
    Sortie :
        une chaîne de caractères représentant le chemin à suivre depuis la racine du parcours
    '''
    if pred[s] ==s:
        return str(s)
    else:
        return chemin(pred[s], pred) +' -> '+ str(s)


def existe_chemin(g, s1: str, s2: str)->str:
    '''Fonction qui détermine le chemin ( pas le plus court ) entre deux sommets si celui-ci existe.
    Entrées :
        G = objet de type GrapheD
        s1 = étiquette du premier sommet
        s2 = étiquette du deuxième sommet
    Sortie :
        le chemin si il existe
        une information indiquant que le chemin n'existe pas dans le cas contraire
    '''
    pile = p.PileDynamique()
    pred= {s1:s1}
    pile.empiler(s1)
    while pile.est_vide() != True:
        u = pile.depiler()
        if u == s2:
            return chemin(s2,pred)
        for v in g[u]:
            if v not in pred:
                pred[v] = u
                pile.empiler(v)
    return False


def plus_court_chemin(g, s1: str, s2:str)->str:
    '''Fonction qui détermine le plus court chemin entre deux sommets quelconques d'un graphe
    Entrée :
        G = objet de type GrapheD
        s1 et s2 = étiquettes des deux sommets
    Sortie :
        chaîne = chemin entre les deux sommets
    '''
    file = f.FileDynamique()
    pred = {s1:s1}
    file.enfiler(s1)
    while file.estVide() != True:
        u = file.defiler()
        if u == s2:
            return chemin(s2,pred)
        for v in g[u]:
            if v not in pred:
                pred[v] = u
                file.enfiler(v)
    return False


def distances(g, r: str)->dict:
    '''Fonction qui calcule les distances du sommet racine du parcours aux autres sommets du graphe
    Entrée :
        G = objet de type GrapheD
        r = étiquette du sommet racine
    Sortie :
        le dictionnaire donnant pour chaque sommet sa distance à la racine.
    '''
    d = {i : inf for i in g}
    file = f.FileDynamique()
    file.enfiler(r)
    d[r] = 0
    while file.estVide() != True:
        u = file.defiler()
        for v in g[u]:
            if d[v] == inf :
                file.enfiler(v)
                d[v]=d[u]+1
    return d

# print(chemin('C',pred))
g={'A': ['B'],'B': ['A'],'C': ['E'],'D': ['B', 'C'],'E': ['C', 'F'],'F': ['B', 'C']}
# print(contient_cycle(g))
# print(existe_chemin(g,'C','G'))
# print(plus_court_chemin(g,'A','G'))
# print(distances(g,'D'))