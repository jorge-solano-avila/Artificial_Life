import sys
from random import randrange as randomRange

import pygame
from pygame.locals import *

from individuals import Flock, Individual

FISH_1 = 20
FISH_2 = 30

pygame.init()
screen = pygame.display.set_mode( ( 960, 600 ), pygame.RESIZABLE )
pygame.display.set_caption( "Artificial Life Project" )

backgroundImage = pygame.image.load( "../Assets/background.jpg" ).convert()
screen.blit( backgroundImage, ( 0, 0 ) )

fishImage = pygame.image.load( "../Assets/fish.png" ).convert_alpha()
fishImageSmall = pygame.transform.scale( fishImage, ( 100, 60 ) )

height = pygame.display.Info().current_h
width = pygame.display.Info().current_w

flock1 = Flock()
for i in range( FISH_1 ):
	flock1.addBoid( Individual( 0, i, fishImage, randomRange( width ), randomRange( height ) ) )

flock2 = Flock()
for i in range( FISH_2 ):
	flock2.addBoid( Individual( 1, i, fishImageSmall, randomRange( width ), randomRange( height ) ) )

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode( ( event.w, event.h ), pygame.RESIZABLE )
			height = pygame.display.Info().current_h
			width = pygame.display.Info().current_w

	screen.blit( backgroundImage, ( 0, 0 ) )

	flock1.run(
		screen = screen,
		height = height,
		width = width
	)
	flock2.run(
		screen = screen,
		height = height,
		width = width
	)

	pygame.display.update()
	pygame.time.delay( 10 )