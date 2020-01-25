import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("TIC.TAC.TOE MENU")
def show_text(msg,x,y,color,n):
    fontobj= pygame.font.SysFont("courier",n)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))    
while True:
    screen.fill((255,255,255))
    show_text(('TIC TAC TOE'),20,70,(71,60,139),85)
    show_text(('TIC TAC TOE'),24,70,(131,111,255),85)
    show_text(('BY:MAHA MUTHU'),140,145,(205,16,118),40)
    show_text(('BY:MAHA MUTHU'),142,145,(255,105,180),40)

    pygame.draw.rect(screen, (100,149,237), (0, 300, 600, 50), 0)
    pygame.draw.rect(screen, (0,201,87), (0, 400, 600, 50), 0)
    show_text(('- PLAY -'),205,300,(0,0,0),40)
    show_text(('- PLAY -'),208,300,(255,255,255),40)
    show_text(('- QUIT -'),205,400,(0,0,0),40)
    show_text(('- QUIT -'),208,400,(255,255,255),40)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            a,b=event.pos
            if 0<a<600 and 300<b<350:
                import pygame
                import time
                from pygame.locals import *
                pygame.init()
                screen = pygame.display.set_mode((600,600))
                pygame.display.set_caption("TIC TAC TOE")
                a=-200
                b=-200
                n="x"
                z=0
                pygame.draw.rect(screen, (255,255,255) , (0,0,600,600), 0)
                pygame.draw.line(screen, (0,0,0), (200,0), (200,600), 5)
                pygame.draw.line(screen, (0,0,0), (400,0), (400,600), 5)
                pygame.draw.line(screen, (0,0,0), (0,200), (600,200), 5)
                pygame.draw.line(screen, (0,0,0), (0,400), (600,400), 5)
                WINNER=False
                win = {"1":"-",  "2":"-",   "3":"-",   "4":"-",  "5":"-",  "6":"-",  "7":"-",  "8":"-",  "9":"-"}
                def drawo(x,y):
                    pygame.draw.circle(screen,(255,128,0), (x,y), 80, 10)
                def drawx(x,y):
                    pygame.draw.line(screen, (255,20,147), (x, y), (x+150, y+150), 10)
                    pygame.draw.line(screen, (255,20,147), (x+150, y), (x, y+150), 10)
                def xwinner():
                    if win["1"]==win["2"]==win["3"]=='x' or win["4"]==win["5"]==win["6"]=='x' or win["7"]==win["8"]==win["9"]=='x' or win["1"]==win["4"]==win["7"]=='x' or win["2"]==win["5"]==win["8"]=='x' or win["3"]==win["6"]==win["9"]=='x' or win["1"]==win["5"]==win["9"]=='x' or win["3"]==win["5"]==win["7"]=='x':
                        print('X Player is the winner')
                        show_text(('PLAYER X IS THE WINNER!'),35,280,(0,0,255))
                def owinner():
                    if win["1"]==win["2"]==win["3"]=='o' or win["4"]==win["5"]==win["6"]=='o' or win["7"]==win["8"]==win["9"]=='o' or win["1"]==win["4"]==win["7"]=='o' or win["2"]==win["5"]==win["8"]=='o' or win["3"]==win["6"]==win["9"]=='o' or win["1"]==win["5"]==win["9"]=='o' or win["3"]==win["5"]==win["7"]=='o':
                        print('O Player is the winner')
                        show_text(('PLAYER O IS THE WINNER!'),35,280,(0,0,255))
                def tie(win):
                    if (win["1"]!='-' and win["2"]!='-' and win["3"]!='-' and
                        win["4"]!='-' and win["5"]!='-' and win["6"]!='-' and
                        win["7"]!='-' and win["8"]!='-' and win["9"]!='-'):
                            print('Game is a tie')
                            show_text(('GAME IS A TIE'),100,280,(0,0,255))
                def show_text(msg,x,y,color):
                    fontobj= pygame.font.SysFont("arial",50)
                    msgobj = fontobj.render(msg,False,color)
                    screen.blit(msgobj,(x,y))
                player=0
                while True:
                    for event in pygame.event.get():  
                        if event.type == QUIT:
                            pygame.quit()
                            exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            player=player+1
                            x,y=event.pos
                            if 0<x<200 and 0<y<200:
                                if win["1"]== "-":
                                    if n=="x": 
                                        a=25
                                        b=25
                                        drawx(a,b)
                                        win["1"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=100
                                        b=100
                                        drawo(a,b)
                                        win["1"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 200<x<400 and 0<y<200:
                                if win["2"]== "-":
                                    if n=="x": 
                                        a=225
                                        b=25
                                        drawx(a,b)
                                        win["2"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=300
                                        b=100
                                        drawo(a,b)
                                        win["2"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 400<x<600 and 0<y<200:
                                if win["3"]== "-":
                                    if n=="x": 
                                        a=425
                                        b=25
                                        drawx(a,b)
                                        win["3"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=500
                                        b=100
                                        drawo(a,b)
                                        win["3"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 0<x<200 and 200<y<400:
                                if win["4"]== "-":
                                    if n=="x": 
                                        a=25
                                        b=225
                                        drawx(a,b)
                                        win["4"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=100
                                        b=300
                                        drawo(a,b)
                                        win["4"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 200<x<400 and 200<y<400:
                                if win["5"]== "-":
                                    if n=="x": 
                                        a=225
                                        b=225
                                        drawx(a,b)
                                        win["5"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=300
                                        b=300
                                        drawo(a,b)
                                        win["5"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 400<x<600 and 200<y<400:
                                if win["6"]== "-":
                                    if n=="x": 
                                        a=425
                                        b=225
                                        drawx(a,b)
                                        win["6"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=500
                                        b=300
                                        drawo(a,b)
                                        win["6"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 0<x<200 and 400<y<600:
                                if win["7"]== "-":
                                    if n=="x": 
                                        a=25
                                        b=425
                                        drawx(a,b)
                                        win["7"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=100
                                        b=500
                                        drawo(a,b)
                                        win["7"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 200<x<400 and 400<y<600:
                                if win["8"]== "-":
                                    if n=="x": 
                                        a=225
                                        b=425
                                        drawx(a,b)
                                        win["8"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=300
                                        b=500
                                        drawo(a,b)
                                        win["8"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if 400<x<600 and 400<y<600:
                                if win["9"]== "-":
                                    if n=="x": 
                                        a=425
                                        b=425
                                        drawx(a,b)
                                        win["9"]="x"
                                        n="o"
                                    elif n=="o":
                                        a=500
                                        b=500
                                        drawo(a,b)
                                        win["9"]="o"
                                        n="x"
                                else:
                                    print('spot is already taken, choose another spot')
                            if player%2!=0:
                                xwinner()
                                tie(win)
                                break
                            if player%2==0:
                                owinner()
                                tie(win)
                                break
                                       
                    pygame.display.update()

            if 0<a<600 and 400<b<450:
                pygame.quit()
                exit()
                
            
