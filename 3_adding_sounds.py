import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption("Sound Effects")

"LOAD Sound"
sound_1 = pygame.mixer.Sound('sound_1.wav')
sound_2 = pygame.mixer.Sound('sound_2.wav')

"PLAY Sound"
for i in range(10):
    sound_1.play()
    pygame.time.delay(500) #1sec = 1000msec


sound_2.play()
pygame.time.delay(2000) #1sec = 1000msec

"Volume Control"
sound_2.set_volume(0.2)
sound_2.play()

"LOAD Background Music"
pygame.mixer.music.load('music.wav')

"Play ＆　ｓｔｏｐ BGMUSIC"
pygame.mixer.music.play(-1, 0.0)
pygame.time.delay(1000)
sound_2.play()
pygame.time.delay(5000)
pygame.mixer.music.stop()

"Main Loop"
running = True #設定遊戲狀態:持續(為真)
while running: 
    for event in pygame.event.get():#screen detect any if event is happening
        #print(event)
        if event.type==pygame.QUIT: 
            running = False
    
    pygame.display.update()





pygame.quit()