from classe import *




def move_penality(x,y,board,direction):
        moving = True
        min_value = 3
        cpt_1=0
        cpt_2 = 0
        cpt_3 = 0
        if direction == "D":
            
            while moving:
                
                if board[y][x].sud==False and board[y+1][x].nord==False and board[y+1][x].robot.couleur=="O" or board[y][x].val==1 or y==14:
                    if board[y][x].val==1 :
                    
                        cpt_1+=1
                        min_value = 2

                        return min_value
                    if board[y][x].val==2 :
                        
                        cpt_2 +=1
                   
                       
                        
                    y+=1
                  
                else:
                    moving = False
                   
                    min_value = 3
                    return min_value
                


    
        if direction =="U":
            moving = True
            min_value = 3
            while moving:
             
                if board[y][x].nord==False and board[y-1][x].sud==False and board[y-1][x].robot.couleur=="O" or board[y][x].val==1:
                    if board[y][x].val==1 :
                        cpt_1+=1
                        min_value = 2
                        return min_value
                    if board[y][x].val==2:
                        
                        cpt_2 +=1
                       
                   
                    
                    y-=1
        
                
                else:
                    moving = False
                    min_value = 3
                    return min_value
       
                   
                        
                
    
        if direction =="R":
            min_value = 3
            while moving:
                if board[y][x].est==False and board[y][x+1].ouest == False and board[y][x+1].robot.couleur=="O" or board[y][x].val==1 :
                    if board[y][x].val==1 :
                        cpt_1+=1
                        min_value = 2
                        return min_value
                    if board[y][x].val==2:
                        
                        cpt_2 +=1
                    
                    
                    x+=1
                else:
                    moving=False
                    min_value = 3
                    return min_value
               
                  

        if direction =="L":
            
            while moving:
                if board[y][x].ouest==False and board[y][x-1].est == False and board[y][x-1].robot.couleur=="O" or board[y][x].val==1:
                    if board[y][x].val==1 :
                        cpt_1+=1
                        min_value = 2
                        return min_value
                    if board[y][x].val==2:
                    
                        cpt_2 +=1
                    x-=1
                else:
                    moving=False
                    min_value = 3
                    return min_value
               

