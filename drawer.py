from imports import PhotoImage, config

class Drawer():

	def __init__(self,canvas):
		"""Holds the canvas to make the drawings in the game loop"""
		self.gameMap = canvas
		#self.image = PhotoImage(file='/home/pulid0/100CodingChallenge/RunBladeRun/shuriken.gif')
		self.image = PhotoImage(file='shuriken.gif')
	
	def move(self,drawing, tag, x, y):
		""" Draws the corresponding move then updates the canvas. Recieves a tag to recognice the object to move """
		self.gameMap.move(tag, (x * drawing.xdirection), (y * drawing.ydirection))
		self.gameMap.update()

	def drawWalls(self):
		self.gameMap.create_rectangle(config.BORDER_LEFT, config.BORDER_BOTTOM, config.WALL_LEFT, config.WALL_TOP, fill="black", tag="leftWall")
		self.gameMap.create_rectangle(config.WALL_RIGHT, config.WALL_BOTTOM, config.BORDER_RIGHT, config.BORDER_TOP, fill="black", tag='rightWall')
		self.gameMap.update()
	
	def drawShuriken(self):
		self.gameMap.create_image(config.SHURIKEN_INITIAL_X,config.SHURIKEN_INITIAL_Y, image=self.image, tag='shuriken')
		self.gameMap.update()
	
	def drawObstacle(self):
		self.gameMap.create_rectangle(config.OBSTACLE_INITIAL_X-5, config.OBSTACLE_INITIAL_Y-20, config.OBSTACLE_INITIAL_X+5, config.OBSTACLE_INITIAL_Y+20, fill="blue", tag="obstacle")
