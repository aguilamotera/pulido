
from imports import Frame, Tk, config, Shuriken, Obstacle

class RunBladeRun(Frame):

	def __init__(self, master=None):
		
		 Frame.__init__(self, master)
		 self.pack()

		 self.shuriken = Shuriken()
		 self.obstacle = Obstacle()

		# self.canvas = Canvas(self, width=WIDTH, height=HEIGHT,  background="white")
		# self.eventListener = EventListener()
		# self.eventListener.start()
		# self.bind("<Left>", lambda e: eventHandler(self.eventListener,'left'))
		# self.bind("<Right>", lambda e: eventHandler(self.eventListener,'right'))
		
		# self.canvas.pack()
		# self.focus()

		# setupGame(self.canvas)


if __name__ == '__main__':
	app = RunBladeRun()
	#app.mainloop()