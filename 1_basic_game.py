"""
Purpose: Display Surface & Basic Game Structure
"""
import pygame

#1. Initiate Pygame
pygame.init()#使用pygame工具庫的init()函式

#2. Create Display Sruface & Caption
 
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 400
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) #設定遊戲視窗的物件(object)
pygame.display.set_caption("My First Game")

#Define colors as RGB Tuples(R, G, B)
##Basic Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255 )#(0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
##Personal Colors
SAKURA = (246, 203, 218)
TIFFANY = (10, 186, 181)
CORAL_ORANGE = (247, 135, 99)
SOFT_GREY = (203, 205, 207)

display.fill(SOFT_GREY)

"PyGame Drawing"
#Line(surface, color, startpos, endpos, linethick)
pygame.draw.line(display, SAKURA, (0, 0), (350, 200), 5)
pygame.draw.line(display, TIFFANY, (700, 0), (350, 200), 5)
pygame.draw.line(display, CORAL_ORANGE, (0, 400), (350, 200), 5)
pygame.draw.line(display, GREEN, (700, 400), (350, 200), 5)

#Circle(surface, color, center, radius, linethick) 0=fill
pygame.draw.circle(display, WHITE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 150, 0)
pygame.draw.circle(display, CORAL_ORANGE, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 75, 0)

#Rectangle(surface, color, (topleftx, toplefty, width, height))
pygame.draw.rect(display, BLACK, (500, 0, 100, 150))

#3. Main Game Loop
running = True #設定遊戲狀態:持續(為真)
while running:  #when True ->enter loop ->loop
    for event in pygame.event.get():#screen detect any if event is happening
        #print(event)
        if event.type==pygame.QUIT: #continuous detection of when the game will end(mouse click quit -> pygame.quit())
            running = False
    pygame.display.update() #Screen Update

#4. End Game
pygame.quit()