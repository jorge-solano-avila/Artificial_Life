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

screen = pygame.display.set_mode((1920, 1200))
player = pygame.image.load('Assets/fish2.png').convert_alpha()
background = pygame.image.load('Assets/background.jpg').convert()
screen.blit(background, (0, 0))
objects = []
for x in range(100):
	o = GameObject(player, randrange( 200 ), 1)
	objects.append(o)
while 1:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	for o in objects:
		screen.blit(background, o.pos, o.pos)
	for o in objects:
		o.move()
		screen.blit(o.image, o.pos)
	pygame.display.update()