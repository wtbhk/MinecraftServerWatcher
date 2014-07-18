from FetchQueen import FetchQueen
from ServerInfo import ServerInfo
from ServerStatus import ServerStatus
import redis
import time
import thread

class FetchLoop:
	def __init__(self):
		r = redis.Redis()
		self.delay = 30	#minutes
	def setDelay(delay, self):
		self.delay = delay
	def startLoop(self):
		thread.start_new_thread(doFetch)
		thread.start_new_thread(putServersIntoQueen, (self.delay))

def doFetch(self):
	fetchQueen = FetchQueen()
	while True:
		server = fetchQueen.blpop()
		server = ServerStatus(server.info()['addr'], server.info()['port']).get()
		server.save()

def putServersIntoQueen(delay):
	while True:
		r = redis.Redis()
		server_list = r.smembers('ServerList')
		for i in server_list:
			fetchQueen = FetchQueen()
			fetchQueen.rpush(ServerInfo(i))
		time.sleep(delay)
