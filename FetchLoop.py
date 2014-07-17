from FetchQueen import FetchQueen
from ServerInfo import ServerInfo
from ServerStatus import ServerStatus
import redis
import threading
import time

class FetchLoop:
	def __init__(self):
		r = redis.Redis()
		self.delay = 30	#minutes
	def setDelay(delay, self):
		self.delay = delay
	def startLoop(self):
		fetchThread = DoFetch()
		fetchThread.start()

class DoFetch(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
	def run(self):
		fetchQueen = FetchQueen()
		while True:
			server = fetchQueen.blpop()
			server = ServerStatus(server.info()['addr'], server.info()['port']).get()
			server.save()


def putServersIntoQueen():
	r = redis.Redis()
	#TODO