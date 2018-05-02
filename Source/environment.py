import sys
from random import randrange as randomRange

import pygame
from pygame.locals import *

from individuals import Fish, Shark, Food, Badge

pygame.init()
screen = pygame.display.set_mode( ( 960, 600 ), pygame.RESIZABLE )
pygame.display.set_caption( "Artificial Life" )

fishImage = pygame.image.load( "../Assets/fish.png" ).convert_alpha()
#print( fishImage.get_width(), fishImage.get_height() )
convertedFishImage = pygame.transform.scale( fishImage, ( 100, 60 ) )
sharkImage = pygame.image.load( "../Assets/shark.png" ).convert_alpha()

background = pygame.image.load( "../Assets/background.jpg" ).convert()
screen.blit( background, ( 0, 0 ) )

fishTotal = 50
sharkTotal = 3
foodTotal = 100
fishList = []
sharkList = []
food = pygame.sprite.RenderPlain()
#badges = pygame.sprite.RenderPlain()
font = pygame.font.SysFont( "Arial", 20, True )

for index in range( fishTotal ):
	#fishList.append( Fish( 1, index + 1, fishImage ) )
	if index % 2 == 0:
		fish = Fish( 1, index + 1, fishImage )
	else:
		fish = Fish( 2, index + 1, convertedFishImage )
	fishList.append( fish )
	#badges.add( Badge( fish.x, fish.y ) )

for index in range( sharkTotal ):
	sharkList.append( Shark( 3, index + 1, sharkImage ) )

height = pygame.display.Info().current_h
width = pygame.display.Info().current_w
for index in range( foodTotal ):
	food.add( Food( randomRange( width ), randomRange( 3 * height / 4, height ) ) )
screen.blit( background, ( 0, 0 ) )
food.draw( screen )
#badges.draw( screen )

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode( ( event.w, event.h ), pygame.RESIZABLE )
			food.empty()
			height = pygame.display.Info().current_h
			width = pygame.display.Info().current_w
			for index in range( foodTotal ):
				food.add( Food( randomRange( width ), randomRange( 3 * height / 4, height ) ) )

	screen.blit( background, ( 0, 0 ) )
	food.draw( screen )
	#badges.empty()
	for fish in fishList:
		screen.blit( background, fish.position, fish.position )
	for shark in sharkList:
		screen.blit( background, shark.position, shark.position )

	for shark in sharkList:
		shark.move( fishList )
		screen.blit( shark.image, shark.position )
	for fish in fishList:
		fish.move( fishList, sharkList, food )
		if fish.energy > 0:
			screen.blit( fish.image, fish.position )
			#badges.add( Badge( fish.position.centerx, fish.position.centery ) )
			screen.blit( font.render( str( fish.energy ), True, ( 0, 0, 0 ) ), fish.position )
	#badges.draw( screen )

	pygame.display.update()