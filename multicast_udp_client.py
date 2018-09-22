from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastClient(DatagramProtocol):

    def startProtocol(self):
        self.transport.joinGroup("228.0.0.5")
        self.transport.write(b'Hello World', ("228.0.0.5", 8005))

    def datagramReceived(self, datagram, address):
        print ("Datagram {} received from {}".format(repr(datagram), repr(address)))


reactor.listenMulticast(8005, MulticastClient(), listenMultiple=True)
reactor.run()