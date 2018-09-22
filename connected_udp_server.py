from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class ReceiveMessage(DatagramProtocol):

    def __init__(self, host, port):
       self.host = host
       self.port = port

    def startProtocol(self):
        self.transport.connect(self.host, self.port)

    def datagramReceived(self, data, host_port):
        (host, port) = host_port
        print("received {} from {}:{}".format(data, host, port))

    def connectionRefused(self):
        print("No one listening")

reactor.listenUDP(1234, ReceiveMessage('127.0.0.1', 80)) 
reactor.run() 