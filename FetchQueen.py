import redis
from ServerInfo import ServerInfo
import json

class FetchQueen:
	def __init__(self):
		self.r = redis.Redis()
		self.redis_key = 'ServerQueen'
	def lpush(server, self):
		self.r.lpush(json.dumps(server.toDict()))
	def rpush(server, self):
		self.r.rpush(json.dumps(server.toDict()))
	def lpop(self):
		return ServerInfo(json.loads(self.r.lpop(self.redis_key)))
	def blpop(self):
		return ServerInfo(json.loads(self.r.blpop(self.redis_key, 0)))