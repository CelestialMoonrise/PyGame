import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Keyboard Controled")

Velocity = 50 #當鍵盤按下時，改變輛=10

"Import Image"
dragon_image = pygame.image.load("dragon_icon.png")
dragon_image_rect = dragon_image.get_rect()
dragon_image_rect.topleft = (0, 0)

dragon_image_r = pygame.image.load("dragon_icon_r.png")
dragon_image_r_rect = dragon_image_r.get_rect()
dragon_image_r_rect.topright = (WINDOW_WIDTH, 0)

"Main Loop"
running = True
while running==True:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            running=False
        #check key motion
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                dragon_image_rect.x = dragon_image_rect.x-Velocity
            if event.key==pygame.K_RIGHT:
                dragon_image_rect.x = dragon_image_rect.x+Velocity
            if event.key==pygame.K_UP:
                dragon_image_rect.y = dragon_image_rect.y-Velocity
            if event.key==pygame.K_DOWN:
                dragon_image_rect.y = dragon_image_rect.y+Velocity
            
    "Fill Screen to Cover extra images of sprite"
    displayscreen.fill((0, 0, 0))
    
    "Blit Sprite"
    displayscreen.blit(dragon_image, dragon_image_rect)
    
    "Update Display"
    pygame.display.update()

pygame.quit()