from random import randrange as randomRange

import pygame

class Individual:
	def __init__( self, image ):
		self.image = image
		self.x = 1
		self.y = 1

		height = pygame.display.Info().current_h
		width = pygame.display.Info().current_w

		self.position = self.image.get_rect().move( randomRange( width ), randomRange( height ) )

	def move( self ):
		height = pygame.display.Info().current_h
		width = pygame.display.Info().current_w

		if self.position.left < 0:
			self.x = 1
		elif self.position.right > width:
			self.x = -1

		if self.position.bottom < height / 2:
			self.y = 1
		elif self.position.top > height:
			self.y = -1

		self.position = self.position.move( self.x, self.y )