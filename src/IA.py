from pygame.constants import TIMER_RESOLUTION
from affichage import * 
from classe import * 
from deplacements import *
from affichage import *
from operator import attrgetter, pos, xor
#A*


###Code pour l'algorithme A*###
###Il n'est pas implementer dans le programme princiapl###
###Il permet de trouver un chemin qui deplace uniquement un seul robot###
###Pour tester une cible modifier les coordonées de la winningNode####







#Creation de notre tableau
robot_ia = init_robot()
ia_board = create_board()
modify_board(ia_board,robot_ia)








































#Fonction penalite
def penalite(node,winningNode):
    #Par defaut notre penalite est à 1 cela veut dire que la case est du bon cote et n'a pas de mur empechant la progression vers l'objectif
    node.h = 1

    #Cas ou la case n'est pas du bon cote de l'ouverture de l'objectif
    if winningNode.x>node.x and winningNode.case.ouest==True :
        node.h = 5
    if winningNode.x<node.x and winningNode.case.est==True :
        node.h = 5
    if winningNode.y>node.y and winningNode.case.nord==True :
        node.h = 5
    if winningNode.y<node.y and winningNode.case.sud==True :
        node.h = 5



    #Cas ou la case a un mur empechant la progression vers l'objectif
    if winningNode.x>node.x and winningNode.case.est==node.case.est==True :
        node.h = 3
    if winningNode.x<node.x and winningNode.case.ouest==node.case.ouest==True :
        node.h = 3
    if winningNode.y>node.y and winningNode.case.sud==node.case.sud==True :
        node.h = 3
    if winningNode.y<node.y and winningNode.case.nord==node.case.nord==True :
        node.h = 3
    #Cas ou la case est l'objectif
    if winningNode.y==node.y and winningNode.x==node.x :
        node.h=-100
    #Cas ou la case est aligner avec une des positions de l'objectif
    elif winningNode.y==node.y or winningNode.x==node.x  :
        node.h=-5
 






    return node

#Fonction find_neighbour qui permet de determiner tout les voisins d'un node
def find_neighbour(currentNode,tab):

    return deplacement_ouest(tab,currentNode),deplacement_est(tab,currentNode),deplacement_nord(tab,currentNode),deplacement_sud(tab,currentNode)









#Robot de test


#Definition de la node gagnante
winningNode=Node(ia_board[4][2],None,2,4)

#Debut de l'algorithme A*

#Noeud qui doivent etre evaluer
open = []
#Noeud qui on été evaluer
closed =[]
#Ajout du noeud de départ

open.append(Node(ia_board[robot_ia[0].y][robot_ia[0].x],None,robot_ia[0].x,robot_ia[0].y))
test=[]






best_path_to_obst =[]

find = False
#Tant qu'aucun chemin n'est trouver
while not find:
    
    #Le noeud a analyser est par defaut le premier (utiliser lorsque la liste est composé d'un seul noeud)
    current_node = open[0]
    current_index = 0


    # Determination du meilleur Noeud possible
    for index, item in enumerate(open):
        if item.f < current_node.f:
            current_node = item
            current_index = index

    # Retrait dans Open et Ajout dans Closed
    open.pop(current_index)
    closed.append(current_node)

   
   #Un chemin a ete trouver
    if current_node.h ==-100:
        print("J'ai trouver un chemin :)")
        #Reconstitution du chemin
        
        path = []
        current = current_node
        while current is not None:
            path.append(current)
            current = current.parent
        

        find = True

    #Récupération des coordonées voisins de la node actuelle
    neighbours_co = find_neighbour(current_node,ia_board)
   
    #Liste des voisins
    neighbours =[]
    #Création des voisins et affectations a la liste neihgbours
    for position in neighbours_co: 
        
        if position !=None:
            
            new_Node=Node(ia_board[position[1]][position[0]],current_node,position[0],position[1])
            neighbours.append(new_Node)
        else : 
            continue

    #Analyse des voisins  
    for n in neighbours:
        #Si ce voisins a deja ete analyser , on le passe
        for closed_node in closed:
            if n == closed_node:
                continue
        #Affectation des valeurs g,h et F
        n.g=current_node.g+1
        n.h=penalite(n,winningNode).h
        n.f=n.g + n.h
        
        #Verifcation que la valeur g du voisin est superieure a celle de tout les noeuds présent dans open, si c'est le cas on passe
        for open_node in open:
            if n == open_node and n.g>open_node.g:
                continue
        #Rajout du voisin dans la liste open

        open.append(n)
        
    
        
        
    






pygame.init()  
screen = pygame.display.set_mode((1500,900),pygame.RESIZABLE)  
screen.fill([255,255,0])

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
myfont = pygame.font.SysFont('Comic Sans MS', 30)

annonce = "J'effectue : " + str(len(path)-1) + "coups "
textsurface = myfont.render(annonce, False, (0, 0, 0))
screen.blit(textsurface,(850,400))

path = path[::-1]



#Partie affichage du chemin 




for i in range(len(path)):
    if i+1 < len(path):
        if path[i].x > path[i+1].x:
            setattr(ia_board[path[i].y][path[i].x],'objectif','G')
            
        if path[i].x < path[i+1].x:
            setattr(ia_board[path[i].y][path[i].x],'objectif','D')
            
        if path[i].y > path[i+1].y:
            setattr(ia_board[path[i].y][path[i].x],'objectif','H')
          
        if path[i].y< path[i+1].y:
            setattr(ia_board[path[i].y][path[i].x],'objectif','B')
    pygame.time.wait(1000)   
    affichage(screen,ia_board,robot_ia)
    
    pygame.display.flip()


    










main = True        
while main: 
    
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            main = False
 
    pygame.display.flip()  