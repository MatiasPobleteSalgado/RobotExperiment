from flask import Flask, render_template as render, request
from flask_socketio import SocketIO
from sys import stderr

from webApp import WebApp

class SocketApp(SocketIO):
	def __init__(self, app):
		app.config['SECRET_KEY'] = 'secret!'
		SocketIO.__init__(self, app,  async_mode='threading')
		self.__setRoutes()

	def __setRoutes(self):
		self.on_event("connect", self.sockConnect, namespace = "/sock")
		self.on_event("disconnect", self.sockDisConnect, namespace = "/sock")
		self.on_event("json", self.sockCommand, namespace = "/sock")

	def sockConnect(self):
		print("Client connected", file=stderr)

	def sockDisConnect(self):
		print("Client disconnected", file=stderr)

	def sockCommand(self, data):
		print(data, file = stderr)

	def send(self, msg):
		self.emit("msg", msg, namespace = "/sock", ignore_queue = True)