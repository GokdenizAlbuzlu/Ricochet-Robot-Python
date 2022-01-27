from classe import *




def move_robot(robot,board,direction):
        moving = True
        x =robot.x
        y =robot.y
        
            
        if direction == "D":
            setattr(board[robot.y][robot.x],'robot',Robot("O"))
            while moving:
                if board[robot.y][robot.x].sud==False and board[robot.y+1][robot.x].nord==False and board[robot.y+1][robot.x].robot.couleur=="O" :
                
                    robot.y+=1
                else:
                    moving = False
                    # if  board[y][x].val >=board[robot.y][robot.x].val:
                    
                    #     setattr(board[robot.y][robot.x],'robot',robot)
                        
                    #     return robot
                    # else:
                    #     robot.x = x
                    #     robot.y = y
                    #     return robot

                    setattr(board[robot.y][robot.x],'robot',robot)
                        
                    return robot
    
        if direction =="U":
            setattr(board[robot.y][robot.x],'robot',Robot("O"))
            while moving:
                if board[robot.y][robot.x].nord==False and board[robot.y-1][robot.x].sud==False and board[robot.y-1][robot.x].robot.couleur=="O" :
                    
                    robot.y-=1
        

                else:
                    moving = False
                
                    # if  board[y][x].val >=board[robot.y][robot.x].val:
                    #     setattr(board[robot.y][robot.x],'robot',robot)
                    #     return robot  
                    # else:
                    #     robot.x = x
                    #     robot.y = y
                    #     return robot
                    setattr(board[robot.y][robot.x],'robot',robot)
                        
                    return robot
        
        if direction =="R":
            setattr(board[robot.y][robot.x],'robot',Robot("O"))
            while moving:
                if board[robot.y][robot.x].est==False and board[robot.y][robot.x+1].ouest == False and board[robot.y][robot.x+1].robot.couleur=="O" :
                    robot.x+=1
                else:
                    moving=False
                    # if  board[y][x].val >=board[robot.y][robot.x].val:
                    #     setattr(board[robot.y][robot.x],'robot',robot)
                    #     return robot
                    # else:
                    #     robot.x = x
                    #     robot.y = y
                    #     return robot
                    setattr(board[robot.y][robot.x],'robot',robot)
                        
                    return robot

        if direction =="L":
            
            while moving:
                if board[robot.y][robot.x].ouest==False and board[robot.y][robot.x-1].est == False and board[robot.y][robot.x-1].robot.couleur=="O" :
                    robot.x-=1
                else:
                    moving=False
                    # if  board[y][x].val >=board[robot.y][robot.x].val:
                    #     setattr(board[robot.y][robot.x],'robot',robot)
                    #     return robot
                    # else:
                    #     robot.x = x
                    #     robot.y = y
                    #     return robot
      
                    setattr(board[robot.y][robot.x],'robot',robot)
                        
                    return robot


