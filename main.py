#!/usr/bin/python3

from socketApp import SocketApp
from webApp    import WebApp
from pygameApp import PygameApp
from sys import argv
from flask_socketio import SocketIO

class Main(object):
	@staticmethod
	def main(args):
		webApp = WebApp(__name__)
		socketApp = SocketApp(webApp)
		gui = PygameApp(socketApp)
		gui.start()
		socketApp.run(webApp, port=5000, host='0.0.0.0')

if(__name__ == "__main__"):
	Main.main(argv)