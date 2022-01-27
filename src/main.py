
#Importation des modules et fichier necessaire
import pygame
from pygame.constants import TIMER_RESOLUTION
import random
from classe import *
from affichage import *
from button import *
from victoire import * 
from choose_target import *
from BFS import *


#Fonction Principale
def game():


    
    #Fonction permettant de savoir quel robot est le robot gagnant

    def winningRobot(target):
        winningRobot=Robot("O")
        for lettre in target:
            if lettre=="B":
                winningRobot=Robot_Bleu
            if lettre=="R":
                winningRobot=Robot_Rouge

            if lettre=="J":
                winningRobot=Robot_Jaune

            if lettre=="V":
                winningRobot=Robot_Vert
            if lettre =="C":
                winningRobot = robot

        return winningRobot



    #Creation de la fenetre d'affichage du jeu
    pygame.init()  
    screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE)  
    screen.fill([0,0,0])
    
    

    main = True
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

    #Initialisation des robots
    robot=init_robot()
    Robot_Bleu = robot[0]
    Robot_Rouge = robot[1]
    Robot_Vert = robot[2]
    Robot_Jaune = robot[3]

    #Creation du tableau
    tableau = create_board()
 
    tableau = modify_board(tableau,robot)
    


    #Variable Utile pour le bon fonctionnement de l'interface

    fonttext = pygame.font.SysFont("comicsansms", 25)
    text = fonttext.render("Inserez le nombre de coups ", True, (112, 148, 124))
    screen.blit(text,(1000,150))
    inp_rect = pygame.Rect(1000,200,140,32)
   
    aC =  pygame.Color('lightskyblue3')
    pC = pygame.Color('gray15')
    basecolor = pygame.Color('gray')
    color =pC
    active = False

    #Creation des boutons de selections
    b1= button(screen,(850,400),"Red",basecolor)
    b2= button(screen,(950,400),"Blue",basecolor) 
    b3= button(screen,(1050,400),"Yellow",basecolor) 
    b4= button(screen,(1200,400),"Green",basecolor)     
    b5= button(screen,(1350,400),"IA",basecolor)     


    affichage(screen,tableau,robot)
    #Il y'a 17 tour dans le jeu
    for i in range(0,16): 
        #Boolen de victoire
        v = False
        #Selection d'une cible
        target = choose_target()

        #Initalisation de l'etat inital pour l'IA
        Initial_State = State(None,[],robot)
        Initial_State.create_child(create_board())

        #Determination du robot gagnant 
        wR=winningRobot(target)
        #Initialisation du nombre de coups annoncé par l'utilisateur
        nbr_de_coup = ''
        cpt = 0



        
        #On affiche la cible
        afficher_target(screen,target)
        pygame.display.flip()
        
        #Tant qu'il n'y a pas de victoire
        while v != True:
            afficher_target(screen,target)
            #Verification a chaque tour de boucle si le robot gagnant a atteint la cible
            v = victoire(target,tableau,wR) 
         
            for event in pygame.event.get():  
                #Nécessaire pour pouvoir modifier la taille de la fenetre
                if event.type == pygame.VIDEORESIZE:
                    screen.fill([0,0,0])
                    b1= button(screen,(850,400),"Red",basecolor)
                    b2= button(screen,(950,400),"Blue",basecolor) 
                    b3= button(screen,(850,500),"Yellow",basecolor) 
                    b4= button(screen,(1000,500),"Green",basecolor)   
                    b5= button(screen,(1350,400),"IA",basecolor)
                    affichage(screen,tableau,robot) 
                    afficher_target(screen,target)
                    screen.blit(text,(1000,150))
                
                #Fermeture de la fenetre
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit
                    break

                #Selection des Robots
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        currentRobot = Robot_Rouge
                        newcolor = pygame.Color('Red')
                        b1= button(screen,(b1.x,b1.y),"Red",newcolor)
                        b2= button(screen,(b2.x,b2.y),"Blue",basecolor) 
                        b3= button(screen,(b3.x,b3.y),"Yellow",basecolor) 
                        b4= button(screen,(b4.x,b4.y),"Green",basecolor)   
                        active=False
                    elif b2.collidepoint(pygame.mouse.get_pos()):
                        currentRobot = Robot_Bleu
                        newcolor = pygame.Color('Blue')
                        b1= button(screen,(b1.x,b1.y),"Red",basecolor)
                        b2= button(screen,(b2.x,b2.y),"Blue",newcolor) 
                        b3= button(screen,(b3.x,b3.y),"Yellow",basecolor) 
                        b4= button(screen,(b4.x,b4.y),"Green",basecolor)   
                        active=False
                    elif b3.collidepoint(pygame.mouse.get_pos()):
                        currentRobot = Robot_Jaune
                        newcolor=pygame.Color('Yellow')
                        b1= button(screen,(b1.x,b1.y),"Red",basecolor)
                        b2= button(screen,(b2.x,b2.y),"Blue",basecolor) 
                        b3= button(screen,(b3.x,b3.y),"Yellow",newcolor) 
                        b4= button(screen,(b4.x,b4.y),"Green",basecolor)   
                        active=False
                    elif b4.collidepoint(pygame.mouse.get_pos()):
                        currentRobot = Robot_Vert
                        newcolor = pygame.Color('Green')
                        b1= button(screen,(b1.x,b1.y),"Red",basecolor)
                        b2= button(screen,(b2.x,b2.y),"Blue",basecolor) 
                        b3= button(screen,(b3.x,b3.y),"Yellow",basecolor) 
                        b4= button(screen,(b4.x,b4.y),"Green",newcolor)   
                        active = False
                    elif b5.collidepoint(pygame.mouse.get_pos()):
                    
                        path =bfs(Initial_State,target,wR,tableau)
                        affichage_bfs(screen,path,tableau)
                        v=True
                    #Selection de l'input Box
                    elif inp_rect.collidepoint(pygame.mouse.get_pos()):
                        
                        active =True
                        color = aC
                    
                    else :
                        active = False


                #Gestion de l'input_box
                if active == True:
                    color = aC
                    pygame.draw.rect(screen,color,inp_rect,2)
                else:
                    color = pC
                    pygame.draw.rect(screen,color,inp_rect,2)


                if event.type == pygame.KEYDOWN:
                    #Recuperation de la valeur
                
                    if active == True :
                            if event.key == pygame.K_RETURN:
                                
                                color = pC
                                nbr_de_coup = int(nbr_de_coup)   
                                pygame.draw.rect(screen,[0,0,0],inp_rect)
                                active = False

                            if (event.key >= ord('0') and event.key <=ord('9') or event.key >= ord('0') and event.key <=ord('9')) or event.key ==pygame.K_BACKSPACE:
                                if len(nbr_de_coup)<2: 
                                    if event.key ==pygame.K_BACKSPACE:
                                        nbr_de_coup = nbr_de_coup[:-1]
                                        
                                        pygame.draw.rect(screen,[0,0,0],inp_rect)
                                        text = myfont.render(nbr_de_coup,True,(255,255,255))
                                        screen.blit(text,(inp_rect.x+5,inp_rect.y-5))
                                    
                                    else :
                                        nbr_de_coup+=event.unicode
                                        text = myfont.render(nbr_de_coup,True,(255,255,255))
                                        screen.blit(text,(inp_rect.x+5,inp_rect.y-5))
                                else:
                                    if event.key ==pygame.K_BACKSPACE:
                                        nbr_de_coup = nbr_de_coup[:-1]
                                        
                                        pygame.draw.rect(screen,[0,0,0],inp_rect)
                                        text = myfont.render(nbr_de_coup,True,(255,255,255))
                                        screen.blit(text,(inp_rect.x+5,inp_rect.y-5))
                                    
                    
                                    
                        
                    #Deplacement des robots
                    if event.key ==pygame.K_LEFT:
                        deplacement = True
                    
                        while deplacement:
                            if tableau[currentRobot.y][currentRobot.x].ouest==False and tableau[currentRobot.y][currentRobot.x-1].est==False and tableau[currentRobot.y][currentRobot.x-1].robot.couleur=="O"and cpt<nbr_de_coup :
                                
                                currentRobot.x-=1
                                
                                
                                setattr(tableau[currentRobot.y][currentRobot.x],'robot',currentRobot)
                                setattr(tableau[currentRobot.y][currentRobot.x+1],'robot',Robot("O"))
                  
                            

                            else:
                                deplacement=False
                                cpt+=1
                            
                            affichage(screen,tableau,robot)
                            pygame.display.flip()  

                
                    if event.key ==pygame.K_RIGHT:
                        deplacement = True
                    
                        while deplacement:
                            if tableau[currentRobot.y][currentRobot.x].est==False and tableau[currentRobot.y][currentRobot.x+1].ouest==False and tableau[currentRobot.y][currentRobot.x+1].robot.couleur=="O" and cpt<nbr_de_coup:
                                
                                currentRobot.x+=1
                                
                                setattr(tableau[currentRobot.y][currentRobot.x],'robot',currentRobot)
                                setattr(tableau[currentRobot.y][currentRobot.x-1],'robot',Robot("O"))
                            
                            
                            else:
                                deplacement=False
                                cpt+=1
                            affichage(screen,tableau,robot)
                            pygame.display.flip()  
                
                                
                    if event.key ==pygame.K_UP:
                        deplacement = True
                    
                        while deplacement:
                            if tableau[currentRobot.y][currentRobot.x].nord==False and tableau[currentRobot.y-1][currentRobot.x].sud==False and tableau[currentRobot.y-1][currentRobot.x].robot.couleur=="O" and cpt<nbr_de_coup :
                                
                                currentRobot.y-=1
                                
                                setattr(tableau[currentRobot.y][currentRobot.x],'robot',currentRobot)
                                setattr(tableau[currentRobot.y+1][currentRobot.x],'robot',Robot("O"))
                                

                            
                            
                                
                            else:
                                deplacement=False
                                cpt+=1
                            affichage(screen,tableau,robot)
                            pygame.display.flip()  
                            
                                
                    if event.key ==pygame.K_DOWN:
                        deplacement = True
                    
                        while deplacement:
                            if tableau[currentRobot.y][currentRobot.x].sud==False and tableau[currentRobot.y+1][currentRobot.x].nord==False and tableau[currentRobot.y+1][currentRobot.x].robot.couleur=="O" and cpt<nbr_de_coup :
                                
                                currentRobot.y+=1
                                
                                setattr(tableau[currentRobot.y][currentRobot.x],'robot',currentRobot)
                                setattr(tableau[currentRobot.y-1][currentRobot.x],'robot',Robot("O"))
                                

                            
                            
                                
                            else:
                                deplacement=False
                                cpt+=1
                            affichage(screen,tableau,robot)
                            pygame.display.flip()         
                        


                       
            
                pygame.display.flip()               
            
                
                

                
                
    while main: 
        
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                main = False
    
        pygame.display.flip()     


