import pygame, random

pygame.init()

"Settings_Display"
WINDOW_WIDTH, WINDOW_HEIGHT = 1122, 599
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Catch the Falling Gems")

"Settings_Game"
FPS = 60
clock = pygame.time.Clock()

"Game Values"
PLAYER_OG_LFP = 5
PLAYER_VELOCITY = 15

GEM_OG_VELOCITY = 5
GEM_ACCELERATION = 0.3

BUFFER_DIST = 100

score = 0
gem_velocity = GEM_OG_VELOCITY
player_lfp = PLAYER_OG_LFP
clown_xdir = random.choice([-1, 1])
clown_ydir = -1

#Basic Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255 )
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
#Game Specific Colors
GOLDEN_ORANGE = (249, 162, 51)
SOFTENED_PURPLE = (170, 78, 185)

"Set Images"
#Background Image
bg_image = pygame.image.load('background_image.jpg')
bg_rect = bg_image.get_rect()
bg_rect.topleft = (0, 0)

#Mining Cart
cart_image = pygame.image.load('mining-cart.png')
cart_rect = cart_image.get_rect()
cart_rect.center =  (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Green Gem
greengem_image = pygame.image.load('green_gem.png')
greengem_rect = greengem_image.get_rect()

#Red Gem
redgem_image = pygame.image.load('red_gem.png')
redgem_rect = redgem_image.get_rect()


"Set Text"
font_l = pygame.font.Font('Cathedral-9Ydly.ttf', 90)
font_s = pygame.font.Font('Cathedral-9Ydly.ttf', 40)

#Title
title_text = font_l.render("Catching Gems", True, GOLDEN_ORANGE)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, 70)

#Score
score_text = font_s.render("Score: "+str(score), True, SOFTENED_PURPLE)
score_rect = score_text.get_rect()
score_rect.topright = (WINDOW_WIDTH-40, 25)

#Life Points
lfp_text = font_s.render("Life Points: "+str(player_lfp), True, SOFTENED_PURPLE)
lfp_rect = lfp_text.get_rect()
lfp_rect.topright = (WINDOW_WIDTH-40, 60)

#Game Over
game_over_text = font_l.render("Game Over", True, RED)
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

#Win
win_text = font_l.render("VICTORY!", True, GOLDEN_ORANGE)
win_rect = win_text.get_rect()
win_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
#Continue
cont_text = font_s.render("Press any key to play again", True, SOFTENED_PURPLE)
cont_rect = cont_text.get_rect()
cont_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2-60)

"Audio"
bg_music = pygame.mixer.music.load('Background_music.mp3')
plink_sound = pygame.mixer.Sound('plink.wav')
fail_sound = pygame.mixer.Sound('fail.wav')
thud_sound = pygame.mixer.Sound('thud.wav')

"Main Game Loop"
pygame.mixer.music.play(-1, 0, 0)
running = True
while running:
    #Quit?
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    #Move Cart
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP or pygame.K_w] or cart_rect.bottom>=WINDOW_HEIGHT:
        cart_rect.y -= PLAYER_VELOCITY
    if keys[pygame.K_DOWN or pygame.K_s] or cart_rect.top<=0:
        cart_rect.y += PLAYER_VELOCITY
    if keys[pygame.K_LEFT or pygame.K_a] or cart_rect.right>=WINDOW_WIDTH:
        cart_rect.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT or pygame.K_d] or cart_rect.left<=0:
        cart_rect.x += PLAYER_VELOCITY

    #Move Green Gem
    if greengem_rect.y>WINDOW_HEIGHT:
        player_lfp -=1
        fail_sound.play()
        greengem_rect.y = 0+BUFFER_DIST
        greengem_rect.x = random.randint(64, WINDOW_WIDTH-64)
    else:
        greengem_rect.y += gem_velocity

    #Collsion Detection
    if cart_rect.colliderect(greengem_rect):
        score += 1
        plink_sound.play()
        gem_velocity += GEM_ACCELERATION
        greengem_rect.y = 0+BUFFER_DIST
        greengem_rect.x = random.randint(64, WINDOW_WIDTH-64)
        score += 1

    #Update Score + LFP
    score_text = font_s.render("Score: "+str(score), True, SOFTENED_PURPLE)
    lfp_text = font_s.render("Life Points: "+str(player_lfp), True, SOFTENED_PURPLE)

    #Game Over
    if player_lfp == 0:
        displayscreen.blit(game_over_text, game_over_rect)
        displayscreen.blit(cont_text, cont_rect)
        pygame.display.update()

        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    player_lfp = PLAYER_OG_LFP
                    score = 0
                    gem_velocity = GEM_OG_VELOCITY
                    cart_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    pygame.mixer.music.play(-1, 0, 0)
                    is_paused = False
                if event.type==pygame.QUIT:
                    is_paused = False
                    running = False
    #Win
    if score >= 45:
        displayscreen.blit(win_text, win_rect)
        displayscreen.blit(cont_text, cont_rect)
        pygame.display.update()

        pygame.mixer.music.stop()
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    player_lfp = PLAYER_OG_LFP
                    score = 0
                    gem_velocity = GEM_OG_VELOCITY
                    cart_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
                    pygame.mixer.music.play(-1, 0, 0)
                    is_paused = False
                if event.type==pygame.QUIT:
                    is_paused = False
                    running = False
    #Blit Items
    displayscreen.blit(bg_image, bg_rect)
    displayscreen.blit(cart_image, cart_rect)
    displayscreen.blit(greengem_image, greengem_rect)
    displayscreen.blit(title_text, title_rect)
    displayscreen.blit(score_text, score_rect)
    displayscreen.blit(lfp_text, lfp_rect)

    #Update + tick
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
