from tkinter import *
import graphe as gr
import algo_graphe as ag
from random import randint
'''
DEFINITIONS DES CLASSES
'''
class Labyrinthe:
    def __init__(self,laby):
        self.laby = laby
    
    def cree_graphe_laby(self):
        g = gr.GrapheD()
        for i in range(len(self.laby)):
            for j in range(len(self.laby[0])):
                if self.laby[i][j] != 1:
                    g.ajouteSommet((i,j))
                    if j != 0 and (self.laby[i][j-1] != 1):
                        g.ajouteArret((i,j),(i,j-1))
                    if i != 0 and (self.laby[i-1][j] != 1):
                        g.ajouteArret((i,j),(i-1,j))
        return g
    
    def affiche_laby(self):
        for y in range(len(self.laby)):
            for x in range(len(self.laby[0])):
                if self.laby[y][x]==1:
                    can.create_rectangle(x*26,y*26,(x+1)*26,(y+1)*26,fill='blue')
                elif self.laby[y][x]==2:
                    can.create_oval(x*26+7,y*26+7,(x+1)*26-7,(y+1)*26-7,fill='yellow')
                elif self.laby[y][x] == 3:
                    can.create_oval(x*26+4,y*26+4,(x+1)*26-4,(y+1)*26-4,fill='yellow')
    
class Pac_man(Labyrinthe):
    def __init__(self, x, y, graphe):
        self.x = x
        self.y = y
        self.graphe = graphe
        self.score=0
    '''
    GESTIONNAIRE D'Ã‰VENEMENT 'APPUI SUR UNE TOUCHE'
    '''
    def move(self, event):
        k = event.keysym # la variable 'k' contiendra la touche enfoncÃ©e
        if k == "z" :
            if (self.x-1,self.y) in self.graphe.adjacentsDe((self.x,self.y)):
                can.delete(self.forme)
                self.x -= 1
                self.draw()
        if k == "s" :
            if (self.x+1,self.y) in self.graphe.adjacentsDe((self.x,self.y)) :
                can.delete(self.forme)
                self.x += 1
                self.draw()
        if k == "q" :
            if (self.x,self.y-1) in self.graphe.adjacentsDe((self.x,self.y)) :
                can.delete(self.forme)
                self.y -= 1
                self.draw()
        if k == "d" :
            if (self.x,self.y+1) in self.graphe.adjacentsDe((self.x,self.y)) :
                can.delete(self.forme)
                self.y += 1
                self.draw()
    
    def getPosition(self):
        return self.x, self.y
        
    def draw(self):
        self.forme = can.create_oval(self.y*26, self.x*26, (self.y+1)*26, (self.x+1)*26,fill='yellow')
                        
class Ghost:
    '''
    GESTIONNAIRE D'ÉVENEMENT 'APPUI SUR UNE TOUCHE'
    '''
    def __init__(self,x,y, color , graphe):
        self.x = x
        self.y = y
        self.color = color
        self.graphe = graphe

    def affiche(self):
        self.fantom = can.create_rectangle(self.y*26,self.x*26,(self.y+1)*26,(self.x+1)*26,fill=self.color)

class Clyde(Ghost):
    def move(self):
        adj = self.graphe.adjacentsDe((self.x,self.y))
        i = randint(0,len(adj)-1)
        can.delete(self.fantom)
        self.x = adj[i][0]
        self.y = adj[i][1]
        self.affiche()
    
class Blinky(Ghost):
    def move(self):
        adj = self.graphe.adjacentsDe((self.x,self.y))
        dis = ag.distances(self.graphe.getGraphe(), P.getPosition())
        mini =0
        for i in range(0,len(adj)):
            if dis[adj[i]]<dis[adj[mini]]:
                mini =i
        can.delete(self.fantom)
        self.x = adj[mini][0]
        self.y = adj[mini][1]
        self.affiche()
            
class Pinky(Ghost):
    def move(self):
        adj = self.graphe.adjacentsDe((self.x,self.y))
        dis = ag.distances(self.graphe.getGraphe(), P.getPosition())
        mini =0
        for i in range(0,len(adj)):
            if dis[adj[i]]<dis[adj[mini]]:
                mini =i
        can.delete(self.fantom)
        self.x = adj[mini][0]
        self.y = adj[mini][1]
        self.affiche()
    
class Inky(Ghost):
    def move(self):
        adj = self.graphe.adjacentsDe((self.x,self.y))
        dis = ag.distances(self.graphe.getGraphe(), P.getPosition())
        mini =0
        for i in range(0,len(adj)):
            if dis[adj[i]]<dis[adj[mini]]:
                mini =i
        can.delete(self.fantom)
        self.x = adj[mini][0]
        self.y = adj[mini][1]
        self.affiche()

'''
BOUCLE D'ANIMATION
'''
    
def anim():
    Clyde.move()
    Blinky.move()
    Pinky.move()
    Inky.move()
    fen.after(20000, anim)
    
    
'''
CODAGE DU LABYRINTHE
'''
    
laby = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
[1,3,1,0,0,1,2,1,0,0,0,1,2,1,1,2,1,0,0,0,1,2,1,0,0,1,3,1],
[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
[1,2,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,2,1],
[1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
[1,1,1,1,1,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,1,1,1,1,1],
[1,0,0,0,0,1,2,1,1,1,1,1,0,1,1,0,1,1,1,1,1,2,1,0,0,0,0,1],
[1,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,1],
[1,0,0,0,0,1,2,1,1,0,1,1,0,0,0,0,1,1,0,1,1,2,1,0,0,0,0,1],
[1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
[0,0,0,0,0,0,2,0,0,0,1,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0],
[1,1,1,1,1,1,2,1,1,0,1,0,0,0,0,0,0,1,0,1,1,2,1,1,1,1,1,1],
[1,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,1],
[1,0,0,0,0,1,2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,2,1,0,0,0,0,1],
[1,0,0,0,0,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,0,0,0,0,1],
[1,1,1,1,1,1,2,1,1,0,1,1,1,1,1,1,1,1,0,1,1,2,1,1,1,1,1,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
[1,2,1,1,1,1,2,1,1,1,1,1,2,1,1,2,1,1,1,1,1,2,1,1,1,1,2,1],
[1,3,2,2,1,1,2,2,2,2,2,2,2,0,0,2,2,2,2,2,2,2,1,1,2,2,3,1],
[1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
[1,1,1,2,1,1,2,1,1,2,1,1,1,1,1,1,1,1,2,1,1,2,1,1,2,1,1,1],
[1,2,2,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,1,1,2,2,2,2,2,2,1],
[1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
[1,2,1,1,1,1,1,1,1,1,1,1,2,1,1,2,1,1,1,1,1,1,1,1,1,1,2,1],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
    
'''
INTERFACE
    
'''
        
fen = Tk() # fenÃªtre du jeu
fen.title('Pacman')
    
can = Canvas(fen, width = 1280, height = 800, background='black')
can.pack()
laby = Labyrinthe(laby)
laby.affiche_laby()
P = Pac_man(2,1 ,laby.cree_graphe_laby())
P.draw()
Clyde=Clyde(15,16,'orange',laby.cree_graphe_laby())
Blinky=Blinky(15,15,'red',laby.cree_graphe_laby())
Pinky=Pinky(15,14,'pink',laby.cree_graphe_laby())
Inky=Inky(15,13,'blue',laby.cree_graphe_laby())
Clyde.affiche()
Blinky.affiche()
Pinky.affiche()
Inky.affiche()
fen.bind('<Any-KeyPress>', P.move) # liaison des Ã©vÃ¨nements clavier Ã  la mÃ©thode de dÃ©placement ( nommÃ©e ici move ) de l'objet Pac-Man ( nommÃ© ici P )
    
    
anim() # premier lancement de l'animation
    
fen.mainloop()