import pygame,sys,random
from pygame.locals import *

pygame.init()
#Open Pygame window
screen = pygame.display.set_mode((640, 480)) # add RESIZABLE or FULLSCREEN
#Title
pygame.display.set_caption("tic tac toe")
color=pygame.color.THECOLORS["black"]

tab= pygame.image.load("resources/morp_tab.png").convert()
tab.set_colorkey((0,0,0))
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
cpu_level=2
win=0
player=0
cpu=0
lose=0
draw=0
draw2=0
r=0
time=0
turn="player"
font=pygame.font.SysFont('Arial', 30)       

tab_case=[(170,90),(270,90),(370,90),
         (170,190),(270,190),(370,190),
         (170,290),(270,290),(370,290)]


t=tab_case
win_line=[ [t[0],t[1],t[2]], [t[3],t[4],t[5]],[t[6],t[7],t[8]],
           [t[0],t[3],t[6]], [t[1],t[4],t[7]], [t[2],t[5],t[8]],
           [t[0],t[4],t[8]], [t[6],t[4],t[2]] ]
           

pygame.key.set_repeat(400, 30)

while True:
  
  #loop speed limitation
  #30 frames per second is enought
  pygame.time.Clock().tick(100)
 
  for event in pygame.event.get():
    if event.type==pygame.QUIT:    #wait for events
      pygame.quit()
      sys.exit()
      
    #keyboard commands
    if event.type == KEYDOWN:
       if event.key == K_UP:
          if cpu_level<=1:
             cpu_level+=1
       if event.key == K_DOWN:
          if cpu_level>=1:
             cpu_level-=1
    #mouse commands
    if event.type == MOUSEBUTTONDOWN:
       if win or lose or draw:
          cross_list=[];circle_list=[];win=0;lose=0;draw=0;screen.fill(color);turn="player"
          screen.blit(tab,tab_pos);pygame.display.flip()
       if event.button == 1:
          if turn=="player":
             for case in tab_case:
               if event.pos[0]>case[0]and event.pos[0]<case[0]+100 \
               and event.pos[1]>case[1]and event.pos[1]<case[1]+100 :
                   if not case in cross_list and not case in circle_list:
                      selected=1
                      cross_list.append(case)
                      screen.blit(cross,case)
                      
             for line in win_line:
                 cont=0
                 for case in line:
                     for cross1 in cross_list:
                         if cross1==case:cont+=1
                 if cont==3 and not lose:
                    win=1
             if win:
                player+=1
             if selected:
                cont=0
                selected=0
                turn="cpu"
             
  if turn=="cpu" and not win:
    time+=1
    if time==3:
     time=0
     if not selected and cpu_level>=1:
       
           for line in win_line:
            if not selected:
               cont=0
               for case in line:
                  for circle1 in circle_list:
                   if circle1==case:cont+=1
                   
            if cont==2 and not selected:
               for case in line:
                   for circle1 in  circle_list:
                       if case_inspect!=circle1:
                          if not case in circle_list and not case in cross_list:
                           selected=1
                           circle_list.append(case)
                           screen.blit(circle,case)

                           
     if not selected and cpu_level==2:
       
           for line in win_line:
            if not selected:
               cont=0
               for case in line:
                  for cross1 in cross_list:
                   if cross1==case:cont+=1
                     
            if cont==2 and not selected:
               for case in line:
                   for cross1 in  cross_list:
                       if case!=cross1:
                          if not case in circle_list and not case in cross_list:
                           selected=1
                           circle_list.append(case)
                           screen.blit(circle,case)

                           
     if not selected and cpu_level>=1:
       
           for line in win_line:
            if not selected:
               cont=0
               for case in line:
                  for circle1 in circle_list:
                   if circle1==case:cont+=1
                  for cross1 in cross_list:
                   if cross1==case:cont=0
          
            if cont==1 and not selected:
              for index in range(len(line)):
                  for circle1 in  circle_list:
                    if not selected:
                      if line[index]==circle1 and line[index]!=line[len(line)-1]:
                        if not line[index+1] in circle_list and not line[index+1] in cross_list:
                          selected=1
                          circle_list.append(line[index+1])
                          screen.blit(circle,line[index+1])
                      elif line[index]==circle1 and line[index]==line[len(line)-1]:
                        if not line[index-1] in circle_list and not line[index-1] in cross_list:
                          selected=1
                          circle_list.append(line[index-1])
                          screen.blit(circle,line[index-1])

                          
     if not selected and cpu_level>=0:
       
       for case in tab_case:
         if not selected:
           cont=0
           r=random.randint(0,8)
           for cross1 in cross_list:
               if tab_case[r]==cross1:cont+=1
           for circle1 in circle_list:
               if tab_case==case:cont+=1
           if not cont:
              if not tab_case[r] in circle_list and not tab_case[r] in cross_list:
                 selected=1
                 circle_list.append(tab_case[r])
                 screen.blit(circle,tab_case[r])
          
     if not selected and cpu_level>=0:
       
       for case in tab_case:
         if not selected:
           cont=0
           for cross1 in cross_list:
               if cross1==case:cont+=1
           for circle1 in circle_list:
               if circle1==case:cont+=1
           if not cont:
              if not case in circle_list and not case in cross_list:
                 selected=1
                 circle_list.append(case)
                 screen.blit(circle,case)
                 
     for circle1 in circle_list:
         for line in win_line:
             cont=0
             for case in line:
                 if circle1==case:
                    inspect_line=line
                    for case_inspect in inspect_line:
                         for circle2 in  circle_list:
                             if case_inspect==circle2:
                                cont+=1         
             if cont==3:
                lose=1
     if lose:
        cpu+=1
     cont=0
     cont2=0
     selected=0
     turn="player"
     
  if not win and not lose and not draw:
    for case in tab_case:
        for cross1 in cross_list:
            if cross1==case:cont+=1
        for circle1 in circle_list:
            if circle1==case:cont+=1
        if cont==9:
           draw=1
           draw2+=1
    cont=0
    
  screen.fill(color)
  
  if win:
     text=font.render(("you win"), True, (0,250,0));screen.blit(text,(270,400))
  if lose:
     text=font.render(("you lose"), True, (250,0,0));screen.blit(text,(270,400))
  if draw:
     text=font.render(("draw"), True, (0,0,250));screen.blit(text,(285,400))
     
  text=font.render(("cpu level="+str(cpu_level)), True, (250,250,250));screen.blit(text,(480,0))
  text=font.render(("cpu="+str(cpu)), True, (250,0,0));screen.blit(text,(180,0))
  text=font.render(("player="+str(player)), True, (0,250,0));screen.blit(text,(0,0))
  text=font.render(("draw="+str(draw2)), True, (0,0,250));screen.blit(text,(340,0))

  screen.blit(tab,tab_pos)
  for cross_pos in cross_list:
      screen.blit(cross,cross_pos)
  for circle_pos in circle_list:
      screen.blit(circle,circle_pos)

  pygame.display.flip()
