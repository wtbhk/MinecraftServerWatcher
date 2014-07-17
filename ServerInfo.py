import redis

class ServerInfo:
	def __init__(addr, port=25565, self):
		self.fields = {
			'addr' : '',
			'port' : '',
			'name' : '',
			'online' : '',
			'max' : '',
			'available' : ''
		}
		if isinstance(addr, dict):
			self.setFields(addr)
		else:
			self.fields['addr'] = addr
			self.fields['port'] = port

	def setFields(fields, self):
		for i in fields:
			if i in self.fields:
				self.fields[i] = fields[i]
	def info(self):
		return self.fields
	def available(self):
		return self.fields['available']
	def save(self):
		redis_key = self.fields['addr'] + ':' + self.fields['port']
		r = redis.Redis()
		r.hmset(redis_key, self.fields)
	def toDict(self):
		return self.fields