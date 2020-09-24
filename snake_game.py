import pygame
import random
pygame.init()
win=pygame.display.set_mode((900,600))
pygame.display.set_caption("My Snake")
x=45
y=55
size=30
v=5
vx=0
vy=0
score=0
l=1
snk_list = []
running=True
fx=random.randint(20,450)
fy=random.randint(20,300)
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)


def text_display(text,color,x,y):
    scr_text=font.render(text,True,color)
    win.blit(scr_text,(x,y))

def plot_snake(win,color,snk_list,size):
    for x,y in snk_list:
        pygame.draw.rect(win,color,(x,y,size,size))



def welcome():
    running=True
    text_display(("WELCOME TO SNAKE GAME!"),(255,0,0),200,300)
    text_display(("PRESS ENTER TO START"),(255,0,0),170,350)
    while running:
        win.fill((150,250,100))
        text_display(("WELCOME TO SNAKE GAME!"),(255,0,0),200,300)
        text_display(("PRESS ENTER TO START"),(255,0,0),170,350)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()
        pygame.display.update()
        clock.tick(50)


def gameloop():
    x=45
    y=55
    size=30
    v=5
    vx=0
    vy=0
    score=0
    l=1
    snk_list = []
    running=True
    gameover=False
    fx=random.randint(20,450)
    fy=random.randint(20,300)
    while running:
        if gameover:
            win.fill((0,0,0))
            text_display("GAME OVER!TRY AGAIN",(255,0,0),200,300)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        gameloop()
        
            
        else:
        
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running=False
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        vx=-v
                        vy=0
                    if event.key==pygame.K_RIGHT:
                        vx=v
                        vy=0
                    if event.key==pygame.K_UP:
                        vy=-v
                        vx=0
                    if event.key==pygame.K_DOWN:
                        vy=v
                        vx=0
            x=x+vx
            y=y+vy
            head = []
            head.append(x)
            head.append(y)
            snk_list.append(head)
        
                             
            if abs(x-fx)<10 and abs(y-fy)<10:
                fx=random.randint(20,450)
                fy=random.randint(20,300)
                score=score+10
                l=l+5
            if len(snk_list)>l:
                del snk_list[0]
            if x<0 or x>900 or y<0 or y>600:
                gameover=True
            if head in snk_list[:-1]:
                gameover=True
             
                          
        
            win.fill((0,0,0))
            plot_snake(win,(255,0,0),snk_list,size)
            pygame.draw.rect(win,(0,255,0),(fx,fy,size,size))
            text_display(("Score ="+str(score)),(0,255,0),5,5)                     
        pygame.display.update()
        clock.tick(50)
welcome()
pygame.quit()