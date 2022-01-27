from classe import *
#Fonction déplacement pour l'IA utilisant A*
def deplacement_sud(tableau,currentNode):
    deplacement = True
    cpt_move = 0
    
    ny=currentNode.y
    while deplacement:
        if tableau[ny][currentNode.x].sud==False and tableau[ny+1][currentNode.x].nord==False and tableau[ny+1][currentNode.x].robot.couleur=="O" :
            
            ny+=1
            cpt_move+=1

        else:
            deplacement = False
            if cpt_move !=0:
                return currentNode.x,ny
            else:
                return


def deplacement_nord(tableau,currentNode):
    deplacement = True
    cpt_move=0
    ny=currentNode.y
    while deplacement:
        if tableau[ny][currentNode.x].nord==False and tableau[ny-1][currentNode.x].sud==False and tableau[ny-1][currentNode.x].robot.couleur=="O" :
            
            ny-=1
            cpt_move+=1

        else:
            deplacement = False
            if cpt_move !=0:
                return currentNode.x,ny
            else:
                return

        
def deplacement_est(tableau,currentNode):
    deplacement = True
    cpt_move=0
    nx=currentNode.x
    while deplacement:
        if tableau[currentNode.y][nx].est==False and tableau[currentNode.y][nx+1].ouest==False and tableau[currentNode.y][nx+1].robot.couleur=="O" :
            
            nx+=1
            cpt_move+=1
    
        else:
            deplacement = False
            if cpt_move !=0:
                return nx,currentNode.y
            else:
                return



def deplacement_ouest(tableau,currentNode):

    deplacement = True
    cpt_move=0
    nx=currentNode.x
    while deplacement:
        if tableau[currentNode.y][nx].ouest==False and tableau[currentNode.y][nx-1].est==False and tableau[currentNode.y][nx-1].robot.couleur=="O" :
            
            nx-=1
            
            cpt_move+=1
        
        
        else:
            deplacement = False
            if cpt_move !=0:
                return nx,currentNode.y
            else:
                return
