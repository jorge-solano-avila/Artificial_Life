import sys
from random import randrange as randomRange

import pygame
from pygame.locals import *

from individuals import Flock, Individual

FISH = 50

pygame.init()
screen = pygame.display.set_mode( ( 960, 600 ), pygame.RESIZABLE )
pygame.display.set_caption( "Artificial Life Project" )

backgroundImage = pygame.image.load( "../Assets/background.jpg" ).convert()
screen.blit( backgroundImage, ( 0, 0 ) )

fishImage = pygame.image.load( "../Assets/fish.png" ).convert_alpha()
#fishImage = pygame.transform.scale( fishImage, ( 100, 60 ) )

height = pygame.display.Info().current_h
width = pygame.display.Info().current_w

flock = Flock()
for i in range( FISH ):
	flock.addBoid( Individual( 0, i, fishImage, randomRange( width ), randomRange( height ) ) )

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode( ( event.w, event.h ), pygame.RESIZABLE )
			height = pygame.display.Info().current_h
			width = pygame.display.Info().current_w

	screen.blit( backgroundImage, ( 0, 0 ) )

	flock.run(
		screen = screen,
		height = height,
		width = width
	)

	pygame.display.update()
	pygame.time.delay( 10 )