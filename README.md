# PyGame
### An exploration of PyGame
#### Overview
PyGame is a set of Python modules created for designing 2D video games. It has a large SDL(Simple DirectMedia Layer) that includes computer graphics and audio resources. In this project, I began with learning about the basic structure of any game and was ultimately able to create video games via PyGame.

#### Basic Game Structure with PyGame
1) Import PyGame
~~~python
import pygame
~~~
2 Initiate Game
~~~python
pygame.init()
~~~
3) Set Display
~~~python
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Celestial Games")
~~~
4) Set Game Values
~~~python
FPS = 70 #FreqPerSec
clock = pygame.time.Clock()

PLAYER_LIFEPOINTS = 5
PLAYER_VELOCITY = 10
OG_SCORE = 0
COIN_VELOCITY = 10
COIN_ACCELERATION = 0.5
BUFFER_DISTANCE = 100
score = 0
player_lifepoints = PLAYER_LIFEPOINTS
coin_velocity = COIN_VELOCITY
~~~
5) Set Game Settings(Audio, images, font)
~~~python
#Font
font = pygame.font.SysFont("centurygothic", 32) #(name: _FileArg | None, size: int)
#Text
text = font.render("I am text", True, (255, 255, 255)) #(text: str | bytes, antialias: bool, color: _ColorValue, background: _ColorValue | None = None)
~~~
7) Main Game Loop
~~~python
~~~
11) End Game
#### Resources
* https://www.fontspace.com/commercial-fonts
* https://iconarchive.com/
* https://redketchup.io/color-picker
* https://www.leshylabs.com/apps/sfMaker/
* https://www.gameart2d.com/freebies.html
* https://opengameart.org/
