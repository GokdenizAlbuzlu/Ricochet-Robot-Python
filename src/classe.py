from os import X_OK
import random
#Classe Robot
class Robot:
    x = 0
    y = 0
    objectif= ""

    def __init__(self, color):
        self.couleur = color
    #La fonction __eq__ permet de determiner si deux robots sont égaux ou non en se basant sur leur positions
    def __eq__(self,other):
        return self.x ==other.x and self.y == other.y

    
  
#Classe Case , lorsque que nord sud est ou ouest vaut True cela signifie qu'un mur est présent dans cette direction
class Case : 
    # Attribut généraux
    nord = False
    sud = False
    est = False
    ouest = False
    robot = Robot("O")
    objectif=""
    val = 3

#Classe Node utilisée pour l'algorithme A*
class Node : 
    def __init__(self,Case,parent,x,y):
        self.case = Case
        self.parent = parent
        self.x=x
        self.y=y
        self.h = 0
        self.g = 0
        self.f = 0
    

#Fonction permettant d'initialiser les robots avec leur couleur et leur positions
def init_robot():
    Robot_Vert = Robot("V")
    Robot_Bleu = Robot("B")
    Robot_Rouge = Robot("R")
    Robot_Jaune = Robot("J")
 
    Robot_Vert.x=13
    Robot_Vert.y=5

    Robot_Bleu.x=1
    Robot_Bleu.y=2


    Robot_Rouge.x=0
    Robot_Rouge.y=0

    Robot_Jaune.x=7
    Robot_Jaune.y=4

    return [Robot_Bleu,Robot_Rouge,Robot_Vert,Robot_Jaune]



