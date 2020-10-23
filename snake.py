import pygame
from random import randrange 
import pygame.freetype
import time
pygame.init()
WHITE = (225, 225, 225)
BLACK = (0, 0, 0)
RED = (225, 0, 50)
Hi = 480
We = 800
sise = 40
rcrd = 0
GAME_FONT = pygame.freetype.SysFont('Comic Sans MS', 20)
sc = pygame.display.set_mode((We,Hi))

# test on impuct
def if_imp(inf):
    j = len(inf)    
    for i in range(j-1):    
        if inf[j-1] in inf[:-1]:
            for i in range(20,120,20):
                pygame.draw.circle(sc,(RED),(inf[j-1][0]+20,inf[j-1][1]+20),i)  
            imp = True
            return(imp)    
def ask():
    #sc.fill(WHITE)
    while 1:
        GAME_ASK = pygame.freetype.SysFont('Comic Sans MS', 50)
        GAME_ASK.render_to(sc, (int(We/8), int(Hi/2.5)), 'Do you wont to play?', (100, 100, 100))
        GAME_MS = pygame.freetype.SysFont('Comic Sans MS', 30)
        GAME_MS.render_to(sc, (int(We/8), int(Hi/1.8)), 'Mouse left = yes     Mouse right = no ' , (250, 100, 100))
        GAME_MS.render_to(sc, (int(We/8), int(Hi/1.6)), 'dooble press button = speed up' , (250, 100, 100))
        pygame.display.update()
        for i in pygame.event.get():  
            #print(i)
            if i.type == pygame.QUIT:
                exit()  
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    return        
                if i.button == 3:
                    pygame.quit
                    exit()
        pygame.time.delay(200)

while 1:
    ask()
    x_r=y_r=x=y=80
    drc='E'
    inf=[(x,y)]
    k=3
    bil=0
    dly=180
    flag = imp =  False
    spd=1
    while  not imp:
        #random rect. coord
        if flag == False:
            flag = True
            while (x_r,y_r)  in inf:
                x_r = randrange(0, We-sise, sise)
                y_r = randrange(0, Hi-sise, sise)
            dly-=2
        
        for i in pygame.event.get():
            spd = 1  
            if i.type == pygame.QUIT:
                pygame.quit()
                exit()  
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    if drc == 'E' : break 
                    if drc == 'W' : spd = 0.3
                    drc='W'
                elif i.key == pygame.K_RIGHT:
                    if drc == 'W' : break 
                    if drc == 'E' : spd = 0.3
                    drc='E'
                elif i.key==pygame.K_UP:
                    if drc == 'S' : break 
                    if drc == 'N' : spd = 0.3
                    drc='N'
                elif i.key==pygame.K_DOWN:
                    if drc == 'N' : break
                    if drc == 'S' : spd = 0.3 
                    drc='S'

        if drc =='W':   x-=sise
        elif drc =='E': x+=sise
        elif drc =='N': y-=sise
        elif drc =='S': y+=sise  
        # move thru wools
        if x < 0:   x = We-sise   
        if x >= We: x = 0
        if y < 0:   y = Hi-sise
        if y >= Hi: y=0 
         # add coord to list     
        inf.append((x, y))
        
        # tponcate list to nessesory length
        if len(inf) > k:
            del inf[:-k]
            if inf[k-1] ==  (x_r, y_r):
                flag = False
                k+=1
                bil+=1
        # main code
        sc.fill(WHITE) 
        pygame.draw.rect(sc,(RED),(x_r,y_r,sise,sise))       
        for i in (range(len(inf))):
            pygame.draw.rect(sc,(BLACK),(inf[i][0],inf[i][1],sise,sise),7)
        imp=if_imp(inf)
        GAME_FONT.render_to(sc, (10, 10), str(bil), (100, 100, 100))  
        GAME_FONT.render_to(sc, (40, 10), 'rcrd ='+ str(rcrd), (100, 100, 100))   
        pygame.display.update()
        pygame.time.delay(int(dly*spd))
    if rcrd < bil: rcrd = bil
    
       