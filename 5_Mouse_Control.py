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
dragon_image_rect.topleft = (400, 0)

"Main Loop"
running = True
while running==True:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            running=False
            
        if event.type==pygame.MOUSEBUTTONDOWN:
            print(event)
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            dragon_image_rect.centerx = mouse_x
            dragon_image_rect.centery = mouse_y

            
    "Fill Screen to Cover extra images of sprite"
    displayscreen.fill((0, 0, 0))
    
    "Blit Sprite"
    displayscreen.blit(dragon_image, dragon_image_rect)
    
    "Update Display"
    pygame.display.update()

pygame.quit()