#Importation des fichiers nécessaires
from BFS_Moves import * 
from classe import *
from affichage import * 
from victoire import * 
#Importation des modules nécessaires
import pickle
from timeit import default_timer as timer


 




#Classe Etat utilisée pour l'algorithme BFS
class State: 
   
    __slots__ =('parent','childs','robots')
    
    def __init__(self,parent,childs,robots):
        self.parent = parent
        self.childs = childs
        self.robots = robots
        


    #Fonction permettant de creer tout les enfant d'un etat
    def create_child(self,board):
        string  = ["U","D","L","R"]
        for s in range(4):
            for i in range(4):
                
                #On copie les objets de manière a ce qu'il ne changent uniquement dans la liste 
                temp = pickle.loads(pickle.dumps(self.robots))
           
                
                #On récupere le robot a bouger et on l'enelve de la liste
                temp_robot = temp.pop(i)
            
                
                
        
                #On rajoute le robot avec la nouvelle position dans la liste
                #Cas ou le robot se deplace verticalement
                if s<= 1:
                    
                    if temp_robot.y == move_robot(temp_robot,modify_board(board,self.robots),string[s]).y :
                    
                         continue
                    else : 
                        temp.insert(i,move_robot(temp_robot,modify_board(board,self.robots),string[s]))                     
                        self.childs.append(State(self,[],temp))
                #Cas ou le robot se deplace horizontalement
                else : 
                    if temp_robot.x == move_robot(temp_robot,modify_board(board,self.robots),string[s]).x :
                         continue
                    else : 
                        temp.insert(i,move_robot(temp_robot,modify_board(board,self.robots),string[s]))                     
                        self.childs.append(State(self,[],temp))
                    
            

    def check_visited (self,list):
    
        if self.robots in list:
              
            # if elem == self.robots  :
                
                return True

#Fonction permettant de verifier si des etats sont équivalents ou non   
def checkEquivalence(state,visited,wR):

    
    
    for elem in visited:
        
        for i in range(4):
            if wR.couleur == state.robots[i].couleur and elem.robots[i].x == state.robots[i].x and elem.robots[i].y==state.robots[i].y:
               
                samePos = True
                break
            else:
                return False
        if samePos ==True :
            
            if elem.robots[0].x == state.robots[0].x and  elem.robots[0].y == state.robots[0].y and elem.robots[1].x == state.robots[1].x and  elem.robots[1].y == state.robots[1].y and elem.robots[2].x == state.robots[2].x and  elem.robots[2].y == state.robots[2].y and elem.robots[3].x == state.robots[3].x and  elem.robots[3].y == state.robots[3].y:
                samePos = False
                return True
            else:
                return False



#Algorithme BFS

def bfs(initial_state,target,winningRobot,board):
    
   
    visited  =[]
    queue = [initial_state]




    find = False

    
    while not find: 
        #On recupere l'etat présent en debut de liste
        s = queue.pop(0)

       
        
 
       
       #On verifie si l'etat en cours d'analyse a des enfants ou non 
        if not s.childs:
            
            s.create_child(board)
        
       #Recherche d'une solution
        for child in s.childs:
            for r in child.robots:

           
            
                if  r.couleur == winningRobot.couleur :
                    if victoire(target,create_board(),r):
                        path=[]
                        parent = child
                        while parent !=None:
                            path.append(parent.robots)
                            parent = parent.parent
                        
          
                       #On renvoie le chemin a l'envers, afin que le robot se déplace dans le bon sens
                        return path[::-1]
          

                
            #On verifie si l'etat est un etat "equivalent"
            if checkEquivalence(child,visited,winningRobot)==True:
                continue
            
            #On verifie si l'etat a deja été visiter ou non
            if child.check_visited(visited)!=1:
                
                visited.append(child.robots)
              
                queue.append(child)
                
     
      
      
       
                
                
           
    




























    












