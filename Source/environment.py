import sys
from random import randrange as randomRange

import pygame
from pygame.locals import *

from individuals import Flock, SharkSet, TreeSet, FoodSet, Individual

FISH_1 = 20
FISH_2 = 30
SHARKS = 5
TREES = 10

pygame.init()
screen = pygame.display.set_mode( ( 960, 600 ), pygame.RESIZABLE )
pygame.display.set_caption( "Artificial Life Project" )

arialFont = pygame.font.SysFont( "Arial", 20, True )

backgroundImage = pygame.image.load( "../Assets/background.jpg" ).convert()
screen.blit( backgroundImage, ( 0, 0 ) )

fishImage = pygame.image.load( "../Assets/fish.png" ).convert_alpha()
fishImageSmall = pygame.transform.scale( fishImage, ( 100, 60 ) )
sharkImage = pygame.image.load( "../Assets/shark.png" ).convert_alpha()
tree1Image = pygame.image.load( "../Assets/tree1.png" ).convert_alpha()
tree1Image = pygame.transform.scale( tree1Image, ( int( tree1Image.get_width() / 2 ), int( tree1Image.get_height() / 2 ) ) )
tree2Image = pygame.image.load( "../Assets/tree2.png" ).convert_alpha()
tree2Image = pygame.transform.scale( tree2Image, ( int( tree2Image.get_width() / 2 ), int( tree2Image.get_height() / 2 ) ) )
tree3Image = pygame.image.load( "../Assets/tree3.png" ).convert_alpha()
tree3Image = pygame.transform.scale( tree3Image, ( int( tree3Image.get_width() / 2 ), int( tree3Image.get_height() / 2 ) ) )

height = pygame.display.Info().current_h
width = pygame.display.Info().current_w

flock1 = Flock()
for i in range( FISH_1 ):
	flock1.addBoid( Individual( 0, i, fishImage, randomRange( width ), randomRange( height ) ) )

flock2 = Flock()
for i in range( FISH_2 ):
	flock2.addBoid( Individual( 1, i, fishImageSmall, randomRange( width ), randomRange( height ) ) )

sharkSet = SharkSet()
for i in range( SHARKS ):
	sharkSet.addShark( Individual( 2, i, sharkImage, randomRange( width ), randomRange( height ) ) )

treeSet = TreeSet()
for i in range( TREES ):
	trees = [tree1Image, tree2Image, tree3Image]
	treeSet.addTree( Individual( 3, i, trees[randomRange( 3 )], randomRange( width ), randomRange( height ) ) )

foodSet = FoodSet()

foodIndex = 0
ungeneratedFood = True
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == pygame.VIDEORESIZE:
			screen = pygame.display.set_mode( ( event.w, event.h ), pygame.RESIZABLE )
			height = pygame.display.Info().current_h
			width = pygame.display.Info().current_w

			treeSet = TreeSet()
			for i in range( TREES ):
				trees = [tree1Image, tree2Image, tree3Image]
				treeSet.addTree( Individual( 3, i, trees[randomRange( 3 )], randomRange( width ), randomRange( height ) ) )

			foodSet.add( trees = treeSet.trees )

	screen.blit( backgroundImage, ( 0, 0 ) )

	flock1.run(
		sharks = sharkSet.sharks,
		screen = screen,
		font = arialFont,
		height = height,
		width = width
	)
	flock2.run(
		sharks = sharkSet.sharks,
		screen = screen,
		font = arialFont,
		height = height,
		width = width
	)
	sharkSet.run(
		boids = flock1.boids + flock2.boids,
		screen = screen,
		height = height,
		width = width
	)
	treeSet.draw( screen = screen )
	foodSet.draw( screen = screen )

	miliseconds = pygame.time.get_ticks()
	if miliseconds >= foodIndex * 30000 and miliseconds <= foodIndex * 30000 + 1000:
		if ungeneratedFood:
			foodSet.add( trees = treeSet.trees )

			ungeneratedFood = False
			foodIndex += 1
	if miliseconds >= ( foodIndex - 1 ) * 30000 + 1000:
		ungeneratedFood = True
	pygame.display.update()
	pygame.time.delay( 10 )