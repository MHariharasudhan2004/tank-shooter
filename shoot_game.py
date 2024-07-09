import pygame
import random
import math
from pygame import mixer

#initialize pygame
pygame.init()
#create the screen
w=pygame.display.set_mode((785,600))
#title and icon
pygame.display.set_caption("My 2nd game")
img=pygame.image.load('combat.png')
pygame.display.set_icon(img)
#bg
bg_img=pygame.image.load('tank.png')
player_x=100
player_y=500
player_xchange=0
player_ychange=0
#bg music
mixer.music.load('background.wav')
mixer.music.play(-1)

def tanker(x,y):
    w.blit(bg_img,(x,y))
#bullet
bullet_img=pygame.image.load('bullet.png')
bullet_x=0
bullet_y=480
bulletX_change=0
bulletY_change=4
bullet_state="ready"
#score
score_value=0
font = pygame.font.Font('freesansbold.ttf',28)
textX =10
textY =10
#Game over
over_font=pygame.font.Font('custom_font.ttf',80)

def show_score(x,y):
    score = font.render("Score:" + str(score_value),True,(255,255,255))
    w.blit(score,(x,y)) 
def game_over_text():
    over_text=over_font.render("Game Over!",True,(255,0,0))
    w.blit(over_text,(200,250))
#background
background=pygame.image.load('bg.png')
#enemy
eny_img=[]
eny_x=[]
eny_y=[]
eny_change=[]
enyy_change=[]
num_of_eny = 5
for i in range(num_of_eny):
    if i%2==0:
        eny_img.append(pygame.image.load('soldier.png'))
        eny_x.append(random.randint(0,735))
        eny_y.append(random.randint(50,100))
        eny_change.append(2)
        enyy_change.append(20)
    else:
        eny_img.append(pygame.image.load('missile.png'))
        eny_x.append(random.randint(0,735))
        eny_y.append(random.randint(50,100))
        eny_change.append(2)
        enyy_change.append(20)
def enemy(eny_x, eny_y,i):
    w.blit(eny_img[i],( eny_x, eny_y)) 
#bullet function
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    w.blit(bullet_img,(x+16,y+10))
#collision function
def isCollision(eny_x,eny_y,bullet_x,bullet_y):
        distance=math.sqrt((math.pow(eny_x-bullet_x,2))+(math.pow(eny_y-bullet_y,2)))
        if distance<27:
            return True
        else:
            return False
#Game loop
running =True
while running:
    w.fill((255,215,0))
    w.blit(background,(0,0))
    
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                player_xchange = 5
            if event.key==pygame.K_LEFT:
                player_xchange=-5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('bullet.wav')
                    bullet_Sound.play()
                    bullet_x=player_x
                    fire_bullet(player_x,bullet_y)
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_xchange = 0
            
        if event.type == pygame.QUIT:
            running=False
   
    
    if(player_x<=0):
        player_x=0
    elif(player_y<=0):
        player_y=0
    elif(player_x>=700):
        player_x=700
    elif(player_y>=500):
        player_y=500
    #bullet movement
    if (bullet_y<=0):
        bullet_state="ready"
        bullet_y=480
    if bullet_state is "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y-=bulletY_change
    #enemy movement
    for i in range(num_of_eny):
        #Game over
        if eny_y[i]>470:
            for j in range(num_of_eny):
                eny_y[j]=2000
            game_over_text()
        if i%2==0:
            eny_x[i]+=eny_change[i]
            if(eny_x[i]>=736):
                    eny_change[i]=-2
                    eny_y[i]+=enyy_change[i]       
            elif(eny_x[i]<=0):
                    eny_change[i]=2
                    eny_y[i]+=enyy_change[i]
        else:
            #eny_x[i]+=eny_change[i]
            eny_y[i]+=(enyy_change[i])/60
            
        
        collision = isCollision(eny_x[i],eny_y[i],bullet_x,bullet_y)
        if collision:
            exp_Sound = mixer.Sound('explosion.wav')
            exp_Sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value +=1
            eny_x[i]=random.randint(0,735)
            eny_y[i]=random.randint(50,300)
        enemy(eny_x[i],eny_y[i],i)
    player_x+=player_xchange
    player_y+=player_ychange
    tanker(player_x,player_y)
    show_score(textX,textY)
    pygame.display.update()
