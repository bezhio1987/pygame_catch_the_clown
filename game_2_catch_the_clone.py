import pygame,random
 

#initialize pygame
pygame.init()

#create a display surface and set its caption
WINDOW_WIDTH = 945
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("catch the clone")



# define a clock to slow down the while loop and make sure it runs at the same speed on every single computer (FPS = frame per second)
FPS  = 60
clock = pygame.time.Clock()
#VELOCITY = 10 it runs 10 times a second


#set game values
PLAYER_STARTING_LIVES = 5
CLOWN_STARTING_VELOCITY = 3
CLOWN_ACCELERATION = 0.5

score = 0
player_lives = PLAYER_STARTING_LIVES
clown_velocity = CLOWN_STARTING_VELOCITY
clown_dx = random.choice([-1,1])  # direction in x 
clown_dy = random.choice([-1,1])


#colors
BLUE = (1,175,209)
YELLOW = (248, 231,28)

#set fonts
font = pygame.font.Font("Franxurter.ttf", 32)

#set text 
title_text = font.render("Catch the Clone", True, BLUE)
title_rect = title_text.get_rect()
title_rect.topleft = (50, 10)

score_text = font.render("score: "+str(score), True, YELLOW)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH-50 , 10)

lives_text = font.render("lives: "+str(player_lives), True, YELLOW)
lives_rect = lives_text.get_rect()
lives_rect.topright = (WINDOW_WIDTH-50 , 50)

game_over_text = font.render("Game Over!", True, BLUE, YELLOW)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_HEIGHT//2 , WINDOW_HEIGHT//2)

continue_text = font.render("Click anywhere to play again!", True, BLUE, YELLOW)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_HEIGHT//2 , WINDOW_HEIGHT//2+ 60)

#set music
hit_sound = pygame.mixer.Sound("click_sound.wav")
miss_sound = pygame.mixer.Sound("miss_sound.wav")
pygame.mixer.music.load("ctc_background_music.wav")

#set images
bg_img = pygame.image.load("background.png")
bg_rect = bg_img.get_rect()
bg_rect.topleft = (0,0)

clown_img = pygame.image.load("clown.png")
clown_rect = clown_img.get_rect()
clown_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)


#the main game loop
pygame.mixer.music.play(-1, 0.0)
running = True
while running:
    #lopp through a list of ecents 
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
           running = False 
    
    #move the clown
    clown_rect.x += clown_dx*clown_velocity
    clown_rect.y += clown_dy*clown_velocity

    #bounce the clown when its off the screen
    if clown_rect.left <= 0 or clown_rect.right >= WINDOW_WIDTH:
        clown_dx *= -1
    if clown_rect.top <=0 or clown_rect.bottom >= WINDOW_HEIGHT:
        clown_dy *= -1
     
    #blit the bg
    display_surface.blit(bg_img, bg_rect)
    display_surface.blit(clown_img, clown_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(score_text, score_rect)
    display_surface.blit(lives_text, lives_rect)
 
 

    #update the display
    pygame.display.update()
    
    #tick the clock
    clock.tick(FPS)

           
# end the  game
pygame.quit()
