from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class MulticastServer(DatagramProtocol):

    def startProtocol(self):
        self.transport.setTTL(5)
        self.transport.joinGroup("228.0.0.5")

    def datagramReceived(self, datagram, address):
        print ("Datagram {} received from {}".format(repr(datagram), repr(address)))

reactor.listenMulticast(8005, MulticastServer(),
                        listenMultiple=True)
reactor.run()