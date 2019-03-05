
class Drawer():

	def __init__(self,canvas):
		"""Holds the canvas to make the drawings in the game loop"""
		self.gameMap = canvas
		self.image = PhotoImage(file='/home/pulid0/100CodingChallenge/RunBladeRun/shuriken.gif')
	
	def move(self,drawing, tag, x, y):
		""" Draws the corresponding move then updates the canvas. Recieves a tag to recognice the object to move """
		self.gameMap.move(tag, (x * drawing.xdirection), (y * drawing.ydirection))
		self.gameMap.update()

	def drawWalls(self):
		self.gameMap.create_rectangle(BORDER_LEFT, BORDER_BOTTOM, WALL_LEFT, WALL_TOP, fill="black", tag="leftWall")
		self.gameMap.create_rectangle(WALL_RIGHT, WALL_BOTTOM, BORDER_RIGHT, BORDER_TOP, fill="black", tag='rightWall')
		self.gameMap.update()
	
	def drawShuriken(self):
		self.gameMap.create_image(SHURIKEN_INITIAL_X,SHURIKEN_INITIAL_Y, image=self.image, tag='shuriken')
		self.gameMap.update()
	
	def drawObstacle(self):
		self.gameMap.create_rectangle(OBSTACLE_INITIAL_X-5, OBSTACLE_INITIAL_Y-20, OBSTACLE_INITIAL_X+5, OBSTACLE_INITIAL_Y+20, fill="blue", tag="obstacle")
