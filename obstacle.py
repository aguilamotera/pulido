
class Obstacle():
	""" If shuriken collides with one of this you lose """

	def __init__(self):
		self.x = OBSTACLE_INITIAL_X
		self.y = OBSTACLE_INITIAL_Y
		self.ydirection = 0
		self.movement = None

	def move(self,y):
		"""Recieves the amount of pixels to move in absolute value"""
		self.y += (y * self.ydirection)
	
	def __str__(self):
		return 'OBSTACLE nº1: X: {}, Y: {}, DireccionY: {}, Movement: {}'.format(self.x,self.y,self.ydirection, self.movement)
