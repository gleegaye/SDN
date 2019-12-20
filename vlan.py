#!/usr/bin/env python
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.link import Link,TCLink,Intf
from mininet.net import Mininet
from mininet.node import RemoteController



class Tree( Topo ):
	
	def __init__(self):
		"creating custom topo"

		"initialze topo"
		Topo.__init__( self )

		#Add hosts 
		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		h3 = self.addHost( 'h3' )
		h4 = self.addHost( 'h4' )
		h5 = self.addHost( 'h5' )

	
		#Add switches 
		s1 = self.addSwitch( 's1' )
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		s4 = self.addSwitch( 's4' )
		s5 = self.addSwitch( 's5' )
		s6 = self.addSwitch( 's6' )
		s7 = self.addSwitch( 's7' )
		s8 = self.addSwitch( 's8' )
		s9 = self.addSwitch( 's9' )
		s10 = self.addSwitch( 's10' )

		#Add link for s1
		self.addLink( s1, s3 )
		self.addLink( s1, s4 )
		self.addLink( s1, s5 )
		self.addLink( s1, s6 )

		#Add link for s2
		self.addLink( s2, s3 )
		self.addLink( s2, s4 )
		self.addLink( s2, s5 )
		self.addLink( s2, s6 )
		
		#Add link for s3
		self.addLink( s3, s7 )
		self.addLink( s3, s8 )
	
		#Add link for s4
		self.addLink( s4, s7 )
		self.addLink( s4, s8 )

		#Add link for s5
		self.addLink( s5, s9 )
		self.addLink( s5, s10 )

		#Add link for s6
		self.addLink( s6, s9 )
		self.addLink( s6, s10 )

		#Add link for s7
		self.addLink( h1, s7 )
		self.addLink( h2, s7 )

		#Add link for s8
		self.addLink( h3, s8 )

		#Add link for s9
		self.addLink( h4, s9 )

		#Add link for s10
		self.addLink( h5, s10 )


class VLANHost( Host ):
    "Host connected to VLAN interface"

    def config( self, vlan=100, **params ):
        """Configure VLANHost according to (optional) parameters:
           vlan: VLAN ID for default interface"""

        r = super( VLANHost, self ).config( **params )

        intf = self.defaultIntf()
        # remove IP from default, "physical" interface
        self.cmd( 'ifconfig %s inet 0' % intf )
        # create VLAN interface
        self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
        # assign the host's IP to the VLAN interface
        self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
        # update the intf name and host's intf map
        newName = '%s.%d' % ( intf, vlan )
        # update the (Mininet) interface to refer to VLAN interface name
        intf.name = newName
        # add VLAN interface to host's name to intf map
        self.nameToIntf[ newName ] = intf

        return r

hosts = { 'vlan': VLANHost }

class VLANStarTopo( Topo ):
    """Example topology that uses host in multiple VLANs
       The topology has a single switch. There are k VLANs with
       n hosts in each, all connected to the single switch. There
       are also n hosts that are not in any VLAN, also connected to
       the switch."""

    def build( self, k=2, n=2, vlanBase=100 ):
        s1 = self.addSwitch( 's1' )
        for i in range( k ):
            vlan = vlanBase + i
            for j in range(n):
                name = 'h%d-%d' % ( j+1, vlan )
                h = self.addHost( name, cls=VLANHost, vlan=vlan )
                self.addLink( h, s1 )
        for j in range( n ):
            h = self.addHost( 'h%d' % (j+1) )
            self.addLink( h, s1 )


def exampleCustomTags():
    """Simple example that exercises VLANStarTopo"""

    net = Mininet( topo=VLANStarTopo() )
    net.start()
    CLI( net )
    net.stop()
