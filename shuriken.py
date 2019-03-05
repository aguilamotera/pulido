
class Shuriken():
	""" Shuriken is the main object of the game """

	def __init__(self):
		self.x = SHURIKEN_INITIAL_X
		self.y = SHURIKEN_INITIAL_Y
		self.xdirection = 0
		self.ydirection = 0
		self.movement = 'UPWARDS'

	def move(self,x,y):
		"""Recieves the amount of pixels to move in absolute value"""
		self.x += (x * self.xdirection)
		self.y += (y * self.ydirection)
	
	def __str__(self):
		return 'SHURIKEN : X: {}, Y: {}, DIRECTION X: {}, DIRECTION Y {}, MOVEMENT {}'.format(self.x, self.y, self.xdirection, self.ydirection, self.movement)
