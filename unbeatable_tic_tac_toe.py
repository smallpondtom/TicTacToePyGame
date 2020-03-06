import pygame,sys,random
from minmax import *
from pygame.locals import *

pygame.init()
#Open Pygame window
screen = pygame.display.set_mode((640, 480)) # add RESIZABLE or FULLSCREEN
#Title
pygame.display.set_caption("unbeatable tic tac toe")

color=pygame.color.THECOLORS["black"]

tab2= pygame.image.load("resources/morp_tab.png").convert()
tab2.set_colorkey((0,0,0))
tab_pos =(170,90)

cross= pygame.image.load("resources/cross.png").convert()
cross.set_colorkey((0,0,0))
cross_list=[]

circle= pygame.image.load("resources/circle.png").convert()
circle.set_colorkey((0,0,0))
circle_list=[]
inspect_line=[]
cont=0
selected=0
cpu_level=3
player=0
cpu=0
draw2=0
r=0
time=0
turn="player"
font=pygame.font.SysFont('Arial', 30)       

tab_case=[(170,90),(270,90),(370,90),
         (170,190),(270,190),(370,190),
         (170,290),(270,290),(370,290)]


t2=tab_case
win_line2=[ [t2[0],t2[1],t2[2]], [t2[3],t2[4],t2[5]], [t2[6],t2[7],t2[8]],
           [t2[0],t2[3],t2[6]], [t2[1],t2[4],t2[7]], [t2[2],t2[5],t2[8]],
           [t2[0],t2[4],t2[8]], [t2[6],t2[4],t2[2]] ]
           

pygame.key.set_repeat(400, 30)

while True:
  
  #loop speed limitation
  #30 frames per second is enought
  pygame.time.Clock().tick(3)
 
  for event in pygame.event.get():   #wait for events
    if event.type==pygame.QUIT:
      pygame.quit()
      sys.exit()
      
    #keyboard commands
    if event.type == KEYDOWN:
       if event.key == K_UP:
          if cpu_level<=2:
             cpu_level+=1
       elif event.key == K_DOWN:
          if cpu_level>=2:
             cpu_level-=1
             
       if cpu_level==1:depth=0
       elif cpu_level==2:depth=5
       elif cpu_level==3:depth=9
       
    #mouse commands
    if event.type == MOUSEBUTTONDOWN:
       if win() or lose() or draw():
          cross_list=[];circle_list=[];screen.fill(color);turn="player"
          screen.blit(tab2,tab_pos);pygame.display.flip();init(n=0);update()
       if event.button == 1:
          if turn=="player":
             for i in range(9):
               if event.pos[0]>tab_case[i][0]and event.pos[0]<tab_case[i][0]+100 \
               and event.pos[1]>tab_case[i][1]and event.pos[1]<tab_case[i][1]+100 :
                   if not tab_case[i] in cross_list and not tab_case[i] in circle_list:
                      selected=1
                      tab[i]=2;update();copy_tab()
                      cross_list.append(tab_case[i])
                      screen.blit(cross,tab_case[i])
                      
             if draw():draw2+=1        
             if lose():
                player+=1
             if selected:
                cont=0
                selected=0
                turn="cpu"
             
  if turn=="cpu" and not lose() and not draw():
     time+=1
     if time==3:
        time=0
        best_move=get_best_move(depth)
        for i in range(9):
            if tab_case[i]==tab_case[best_move]:
               if not tab_case[i] in cross_list and not tab_case[i] in circle_list:
                  selected=1
                  tab[i]=1;update()
                  circle_list.append(tab_case[i])
                  screen.blit(circle,tab_case[i])
                  
        if draw():draw2+=1
        if win():
           cpu+=1
        if selected:
           cont=0
           cont2=0
           selected=0
           turn="player"

  
  screen.fill(color)
  
  if lose():
     text=font.render(("you win"), True, (0,250,0));screen.blit(text,(270,400))
  if win():
     text=font.render(("you lose"), True, (250,0,0));screen.blit(text,(270,400))
  if draw():
     text=font.render(("draw"), True, (0,0,250));screen.blit(text,(285,400))
     
  text=font.render(("cpu level="+str(cpu_level)), True, (250,250,250));screen.blit(text,(480,0))
  text=font.render(("cpu="+str(cpu)), True, (250,0,0));screen.blit(text,(180,0))
  text=font.render(("player="+str(player)), True, (0,250,0));screen.blit(text,(0,0))
  text=font.render(("draw="+str(draw2)), True, (0,0,250));screen.blit(text,(340,0))

  screen.blit(tab2,tab_pos)
  for cross_pos in cross_list:
      screen.blit(cross,cross_pos)
  for circle_pos in circle_list:
      screen.blit(circle,circle_pos)

  pygame.display.flip()
