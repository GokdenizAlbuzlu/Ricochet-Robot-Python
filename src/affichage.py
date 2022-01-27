import pygame
import Images
from classe import * 
def create_board():
         #-----------------------------------------------------------------Partie 1------------------------------------------------
    part1 = [] 
    a=0
    #Creer un tableau de 8 par 8 avec 64 objet different
    for l in range (8):
        ligne = []
        for c in range(8):
            ligne.append(Case()) #On insere directement la classe Case() , ce qui permet de creer directement des objets different
            a+=1
        part1.append(ligne)
        

    #On modifie maintenant les valeur qui change (mur interne et cible)

    setattr(part1[0][3],'est',True)

    setattr(part1[2][5],'objectif','EB')#Etoile Bleue
    setattr(part1[2][5],'est',True) 
    setattr(part1[2][5],'sud',True)

    setattr(part1[4][2],'objectif','CV')#Cercle Vert
    setattr(part1[4][2],'nord',True)
    setattr(part1[4][2],'est',True)

    setattr(part1[5][0],'nord',True)

    setattr(part1[5][7],'objectif','TR')#Triangle Rouge
    setattr(part1[5][7],'ouest',True)
    setattr(part1[5][7],'sud',True)

    setattr(part1[6][1],'objectif','PJ')#Planete Jaune
    setattr(part1[6][1],'nord',True)
    setattr(part1[6][1],'ouest',True)

    setattr(part1[7][7],'nord',True)
    setattr(part1[7][7],'ouest',True)
    #-----------------------------------------------------------------Partie 2------------------------------------------------

    part2 = [] 
    #Creer un tableau de 8 par 8 avec 64 objet different
    for l in range (8):
        ligne = []
        for c in range(8):
            ligne.append(Case()) #On insere directement la classe Case() , ce qui permet de creer directement des objets different
        part2.append(ligne)

    #On modifie maintenant les valeur qui change (mur interne et cible)

    setattr(part2[0][1],'est',True)

    setattr(part2[1][5],'objectif','TV') #Triangle Vert
    setattr(part2[1][5],'est',True) 
    setattr(part2[1][5],'sud',True)
            
    setattr(part2[1][7],'sud',True)
            
    setattr(part2[3][1],'objectif','PB') #Planète Bleue
    setattr(part2[3][1],'nord',True)
    setattr(part2[3][1],'ouest',True) 
            
    setattr(part2[4][6],'objectif','CR') #Cercle Rouge
    setattr(part2[4][6],'nord',True)
    setattr(part2[4][6],'est',True)
        
    setattr(part2[6][4],'objectif','EJ') # Etoile Jaune        
    setattr(part2[6][4],'sud',True)
    setattr(part2[6][4],'ouest',True)
            
    setattr(part2[7][0],'nord',True)
    setattr(part2[7][0],'est',True)

    #-----------------------------------------------------------------Partie 3------------------------------------------------

    part3 = [] 
    #Creer un tableau de 8 par 8 avec 64 objet different
    for l in range (8):
        ligne = []
        for c in range(8):
            ligne.append(Case()) #On insere directement la classe Case() , ce qui permet de creer directement des objets different
        part3.append(ligne)


    #On modifie maintenant les valeur qui change (mur interne et cible)

    setattr(part3[0][7],'ouest',True)
    setattr(part3[0][7],'sud',True)

    setattr(part3[1][4],'objectif','TJ')#Triangle Jaune
    setattr(part3[1][4],'ouest',True) 
    setattr(part3[1][4],'sud',True)

    setattr(part3[2][6],'objectif','CB')#Cercle Bleu
    setattr(part3[2][6],'nord',True)
    setattr(part3[2][6],'ouest',True)

    setattr(part3[3][0],'nord',True)

    setattr(part3[4][7],'objectif','MC')#Multicouleur = N'importe quel objectif
    setattr(part3[4][7],'est',True)
    setattr(part3[4][7],'nord',True)

    setattr(part3[5][1],'objectif','ER')#Etoile Rouge
    setattr(part3[5][1],'nord',True)
    setattr(part3[5][1],'est',True)

    setattr(part3[6][3],'est',True)
    setattr(part3[6][3],'sud',True)
    setattr(part3[6][3],'objectif','PV')
    setattr(part3[7][4],'est',True)

    #-----------------------------------------------------------------Partie 4------------------------------------------------

    part4 =[]
    #Creer un tableau de 8 par 8 avec 64 objet different
    for l in range (8):
        ligne = []
        for c in range(8):
            ligne.append(Case()) #On insere directement la classe Case() , ce qui permet de creer directement des objets different
        part4.append(ligne)


    #On modifie maintenant les valeur qui change (mur interne et cible)

    setattr(part4[0][0],'est',True)
    setattr(part4[0][0],'sud',True)

    setattr(part4[1][5],'objectif','TB')#Triangle Bleu
    setattr(part4[1][5],'ouest',True) 
    setattr(part4[1][5],'sud',True)

    setattr(part4[3][1],'objectif','CJ')#Cercle Jaune
    setattr(part4[3][1],'sud',True)
    setattr(part4[3][1],'est',True)

    setattr(part4[3][7],'sud',True)

    setattr(part4[5][6],'objectif','PR')#Planète Rouge
    setattr(part4[5][6],'est',True)
    setattr(part4[5][6],'nord',True)

    setattr(part4[6][2],'objectif','EV')#Etoile Vert
    setattr(part4[6][2],'nord',True)
    setattr(part4[6][2],'ouest',True)

    setattr(part4[7][3],'est',True)







    board=[]

    
    for i in range(8):
        
        
        board.append(part1[i]+part2[i])
    

    for i in range(8):

        
        board.append(part3[i]+part4[i])
        



    

    a=0
    b=0
    for element in board[0]:
        setattr(element,'nord',True)
    
    for element in board[15]:
        setattr(element,'sud',True)

    for ligne in board:    
        
        setattr(board[a][0],'ouest',True)
        a+=1 
        
    for ligne in board:    
        
        setattr(board[b][15],'est',True)
        b+=1 

    

   

    return board

#Fonction permettant de placer les robots sur le plateau 
def modify_board(board,robots):
    for i in range(16):
        for j in range(16):
            if board[i][j].robot.couleur != "O":
                setattr(board[i][j],'robot',Robot("O"))
    
    for robot in robots:
        setattr(board[robot.y][robot.x],'robot',robot)
    
    return board



#Fonction permettant d'afficher le chemin parcouru par l'IA
def affichage_bfs(screen,path,board):
    for element in path:
        for r in element:
            setattr(board[r.y][r.x],'robot',r)
        

        pygame.time.wait(1000)   
        affichage(screen,board,element)
        
        pygame.display.flip()


def affichage(screen,tab,robot):
   

    
    done = False  
   






    x=0
    y=0

    for ligne in tab:

        
        for element in ligne :
            
            
            
                image = pygame.image.load("Images/vide.png")
                screen.blit(image,(x,y))
            
                if  element.ouest == True :
                    image = pygame.image.load("Images/mur.png")
                    screen.blit(image,(x,y))
                    
                if element.est == True:
                    image = pygame.image.load("Images/mur.png")
                    screen.blit(image,(x+45,y))
                if element.nord == True:
                    image = pygame.image.load("Images/mur_horizontal.png")
                    screen.blit(image,(x,y))
                if element.sud ==True:
                    image = pygame.image.load("Images/mur_horizontal.png")
                    screen.blit(image,(x,y+45))
                if element.objectif=="EB":
                    image = pygame.image.load("Images/EB.png")
                    screen.blit(image,(x,y))
                if element.objectif=="EJ":
                    image = pygame.image.load("Images/EJ.png")
                    screen.blit(image,(x+5,y-1))
                if element.objectif=="EV":
                    image = pygame.image.load("Images/EV.png")
                    screen.blit(image,(x+5,y+5))
                if element.objectif=="ER":
                    image = pygame.image.load("Images/ER.png")
                    screen.blit(image,(x+1,y+5))
                if element.objectif=="CV":
                    image = pygame.image.load("Images/CV.png")
                    screen.blit(image,(x+2,y+5))
                if element.objectif=="CB":
                    image = pygame.image.load("Images/CB.png")
                    screen.blit(image,(x+5,y+5))
                if element.objectif=="CJ":
                    image = pygame.image.load("Images/CJ.png")
                    screen.blit(image,(x+1,y+2))
                if element.objectif=="CR":
                    image = pygame.image.load("Images/CR.png")
                    screen.blit(image,(x+1,y+5))
                
                if element.objectif=="PR":
                    image = pygame.image.load("Images/PR.png")
                    screen.blit(image,(x+1,y+5))
                if element.objectif=="PB":
                    image = pygame.image.load("Images/PB.png")
                    screen.blit(image,(x+5,y+5))
                if element.objectif=="PJ":
                    image = pygame.image.load("Images/PJ.png")
                    screen.blit(image,(x+5,y+5))
                if element.objectif=="PV":
                    image = pygame.image.load("Images/PV.png")
                    screen.blit(image,(x+1,y+1))
                if element.objectif=="TR":
                    image = pygame.image.load("Images/TR.png")
                    screen.blit(image,(x+5,y+2))
                if element.objectif=="TJ":
                    image = pygame.image.load("Images/TJ.png")
                    screen.blit(image,(x+5,y+1))
                if element.objectif=="TV":
                    image = pygame.image.load("Images/TV.png")
                    screen.blit(image,(x+2,y+2))
                if element.objectif=="TB":
                    image = pygame.image.load("Images/TB.png")
                    screen.blit(image,(x+5,y+2))
                if element.objectif=="MC":
                    image = pygame.image.load("Images/MC.png")
                    screen.blit(image,(x+1,y+5))


                if element.objectif=="H":
                    image = pygame.image.load("Images/H.png")
                    screen.blit(image,(x+1,y+5))
                if element.objectif=="B":
                    image = pygame.image.load("C:/Users/edbes/OneDrive/Bureau/IA41/Images/B.png")
                    screen.blit(image,(x+1,y+5))
                if element.objectif=="D":
                    image = pygame.image.load("C:/Users/edbes/OneDrive/Bureau/IA41/Images/D.png")
                    screen.blit(image,(x+1,y+5))
                if element.objectif=="G":
                    image = pygame.image.load("C:/Users/edbes/OneDrive/Bureau/IA41/Images/G.png")
                    screen.blit(image,(x+1,y+5))

                if  element.robot.couleur == "V":
                    image = pygame.image.load("Images/Ro_V.png")
                    screen.blit(image,(x+2,y+5))

                if   element.robot.couleur == "B" :
                    image = pygame.image.load("Images/Ro_B.png")
                    screen.blit(image,(x+2,y+5))

                if   element.robot.couleur =="J" :
                    image = pygame.image.load("Images/Ro_J.png")
                    screen.blit(image,(x+2,y+5))

                if   element.robot.couleur == "R" :
                    image = pygame.image.load("Images/Ro_R.png")
                    screen.blit(image,(x+2,y+5))


                x+=50
                if x==800:
                    x=0
            
        y+=50
    
def afficher_target(screen,target):
    if target=="EB":
        image = pygame.image.load("Images/GEB.png")
        
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="EJ":
        image = pygame.image.load("Images/GEJ.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="EV":
        image = pygame.image.load("Images/GEV.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="ER":
        image = pygame.image.load("Images/GER.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="CV":
        image = pygame.image.load("Images/GCV.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="CB":
        image = pygame.image.load("Images/GCB.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="CJ":
        image = pygame.image.load("Images/GCJ.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="CR":
        image = pygame.image.load("Images/GCR.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    
    if target=="PR":
        image = pygame.image.load("Images/GPR.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="PB":
        image = pygame.image.load("Images/GPB.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="PJ":
        image = pygame.image.load("Images/GPJ.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="PV":
        image = pygame.image.load("Images/GPV.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="TR":
        image = pygame.image.load("Images/GTR.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="TJ":
        image = pygame.image.load("Images/GTJ.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="TV":
        image = pygame.image.load("Images/GTV.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="TB":
        image = pygame.image.load("Images/GTB.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))
    if target=="MC":
        image = pygame.image.load("Images/GMC.png")
        image = pygame.transform.scale(image, (75,75))
        screen.blit(image,(365,365))