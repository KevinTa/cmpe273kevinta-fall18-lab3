from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class SendMessage(DatagramProtocol):

    def __init__(self, host, port):
       self.host = host
       self.port = port

    def startProtocol(self):
        self.transport.connect(self.host, self.port)
        self.transport.write(b"Hello World")

    def datagramReceived(self, data, host_port):
        (host, port) = host_port
        print("{} from {}:{}".format(data, host, port))

    def connectionRefused(self):
        print("No one listening")

reactor.listenUDP(80, SendMessage('127.0.0.1', 1234)) 
reactor.run() 