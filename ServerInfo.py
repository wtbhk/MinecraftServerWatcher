import redis

class ServerInfo:
	def __init__(*args, self):
		self.fields = {
			'addr' : '',
			'port' : '',
			'name' : '',
			'online' : '',
			'max' : '',
			'available' : ''
		}
		if isinstance(args[0], dict):
			self.setFields(args[0])
			return
		if len(args) == 1:
			if strspn(args[0],':'):
				port = int(addr.split(':')[1])
				addr = addr.split(':')[0]
			else:
				addr = args[0]
				port = 25565
		elif len(args) == 2:
			addr = args[0]
			port = int(args[1])
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
		r.sadd('ServerList', redis_key)
	def toDict(self):
		return self.fields