import pygame

"1. Initiate Pygame"
pygame.init()

"2. Create Display Surface & Caption"
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Blit Image")

#Basic Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255 )
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
#Personal Colors
SAKURA = (246, 203, 218)
TIFFANY = (10, 186, 181)
GREY_BLUE_D = (75, 117, 143)
CORAL_ORANGE = (247, 135, 99)
SOFT_GREY = (203, 205, 207)


#Create Image & Return screen with the image
dragon_image_l = pygame.image.load("dragon_icon.png")
dragon_image_l_rect = dragon_image_l.get_rect()
dragon_image_l_rect.topleft = (0, 0)

dragon_image_r = pygame.image.load("dragon_icon_r.png")
dragon_image_r_rect = dragon_image_r.get_rect()
dragon_image_r_rect.topright = (WINDOW_WIDTH, 0)

star_image = pygame.image.load("star_icon.png")
star_image_rect = star_image.get_rect()
star_image_rect.center = (WINDOW_WIDTH-550, WINDOW_HEIGHT-100)

star_image_2 = pygame.image.load("star_icon_2.png")
star_image_2_rect = star_image_2.get_rect()
star_image_2_rect.center = (WINDOW_WIDTH-50, WINDOW_HEIGHT-100)

#See All Available Fonts\
fonts = pygame.font.get_fonts()
"""
for i in fonts:
    print(i)
"""    
#Define Font
system_font = pygame.font.SysFont('centurygothic', 64)
custom_font = pygame.font.Font('HelloKetta.ttf', 40)

system_text = system_font.render("Dragon Boat", True, TIFFANY)
system_text_rect = system_text.get_rect()
system_text_rect.center = (300, 150)

custom_text = custom_font.render("Move the Dragons", True, TIFFANY)
custom_text_rect = custom_text.get_rect()
custom_text_rect.center = (300, 250)

"3. Main Loop"
running = True #設定遊戲狀態:持續(為真)
while running: 
    for event in pygame.event.get():#screen detect any if event is happening
        #print(event)
        if event.type==pygame.QUIT: 
            running = False
            
    #Blit a screen obj. to display
    displayscreen.blit(dragon_image_l, dragon_image_l_rect)
    displayscreen.blit(dragon_image_r, dragon_image_r_rect)
    displayscreen.blit(star_image, star_image_rect)
    displayscreen.blit(star_image_2, star_image_2_rect)
    
    #Blit text
    displayscreen.blit(system_text, system_text_rect)
    displayscreen.blit(custom_text, custom_text_rect)
    
    #Draw Line
    pygame.draw.line(displayscreen, WHITE, (0, 75), (WINDOW_WIDTH, 75), 4)
    pygame.display.update()

"4. End Game"
pygame.quit()