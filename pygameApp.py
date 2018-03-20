import pygame as pgm
import threading as th

class PygameApp(object):
	def __init__(self, socket):
		self.socket = socket
		self.scr = pgm.display.set_mode((640, 480))
		self.on = True
		self.thread = th.Thread(target = self.loop)

	def draw(self):
		self.scr.fill((255, 255, 255))
		pgm.display.update()

	def update(self):
		for e in pgm.event.get():
			if(e.type == pgm.QUIT):
				self.on = False

			if(e.type == pgm.KEYDOWN):
				if(e.key == pgm.K_ESCAPE):
					self.on = False
				else:
					print("Nani")
					self.socket.send({"msg": e.key})

	def start(self):
		self.thread.start()

	def loop(self):
		while(self.on):
			self.update()
			self.draw()
		pgm.quit()