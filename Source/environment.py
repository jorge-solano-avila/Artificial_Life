import sys
from random import randrange as randomRange
from math import *

import pygame
from pygame.locals import *

from individuals import Fish, Shark, Food, Badge

def getCompleteRule( iterations ):
	rules = ["X"]

	for i in range( iterations ):
		j = 0
		while j < len( rules ):
			if rules[j] == "X":
				rules.pop( j )
				for item in treeRules[0][::-1]:
					rules.insert( j, item )
				j += len( treeRules[0] ) - 1
			elif rules[j] == "F":
				rules.pop( j )
				for item in treeRules[1][::-1]:
					rules.insert( j, item )
				j += len( treeRules[1] ) - 1
			j += 1

	return rules

pygame.init()
screen = pygame.display.set_mode( ( 960, 600 ), pygame.RESIZABLE )
pygame.display.set_caption( "Artificial Life" )

fishImage = pygame.image.load( "../Assets/fish.png" ).convert_alpha()
#print( fishImage.get_width(), fishImage.get_height() )
convertedFishImage = pygame.transform.scale( fishImage, ( 100, 60 ) )
sharkImage = pygame.image.load( "../Assets/shark.png" ).convert_alpha()

background = pygame.image.load( "../Assets/background.jpg" ).convert()
screen.blit( background, ( 0, 0 ) )

treeTotal = 10
fishTotal = 50
sharkTotal = 3
foodTotal = 100
fishList = []
sharkList = []
food = pygame.sprite.RenderPlain()
#badges = pygame.sprite.RenderPlain()
font = pygame.font.SysFont( "Arial", 20, True )

treeRules = ["F-[[X]+X]+F[+FX]-X", "FF"]

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

	"""rule = getCompleteRule( 5 )
	position = ( randomRange( height ), height )
	unit = 2.25
	initialAngle = -90
	angle = 20
	angles = []
	positions = []
	for letter in rule:
		if letter == "F":
			dx = cos( radians( initialAngle ) ) * unit
			dy = sin( radians( initialAngle ) ) * unit

			initialAngleAbs = abs( initialAngle )
			color = ( 255, 0, 0 )
			pygame.draw.line( screen, color, position, ( position[0] + dx, position[1] + dy ) )
			pygame.display.update( ( position[0] - 1, position[1] - 1, position[0] + dx + 1, position[1] + dy + 1 ) )

			position = ( position[0] + dx, position[1] + dy )
		elif letter == "+":
			initialAngle += angle
		elif letter == "-":
			initialAngle -= angle
		elif letter == "[":
			positions.append( position )
			angles.append( initialAngle )
		elif letter == "]":
			position = positions.pop()
			initialAngle = angles.pop()"""

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