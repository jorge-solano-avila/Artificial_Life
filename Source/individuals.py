from random import randrange as randomRange
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *
from pygame.color import *

SPEED = 1
EAT = 10
DIE = 10000

class Individual:
	def __init__( self, type, id, image ):
		self.type = type
		self.id = id
		self.image = image
		self.x = SPEED
		self.y = SPEED
		self.energy = 100

		height = pygame.display.Info().current_h
		width = pygame.display.Info().current_w

		self.position = self.image.get_rect().move( randomRange( width ), randomRange( height ) )

	def near( self, individual ):
		x = abs( individual.position.centerx - self.position.centerx )
		y = abs( individual.position.centery - self.position.centery )

		distance = math.sqrt( math.pow( x, 2 ) + math.pow( y, 2 ) )

		return distance <= 100

	def nearObject( self, position ):
		x = abs( position[0] - self.position.centerx )
		y = abs( position[1] - self.position.centery )

		distance = math.sqrt( math.pow( x, 2 ) + math.pow( y, 2 ) )

		return distance <= 100

	def movement( self, target ):
		x = 0
		y = 0

		if target.position.centerx > self.position.centerx:
			x = SPEED * 2
		elif target.position.centerx < self.position.centerx:
			x = -SPEED * 2

		if target.position.centery > self.position.centery:
			y = SPEED * 2
		elif target.position.centery < self.position.centery:
			y = -SPEED * 2

		return ( x, y )

	"""def movement( self, position ):
		x = 0
		y = 0

		if position[0] > self.position.centerx:
			x = 2
		elif position[0] < self.position.centerx:
			x = -2

		if position[1] > self.position.centery:
			y = 2
		elif position[1] < self.position.centery:
			y = -2

		return ( x, y )"""

class Fish( Individual ):
	def move( self, fishList, sharkList, food ):
		height = pygame.display.Info().current_h
		width = pygame.display.Info().current_w

		"""nearFish = []
		for fish in fishList:
			if self.id != fish.id and self.type == fish.type:
				near = self.near( fish )
				if near:
					nearFish.append( fish )

		countNearFish = len( nearFish )
		if countNearFish > 0:
			averageX = 0
			averageY = 0
			for index in range( countNearFish ):
				averageX += nearFish[index].position.centerx
				averageY += nearFish[index].position.centery
			averageX /= countNearFish
			averageY /= countNearFish

			self.x, self.y = self.movement( ( averageX, averageY ) )"""

		nearShark = None
		for shark in sharkList:
			near = self.near( shark )
			if near:
				nearShark = shark
				break

		if near:
			self.x, self.y = self.movement( nearShark )
			self.x *= -1
			self.y *= -1

		for sprite in food:
			near = self.nearObject( ( sprite.rect.centerx, sprite.rect.centery ) )
			if near:
				self.energy += EAT

		if self.position.left < 0:
			self.x = SPEED
		elif self.position.right > width:
			self.x = -SPEED

		if self.position.bottom < height / 2:
			self.y = SPEED
		elif self.position.top > height:
			self.y = -SPEED

		self.position = self.position.move( self.x, self.y )

class Shark( Individual ):
	def move( self, fishList ):
		height = pygame.display.Info().current_h
		width = pygame.display.Info().current_w

		for fish in fishList:
			near = self.near( fish )
			if near:
				fish.energy -= DIE

		if self.position.left < 0:
			self.x = 1
		elif self.position.right > width:
			self.x = -1

		if self.position.bottom < 0:
			self.y = 1
		elif self.position.top > height:
			self.y = -1

		self.position = self.position.move( self.x, self.y )

class Food( pygame.sprite.Sprite ):
	def __init__( self, x, y ):
		pygame.sprite.Sprite.__init__( self )
		self.x = x
		self.y = y
		self.color = "red"
		self.width = 10
		self.height = 10
		self.image = self.draw()
		self.rect = Rect( x, y, self.width, self.height )

	def draw( self ):
		screen = pygame.Surface( ( self.width, self.height ) )
		screen.set_colorkey( ( 0, 0, 0 ) )
		pygame.gfxdraw.filled_circle( screen, int( self.width / 2 ), int( self.height / 2 ), int( self.height / 2 - 1 ), THECOLORS[self.color] )

		return screen

class Badge( pygame.sprite.Sprite ):
	def __init__( self, x, y ):
		pygame.sprite.Sprite.__init__( self )
		self.x = x
		self.y = y
		self.color = "yellow"
		self.width = 30
		self.height = 30
		self.image = self.draw()
		self.rect = Rect( x, y, self.width, self.height )

	def draw( self ):
		screen = pygame.Surface( ( self.width, self.height ) )
		screen.set_colorkey( ( 0, 0, 0 ) )
		pygame.gfxdraw.filled_circle( screen, int( self.width / 2 ), int( self.height / 2 ), int( self.height / 2 - 1 ), THECOLORS[self.color] )

		return screen