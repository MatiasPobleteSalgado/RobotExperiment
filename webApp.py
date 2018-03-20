from flask import Flask, render_template as render, request
from flask_socketio import SocketIO
from sys import stderr

class WebApp(Flask):
	def __init__(self, name):
		Flask.__init__(self, name, static_url_path = '/static')
		self.__setRoutes()

	def __setRoutes(self):
		#- Regular HTTP calls
		self.add_url_rule("/"       , "index"  , self.__index)
		self.add_url_rule("/home"   , "home"   , self.__index)
		self.register_error_handler(404, self.__notFound)

	def __index(self):
		return render("index.html")

	def __notFound(self, error):
		return render("404.html")