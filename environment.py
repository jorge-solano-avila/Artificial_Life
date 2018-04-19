import sys
from random import randrange

import pygame
from pygame.locals import *

class GameObject:
	def __init__(self, image, width, speed):
		self.speed = speed
		self.image = image
		self.pos = image.get_rect().move(width, 0)

	def move(self):
		self.pos = self.pos.move(self.speed, 0)
		if self.pos.top > 600:
			self.pos.bottom = 0

	def move2(self):
		self.pos = self.pos.move(0, self.speed)
		if self.pos.top > 600:
			self.pos.bottom = 0

screen = pygame.display.set_mode((1920, 1200))
player = pygame.image.load('Assets/fish2.png').convert_alpha()
background = pygame.image.load('Assets/background.jpg').convert()
screen.blit(background, (0, 0))
objects = []
for x in range(1):
	o = GameObject(pygame.transform.scale( player, (200, 100) ), randrange( 200 ), 1)
	o2 = GameObject(player, randrange( 200 ), 1)
	objects.append(o)
	objects.append(o2)
while 1:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	for o in objects:
		screen.blit(background, o.pos, o.pos)
	i = 0
	for o in objects:
		if i == 0:
			o.move()
		else:
			o.move2()
		screen.blit(o.image, o.pos)
		i += 1
	pygame.display.update()