import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap
import time
import numpy as np
import ctypes
from tkinter import simpledialog
import random

def GetWindowRectDesktop():   
    user32 = ctypes.windll.user32
    w,h = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)
    return (w, h)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0,  255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)




pygame.font.init()
#font = pygame.font.Font('freesansbold.ttf', 32)

font=pygame.font.SysFont('timesnewroman',  20)

w, h = GetWindowRectDesktop()
w , h = w-50, h-50



def main():
    #user_row_col=simpledialog.askinteger(title="Input ROW/COL",prompt="enter grid size",minvalue=0,maxvalue=100)
    #print(user_row_col)
    dimensions = (h,w)
    start=(random.randint(0,w),
        random.randint(0,h))
    goal=(random.randint(0,w),
        random.randint(0,h))

    obsdim=100
    obsnum=random.randint(0,40)
    iteration=0
    t1=0

    pygame.init()

    map=RRTMap(start,goal,dimensions,obsdim,obsnum)
    graph=RRTGraph(start,goal,dimensions,obsdim,obsnum)
    win = map.access2Window()

    obstacles=graph.makeobs()
    map.drawMap(obstacles)

    #t1=time.time()
    startTime=time.time()

    while (not graph.path_to_goal()):

        """
        time.sleep(0.005)
        elapsed=time.time()-t1
        t1=time.time()
        #raise exception if timeout
        if elapsed > 10:
            print('timeout re-initiating the calculations')
            raise
        """
        
        if iteration % 10 == 0:
            X, Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                             map.edgeThickness)

        
        else:
            X, Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad*2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]),
                             map.edgeThickness)

        #if iteration % 5 == 0:

        pygame.display.update()
        iteration += 1
    path2goGS = graph.getPathCoords()
    duration = np.round(time.time()-startTime,4) 
    memory = graph.memory() * 4
    map.drawPath(path2goGS)


   
   
    text1 =f'Size: {dimensions}'
    text2 = f'cells: {dimensions[0] * dimensions[1]}'
    text3 = f'start: {start}'
    text4 = f'Goal: {goal}'
    text5 = f'Time: {duration}'
    text6 = f'Memory: {memory}'
   
    text1 = font.render(text1, True, GREEN, WHITE)
    text2 = font.render(text2, True, GREEN, WHITE)
    text3 = font.render(text3, True, GREEN, WHITE) 
    text4 = font.render(text4, True, GREEN, WHITE) 
    text5 = font.render(text5, True, RED, WHITE) 
    text6 = font.render(text6, True, RED, WHITE) 
    

    
    L = 300#max(len(t1),len(t2),len(t3))

    win.blit(text1, (w-L, 0))
    win.blit(text2, (w-L, 25))
    win.blit(text3, (w-L, 50))
    win.blit(text4, (w-L, 75))
    win.blit(text5, (w-L, 100))
    win.blit(text6, (w-L, 125))


    pygame.display.update()
    #pygame.event.clear()
    #pygame.event.wait(0)
    
def draw_text(win,X,Y, msg, font, forecolor, bg):
    text=font.render(msg,True,forecolor,bg)
    textRect=text.get_rect()
    textRect.center=(X,Y)
    win.blit(text,textRect)
    pygame.display.update()

if __name__ == '__main__':
    """
    result=False
    while not result:
        try:
            main()
            result=True
        except:
            result=False
    """
    running = True
    first =True

    while running:
        try:
            if first:
                main()
                first =False
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  running = False
                elif event.type == pygame.KEYDOWN:
                    main()
            """
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                running = False
            if keys[pygame.K_CLEAR]:
                main()
            """
        except:
            pass
    pygame.quit()
    quit()


























