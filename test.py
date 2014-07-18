from FetchLoop import FetchLoop
from ServerInfo import ServerInfo

server = ServerInfo('202.101.208.35:25565')
server2 = ServerInfo('202.101.208.35:25566')
server.save()
server2.save()

fetchLoop = FetchLoop()
fetchLoop.startLoop()
