# from os import system
import pygame
from pygame.constants import USEREVENT
pygame.init()
import random
import sys

pygame.mixer.init(frequency=44100,size=16,channels=1  ,buffer=512)

#-------Gravity variables i=0.20,k=0
gravity=0.20
bird_y_position=0
score=0
high_score=0
point_sound=0
def floorappers():
   
    # ---iduu display wallaper move
    screen.blit(bg_surface,(floor_x_position,0))
    screen.blit(bg_surface,(floor_x_position+288,0))
   
    #---iduu base move avuraduu
    screen.blit(bg_base,(floor_x_position,450))
    screen.blit(bg_base,(floor_x_position+288,450))
# pipe created and rect function made
def created_pipes():
    pipe_height=random.choice(height_list)
    bottom_pipe=pipe_surface.get_rect(midtop=(400,pipe_height ))
    top_pipe=pipe_surface.get_rect(midbottom=(400,pipe_height-200))
    return bottom_pipe,top_pipe
#-----------rect aaa mov pannraduu
def moving_pipes(pips):
    for pipe in pips:
        pipe.centerx-=2
    return pips
    

#-------move agura pip aaa blit pannrom
def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom>=512:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe=pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
#--------------check collison of bird rect vs pip rect and also tocuch top and bootom
def check_collision(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                # print("{collision")
                bird_hit.play()
                meme_music.play()
                return False
        if bird_rect.top<=-100 or bird_rect.bottom>=450:
            # print("sssssssssssss")
            bird_hit.play()
            return False
        return True
#--------------bird rotation function      (birds,rotationvalue,scalevalue)
def rotation_bird(birds):
    new_bird=pygame.transform.rotozoom(birds,bird_y_position*3,1)
    return new_bird

def score_display(game_state):
    if game_state=="game-on":
        score_surface=game_font.render(str(int(score)) ,True,(255,255,255))
        score_rect=score_surface.get_rect(center=(144,50))
        screen.blit(score_surface,score_rect)
    if game_state=="game-over":
        score_surface=game_font.render(str(int(score)) ,True,(255,255,255))
        score_rect=score_surface.get_rect(center=(144,50))
        screen.blit(score_surface,score_rect)

        highscore_surface=game_font.render(f"HiGhScore :{str(int(score))}" ,True,(234,67,53))
        highscore_rect=highscore_surface.get_rect(center=(144,420))
        screen.blit(highscore_surface,highscore_rect)
def update_high_score(score,high_score):
        if score>=high_score:
            high_score=score
        return high_score


#----display size  
screen=pygame.display.set_mode((288,512))
 #-- FPS gamekuu idaa thandi pogadu (((((clock-->C--capital "c")))))
clock=pygame.time.Clock()

#-----------iduu oru variabl ithay vachu tha game on /off control pannrom

game_active=True

#----- iduu photoo location
bg_surface=pygame.image.load("Game Image/background-night.png")
bg_base=pygame.image.load("Game Image/base.png").convert()

#------------bird appers and collid on game 

bird_source=pygame.image.load("Game Image/redbird-midflap.png").convert_alpha()
bird_rect=bird_source.get_rect(center=(78,252))

end_screen=pygame.image.load("Game Image/message.png").convert_alpha()
end_screen_rect=end_screen.get_rect(center=(150,252))
#------------- pipe appers list, pipe 1200 millisec kalichu varanum nuu "like a timer"
pipe_surface=pygame.image.load("Game Image/pipe-red.png").convert()
pipe_list=[]
spwanpipe=USEREVENT
pygame.time.set_timer(spwanpipe,1200)

#------------font locations

game_font=pygame.font.Font("Game Fonts/Lover.ttf",40)

#------------------sounds effect
flap_sound=pygame.mixer.Sound("Game sounds/sfx_wing.wav")
bird_hit=pygame.mixer.Sound("Game sounds/sfx_hit.wav")
bird_points=pygame.mixer.Sound("Game sounds/sfx_point.wav")
meme_music=pygame.mixer.Sound("Game sounds/Directed-by-Robert-B-Weide-Sound-Effect-Perfect-Cut_BmBxuXd7ifk.mp3")


pygame.mixer.music.load("Game sounds/PUBG-Theme-Song-2Scratch-Trap-Remix_afFD-0TmIGg.mp3")
pygame.mixer.music.play(-1)

pygame.display.set_caption("Freaky flappyBird")
#-------------pipe random heightt list
height_list=[200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400]

#------------- iduu floor_x_ surface ku vulla i=0
floor_x_position=0

#------- iduu while loop user taa event vanguraduu
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    #------------ action Nadakurathukuu space button
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and game_active:
             bird_y_position=0
             bird_y_position-=7
             flap_sound.play()
             
        #----------------iduu oru function key ddown =out anaa odanaa marupidiyum sac amukunaa game varum
            if event.key==pygame.K_SPACE and game_active==False:
                game_active=True
        #------------------- iduvum mella vulla event-key kuda santhadu than iduu clear panna use aguthu
                pipe_list.clear()
                bird_rect.center=(78,252)
                bird_y_position=0
                score=0
                meme_music.stop()

    #------------iduu 1200millisec paituna iduu ndakum "spanpipe"
        if event.type==spwanpipe:
            pipe_list.extend(created_pipes())
        #   print (pipe_list)

            
    #---------------iduu i=i-1------floor_x_position=floor_x_postion-1
    floor_x_position-=1
    floorappers()

    

   

#------------iduu if loop frame fulla mudinga marupidiyum modalla irunduu kondu varaa
    if floor_x_position<=-288:
        floor_x_position=0

    

#--------------i=i+1,
    if game_active:
        bird_y_position=bird_y_position+gravity
        bird_rect.centery=bird_y_position+bird_rect.centery
        rotataion_option=rotation_bird(bird_source)
 #rect blaa vulla ellam inga irunduu thaa edukkom

        pipe_list=moving_pipes(pipe_list)
        draw_pipes(pipe_list)
           
           
        screen.blit(rotataion_option,bird_rect) 
            
            
            
        game_active=check_collision(pipe_list)
        score+=0.1
        # point_sound+=0.1
        # if point_sound>1.0:
        #     bird_points.play()
        #     point_sound=0
            
        score_display("game-on")
    else:
        score_display("game-over")
        high_score=update_high_score(score,high_score)
        screen.blit(end_screen,end_screen_rect)
    pygame.display.update()
    clock.tick(120)