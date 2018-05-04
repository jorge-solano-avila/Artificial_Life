import sys
from random import randrange as randomRange
from math import *

import pygame
from pygame.locals import *

from individuals import Individual, Fish, Shark, Food, Badge

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
#clock = pygame.time.Clock()
screen = pygame.display.set_mode( ( 960, 600 ), pygame.RESIZABLE )
pygame.display.set_caption( "Artificial Life" )

fishImage = pygame.image.load( "../Assets/fish.png" ).convert_alpha()
#print( fishImage.get_width(), fishImage.get_height() )
convertedFishImage = pygame.transform.scale( fishImage, ( 100, 60 ) )
sharkImage = pygame.image.load( "../Assets/shark.png" ).convert_alpha()
skin1 = pygame.image.load( "../Assets/skin1.png" ).convert()
skin1 = pygame.transform.scale( skin1, ( int( skin1.get_width() / 4 ), int( skin1.get_height() / 4 ) ) )
skin2 = pygame.image.load( "../Assets/skin2.png" ).convert()
skin2 = pygame.transform.scale( skin2, ( int( skin2.get_width() / 6 ), int( skin2.get_height() / 6 ) ) )
tree1 = pygame.image.load( "../Assets/tree1.png" ).convert_alpha()
tree1 = pygame.transform.scale( tree1, ( int( tree1.get_width() / 2 ), int( tree1.get_height() / 2 ) ) )
tree2 = pygame.image.load( "../Assets/tree2.png" ).convert_alpha()
tree2 = pygame.transform.scale( tree2, ( int( tree2.get_width() / 2 ), int( tree2.get_height() / 2 ) ) )
tree3 = pygame.image.load( "../Assets/tree3.png" ).convert_alpha()
tree3 = pygame.transform.scale( tree3, ( int( tree3.get_width() / 2 ), int( tree3.get_height() / 2 ) ) )

background = pygame.image.load( "../Assets/background.jpg" ).convert()
screen.blit( background, ( 0, 0 ) )

treeTotal = 10
fishTotal = 50
sharkTotal = 3
foodTotal = 100
fishList = []
skinList = []
sharkList = []
food = pygame.sprite.RenderPlain()
#badges = pygame.sprite.RenderPlain()
font = pygame.font.SysFont( "Arial", 20, True )

treeRules = ["F-[[X]+X]+F[+FX]-X", "FF"]

for index in range( fishTotal ):
	#fishList.append( Fish( 1, index + 1, fishImage ) )
	if index % 2 == 0:
		fish = Fish( 1, index + 1, fishImage )
		skin = Individual( 0, 0, skin1 )
	else:
		fish = Fish( 2, index + 1, convertedFishImage )
		skin = Individual( 0, 0, skin2 )
	fishList.append( fish )
	skinList.append( skin )
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

def drawTree( width, height ):
	rule = getCompleteRule( 5 )
	position = ( randomRange( height ), height )
	unit = 6
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
			test1 = pygame.draw.line( screen, color, position, ( position[0] + dx, position[1] + dy ) )
			test2 = pygame.display.update( ( position[0] - 1, position[1] - 1, position[0] + dx + 1, position[1] + dy + 1 ) )

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
			initialAngle = angles.pop()

	return test1

#tree = drawTree( width, height )
#print( tree.center )

treeImages = [tree1, tree3]
trees = []
for i in range( treeTotal ):
	trees.append( treeImages[randomRange( len( treeImages ) )] )

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

	#msElapsed = clock.tick(120)
	#drawTree( width, height )

	screen.blit( background, ( 0, 0 ) )
	food.draw( screen )
	#badges.empty()
	for i in range( len( fishList ) ):
		fish = fishList[i]
		screen.blit( background, fish.position, fish.position )
		#screen.blit( background, fish.position, fish.position )
	for shark in sharkList:
		screen.blit( background, shark.position, shark.position )

	for shark in sharkList:
		shark.move( fishList )
		screen.blit( shark.image, shark.position )
	for i in range( len( fishList ) ):
		fish = fishList[i]
		skin = skinList[i]
		fish.move( fishList, sharkList, food )
		if fish.energy > 0:
			screen.blit( fish.image, fish.position )
			screen.blit( skin.image, fish.position.center )
			#badges.add( Badge( fish.position.centerx, fish.position.centery ) )
			screen.blit( font.render( str( fish.energy ), True, ( 0, 0, 0 ) ), fish.position )
	#badges.draw( screen )
	for i in range( treeTotal ):
		tree = trees[i]
		screen.blit( tree, ( int( ( i + 1 ) * width / treeTotal ), height - tree.get_height() ) )

	pygame.display.update()