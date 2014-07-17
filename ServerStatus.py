import socket
from ServerInfo import ServerInfo

class ServerStatus:
	def __init__(host='127.0.0.1', port=25565, self):
		self.host = host
		self.port = int(port)
		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connect()

	def connect(self):
		s = self.s
		try:
			s.connect((HOST,PORT))
		except:
			self.connected = False
			return False
		self.connected = True
		return True

	def get(self):
		if self.connected :
			s = self.s
			s.sendall("\xfe")
			data = s.recv(2048)
			data = data[2:].replace('\x00','').split('\xa7')
			data_ = {
				'addr' : self.host,
				'port' : self.port,
				'name' : data[0],
				'online' : data[1],
				'max' : data[2],
				'available' : True
				}
			return ServerInfo(data_)
		else :
			return ServerInfo({
					'addr' : self.host,
					'port' : self.port,
					'available' : False
				})

	def __del__(self):
		self.s.close()