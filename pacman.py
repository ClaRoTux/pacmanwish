# Paul Pierrick Faustin
from tkinter import *
import graphe as gr
import algo_graphe as ag
from random import randint
'''
DEFINITIONS DES CLASSES
'''
class Labyrinthe:
    def __init__(self,laby,sc=0):
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
    def __init__(self, x, y, graphe,score=0):
        self.x = x
        self.y = y
        self.graphe = graphe
        self.sc=score
    '''
    GESTIONNAIRE D'Ã‰VENEMENT 'APPUI SUR UNE TOUCHE'
    '''
    def move(self, event):
        k = event.keysym # la variable 'k' contiendra la touche enfoncÃ©e
        if k == "z" :
            if (self.x-1,self.y) in self.graphe.adjacentsDe((self.x,self.y)):
                can.delete(self.forme)
                P.score()
                P.supergomme()
                self.x -= 1
                self.draw()
        if k == "s" :
            if (self.x+1,self.y) in self.graphe.adjacentsDe((self.x,self.y)) :
                can.delete(self.forme)
                P.score()
                P.supergomme()
                self.x += 1
                self.draw()
        if k == "q" :
            if (self.x,self.y-1) in self.graphe.adjacentsDe((self.x,self.y)) :
                can.delete(self.forme)
                P.score()
                P.supergomme()
                self.y -= 1
                self.draw()
        if k == "d" :
            if (self.x,self.y+1) in self.graphe.adjacentsDe((self.x,self.y)) :
                can.delete(self.forme)
                P.score()
                P.supergomme()
                self.y += 1
                self.draw()
    
    def getPosition(self):
        return self.x, self.y
        
    def draw(self):
        self.forme = can.create_oval(self.y*26, self.x*26, (self.y+1)*26, (self.x+1)*26,fill='yellow')
    
    def score(self):
        if tab[self.x][self.y]==2:
            can.delete(self.affiche_score)
            can.create_rectangle(self.y*26, self.x*26, (self.y+1)*26, (self.x+1)*26,fill='black')
            self.affiche_score= can.create_text(364,300,text=self.sc,fill="white",font=("Times", "24"))
            self.sc+=1
            tab[self.x][self.y]=0
        return self.sc
    
    def affiche(self):
        self.affiche_score= can.create_text(364,300,text=self.sc,fill="white",font=("Times", "24"))
    
    def supergomme(self):
        if tab[self.x][self.y]==3:
            can.delete(self.affiche_score)
            can.create_rectangle(self.y*26, self.x*26, (self.y+1)*26, (self.x+1)*26,fill='black')
            self.affiche_score= can.create_text(364,300,text=self.sc,fill="white",font=("Times", "24"))
            self.sc+=5
            tab[self.x][self.y]=0
        return self.sc
    
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
    
    def touche(self):
        if (self.x,self.y) == P.getPosition():
            score=str(P.score())
            can.destroy()
            loose = Canvas(fen, width = 728, height = 806, background='black')
            loose.create_text(364,300,text="Game Over",fill="white",font=("Times", "24"))
            loose.create_text(364,350,text="Score : ",fill="white",font=("Times", "24"))
            loose.create_text(450,350,text=score,fill="white",font=("Times", "24"))
            loose.pack()

    
class Clyde(Ghost):
    def move(self):
        adj = self.graphe.adjacentsDe((self.x,self.y))
        i = randint(0,len(adj)-1)
        can.delete(self.fantom)
        self.x = adj[i][0]
        self.y = adj[i][1]
        self.affiche()
        self.touche()
    
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
        self.touche()
            
class Pinky(Ghost):
    def move(self):
        adj = self.graphe.adjacentsDe((self.x,self.y))
        adj2 = self.graphe.adjacentsDe(P.getPosition())
        aleatoire = randint(0,len(adj2)-1)
        adj3=self.graphe.adjacentsDe(adj2[aleatoire])
        dis = ag.distances(self.graphe.getGraphe(),(adj3[0]))
        mini =0
        for i in range(0,len(adj)):
            if dis[adj[i]]<dis[adj[mini]]:
                mini =i
        can.delete(self.fantom)
        self.x = adj[mini][0]
        self.y = adj[mini][1]
        self.affiche()
        self.touche()
    
class Inky(Ghost):
    def move(self):
        adj = self.graphe.adjacentsDe((self.x,self.y))
        adj2 = self.graphe.adjacentsDe(P.getPosition())
        aleatoire = randint(0,len(adj2)-1)
        adj3=self.graphe.adjacentsDe(adj2[aleatoire])
        dis = ag.distances(self.graphe.getGraphe(),(adj3[len(adj3)-1]))
        mini =0
        for i in range(0,len(adj)):
            if dis[adj[i]]<dis[adj[mini]]:
                mini =i
        can.delete(self.fantom)
        self.x = adj[mini][0]
        self.y = adj[mini][1]
        self.affiche()
        self.touche()

def victoire(tab):
    win = True
    for x in tab:
        for y in x:
            if y==2 or y==3:
                win = False
    if win == True:
        can.destroy()
        win=Canvas(fen, width = 728, height = 806, background='black')
        win.create_text(364,300,text="Victoire !",fill="white",font=("Times", "24"))
        win.pack()

'''
BOUCLE D'ANIMATION
'''
    
def anim():
    Clyde.move()
    Blinky.move()
    Pinky.move()
    Inky.move()
    victoire(tab)
    fen.after(200, anim)
    
    
'''
CODAGE DU LABYRINTHE
'''
    
tab = [
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
    
can = Canvas(fen, width = 728, height = 806, background='black')
can.pack()
laby = Labyrinthe(tab)
laby.affiche_laby()
P = Pac_man(2,1 ,laby.cree_graphe_laby())
P.draw()
P.affiche()
Clyde=Clyde(15,16,'orange',laby.cree_graphe_laby())
Blinky=Blinky(15,15,'red',laby.cree_graphe_laby())
Pinky=Pinky(15,14,'pink',laby.cree_graphe_laby())
Inky=Inky(15,13,'cyan',laby.cree_graphe_laby())
Clyde.affiche()
Blinky.affiche()
Pinky.affiche()
Inky.affiche()
fen.bind('<Any-KeyPress>', P.move) # liaison des Ã©vÃ¨nements clavier Ã  la mÃ©thode de dÃ©placement ( nommÃ©e ici move ) de l'objet Pac-Man ( nommÃ© ici P )

anim() # premier lancement de l'animation
    
fen.mainloop()
