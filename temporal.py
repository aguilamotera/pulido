import time
from threading import Thread

from tkinter import Canvas
from tkinter import PhotoImage




class EventListener(Thread):

	def __init__(self):
		Thread.__init__(self)
		self.event = None

	def run(self):
		global SHURIKEN_EVENT
		while True:
			if self.event == 'left':
				SHURIKEN_EVENT = 'move_left'

			if self.event == 'right':
				SHURIKEN_EVENT = 'move_right'

			time.sleep(100/1000)
		
			
def eventHandler(eventListener,event):
	print('Event recieved is {}'.format(event))
	if event == 'left':
		eventListener.event = 'left'

		### DEBUG
		#print('Event on EventListener is {}'.format(eventListener.event))
		#print('GLOBAL VARIABLE SHURIKEN EVENT: {}'.format(SHURIKEN_EVENT))
		### DEBUG
	if event == 'right':
		eventListener.event = 'right'

def setupGame(game_map):
	# Init objects required for the game
	shuriken = Shuriken()
	obstacle = Obstacle()
	drawer = Drawer(game_map)

	drawer.drawWalls()
	drawer.drawShuriken()
	drawer.drawObstacle()

	game_loop = Thread(target=GAME_LOOP, args=(shuriken, obstacle, drawer), name='GameLoopThread')
	game_loop.start()

def GAME_LOOP(shuriken, obstacle, drawer, pause=False, ):
	# This is the main game loop:
	# 1-Checks for events
	# 2-Moves corresponding objects -> Also checks collisions
	# 3-Draws them.
	
	while not pause:
		if SHURIKEN_EVENT == 'move_left' and (shuriken.x - SHURIKEN_MOV_X + 10) != WALL_LEFT:
			if shuriken.movement == 'DOWNWARDS':
				moveShuriken_left(shuriken, xdirection=-1, ydirection=1)
				time.sleep(50/1000)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)
			
			if shuriken.movement == 'UPWARDS':
				moveShuriken_left(shuriken)
				time.sleep(50/1000)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)

			### DEBUG
			print(shuriken)
			### DEBUG

		if SHURIKEN_EVENT == 'move_right' and (shuriken.x + SHURIKEN_MOV_X - 10) != WALL_RIGHT:
			if shuriken.movement == 'DOWNWARDS':
				moveShuriken_right(shuriken, xdirection=1, ydirection=1)
				time.sleep(50/1000)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)
			
			if shuriken.movement == 'UPWARDS':
				moveShuriken_right(shuriken)
				time.sleep(50/1000)
				drawer.move(shuriken,'shuriken',SHURIKEN_MOV_X, SHURIKEN_MOV_Y)

			### DEBUG
			print(shuriken)
			### DEBUG
		time.sleep(25/1000)

def checkColision(shuriken, obstacle):
	if (shuriken.x == 270) and (shuriken.y+20 == obstacle.y+60 or shuriken.y+20 == obstacle.y+120 or shuriken.y == obstacle.y+60 or shuriken.y == obstacle.y):
		return True

def moveShuriken_left(shuriken, xdirection=-1, ydirection=-1):
	shuriken.xdirection = xdirection
	shuriken.ydirection = ydirection

	if shuriken.y == WALL_TOP:
		shuriken.movement = 'DOWNWARDS'
	
	if shuriken.y == WALL_BOTTOM:
		shuriken.movement = 'UPWARDS'

	shuriken.move(SHURIKEN_MOV_X, SHURIKEN_MOV_Y)


def moveShuriken_right(shuriken, xdirection=1, ydirection=-1):
	shuriken.xdirection = xdirection
	shuriken.ydirection = ydirection

	if shuriken.y == WALL_TOP:
		shuriken.movement = 'DOWNWARDS'
	
	if shuriken.y == WALL_BOTTOM:
		shuriken.movement = 'UPWARDS'

	shuriken.move(SHURIKEN_MOV_X, SHURIKEN_MOV_Y)
	
"""
def move_obstacle(obstacle):
	
	# DEFAULT OBSTACLE SET UP:
	obstacle.ydirection = 1
	obstacle.movement = 'DOWNWARDS'

	difficulty = 0
	while(True):

		while obstacle.movement == 'DOWNWARDS':
			obstacle.move(20)
			canvas.move("obstacle",0,20)
			checkColision(self.shuriken, self.obstacle)
			time.sleep((333 -  difficulty)/1000)

			###DEBUG
			print(self.obstacle)
			###DEBUG

			if self.obstacle.y == BOTTOM_BORDER-60:
				self.obstacle.movement = 'UPWARDS'
				if difficulty < 325:
					difficulty += 25
				self.obstacle.ydirection = -1

		while self.obstacle.movement == 'UPWARDS':
			self.obstacle.move(20)
			self.canvas.move("obstacle",0,-20)
			checkColision(self.shuriken, self.obstacle)
			time.sleep((333 - difficulty)/1000)

			###DEBUG
			print(self.obstacle)
			###DEBUG

			if self.obstacle.y == TOP_BORDER+40:
				self.obstacle.movement = 'DOWNWARDS'
				if difficulty < 325:
					difficulty += 25
				self.obstacle.ydirection = 1
"""



