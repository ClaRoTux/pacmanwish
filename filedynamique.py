class FileDynamique:
    def __init__(self):
        """ Instancie une file vide """
        self.file = []
        
    def enfiler(self, element):
        """ Enfile un élément en queue de file """
        self.file.append(element)
    
    def defiler(self):
        """ Défile ( si la file n'est pas vide ! ) un élément en tête de file, et le renvoie """
        if self.estVide == True:
            return ' la file est vide '
        element = self.file.pop(0)
        return element
    
    def estVide(self):
        """ Renvoie True si la file est vide, False sinon """
        if self.file == []:
            return True
        return False
    
    def affiche(self):
        return(self.file)
