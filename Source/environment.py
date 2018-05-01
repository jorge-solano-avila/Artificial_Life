import sys
from random import randrange as randomRange

import pygame
from pygame.locals import *

from individuals import Individual

screen = pygame.display.set_mode( ( 960, 600 ), pygame.RESIZABLE )
pygame.display.set_caption( "Artificial Life" )
player = pygame.image.load( "../Assets/fish2.png" ).convert_alpha()
player2 = pygame.transform.scale( player, ( 100, 60 ) )
player3 = pygame.image.load( "../Assets/shark.png" ).convert_alpha()
background = pygame.image.load( "../Assets/background.jpg" ).convert()
screen.blit( background, ( 0, 0 ) )
objects = []
individual = Individual( player )
individual2 = Individual( player2 )
shark = Individual( player3 )

"""
for x in range( 1 ):
	#pygame.transform.scale( player, (200, 100) )
	o = GameObject( player, 1 )
	objects.append( o )
"""
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode( ( event.w, event.h ), pygame.RESIZABLE )
			screen.blit( background, ( 0, 0 ) )

	screen.blit( background, individual.position, individual.position )
	screen.blit( background, individual2.position, individual2.position )
	screen.blit( background, shark.position, shark.position )
	individual.move()
	individual2.move()
	shark.move()
	screen.blit( individual.image, individual.position )
	screen.blit( individual2.image, individual2.position )
	screen.blit( shark.image, shark.position )
	#for o in objects:
	#	screen.blit( background, o.position, o.position )
	#for o in objects:
	#	o.move()
	#	screen.blit( o.image, o.position )
	pygame.display.update()