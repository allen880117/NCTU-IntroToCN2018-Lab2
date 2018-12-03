#!/usr/bin/python                                                                            
                                                                                             
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
'''
Remember to import the following module first!
'''
#from mininet.util import dumpNodeConnections
from mininet.cli  import CLI

'''
MyOwnSwitchTopo
modified it to generate 9 switches and 6 hosts
and link them as topo1.png
'''
class MyOwnSwitchTopo(Topo):
	def build(self):
		# Add 9 switches to a topology
		switch = []
		for num in range(10): #0~9
			if( num == 0 ):
				switch.append( 'NULL' )
			else:
				switch.append( self.addSwitch('s%s' % num ) )
		
		# Add 6 hosts to a topology
		host = []
		for h in range(7): #0~6
			if( h == 0 ):
				host.append( 'NULL' )
			else:
				host.append( self.addHost('h%s' % h) )

		# Add links to a topology
		self.addLink( host[1], switch[1], bw = 12, delay = '6ms', loss = 2)
		self.addLink( switch[1], switch[8], bw = 20, delay = '7ms', loss = 15)
		self.addLink( switch[6], host[2], bw = 18, delay = '2ms', loss = 3)
		self.addLink( switch[4], host[5], bw = 14, delay = '5ms', loss = 2)
		self.addLink( switch[8], switch[4], bw = 23, delay = '6ms', loss = 10)
		self.addLink( switch[8], switch[2], bw = 25, delay = '6ms', loss = 14)
		self.addLink( switch[8], switch[6], bw = 30, delay = '1ms', loss = 12)
		self.addLink( switch[2], switch[9], bw = 30, delay = '3ms', loss = 18)
		self.addLink( switch[9], switch[7], bw = 33, delay = '8ms', loss = 10)
		self.addLink( switch[5], host[6], bw = 15, delay = '4ms', loss = 3)
		self.addLink( switch[9], switch[5], bw = 30, delay = '3ms', loss = 20)
		self.addLink( switch[3], switch[9], bw = 35, delay = '2ms', loss = 17)
		self.addLink( switch[7], host[3], bw = 18, delay = '6ms', loss = 6)
		self.addLink( host[4], switch[3], bw = 13, delay = '3ms', loss = 5)

'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 6 hosts and 9 swithces //topo1.png
    topo = MyOwnSwitchTopo()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()

	# Dump every hosts' and switches' connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)

	# Add the following code and do NOT use net.stop()
    CLI(net)
    # Stop a network
    # net.stop()

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
    simpleTest()
