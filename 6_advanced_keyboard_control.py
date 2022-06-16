import pygame
import random

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Continuous Keyboard Motion")

"Settings"
Velocity = 3 #當鍵盤按下時，改變
FPS = 70 #FreqPerSec
clock = pygame.time.Clock()

"Colors"
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
SAKURA = (246, 203, 218)
TIFFANY = (10, 186, 181)
GREY_BLUE_D = (75, 117, 143)
CORAL_ORANGE = (247, 135, 99)
SOFT_GREY = (203, 205, 207)

"Import Image"
dragon_image = pygame.image.load("dragon_icon.png")
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.center = (25, 25)

coin_image = pygame.image.load("coin.png")
coin_image_rect = coin_image.get_rect()
coin_image_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2) #400, 300

"Main Loop"
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #list all keys being pressed
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a])and dragon_image_rect.left>0: #left
        dragon_image_rect.x -= Velocity
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and dragon_image_rect.right<WINDOW_WIDTH:#right
        dragon_image_rect.x += Velocity
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and dragon_image_rect.top>0: #up
        dragon_image_rect.y -= Velocity
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and dragon_image_rect.bottom<WINDOW_HEIGHT:#down
        dragon_image_rect.y += Velocity

    #Check for collision between sprites
    if dragon_image_rect.colliderect(coin_image_rect):
        print("Hit")
        coin_image_rect.x = random.randint(0, WINDOW_WIDTH-32)
        coin_image_rect.y = random.randint(0, WINDOW_HEIGHT-32)


    displayscreen.fill((0, 0, 0)) #Fill Screen to Cover extra images of sprite
    
    pygame.draw.rect(displayscreen, (0, 255, 0), dragon_image_rect, 1)
    pygame.draw.rect(displayscreen, (241, 181, 82), coin_image_rect, 1)
    
    displayscreen.blit(dragon_image, dragon_image_rect)#blit dragon
    displayscreen.blit(coin_image, coin_image_rect)#Blit Coin
    pygame.display.update()#Update Display
    clock.tick(FPS) #Clock Tick (while loop時脈is controled by FPS setting->can only move 3*70 places/sec)

pygame.quit()