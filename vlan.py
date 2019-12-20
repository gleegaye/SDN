#!/usr/bin/env python

from mininet.net import Mininet

from mininet.cli import CLI

from mininet.link import Link,TCLink,Intf

 

if '__main__' == __name__:

  net = Mininet(link=TCLink)

  #Add hosts 
	h1 = net.addHost( 'h1' )
	h2 = net.addHost( 'h2' )
	h3 = net.addHost( 'h3' )
	h4 = net.addHost( 'h4' )
	h5 = net.addHost( 'h5' )

  #h5 is a switch

  #Add switches 
	s1 = net.addHost( 's1' )
	s2 = net.addHost( 's2' )
	s3 = net.addHost( 's3' )
	s4 = net.addHost( 's4' )
	s5 = net.addHost( 's5' )
	s6 = net.addHost( 's6' )
	s7 = net.addHost( 's7' )
	s8 = net.addHost( 's8' )
	s9 = net.addHost( 's9' )
	s10 = net.addHost( 's10' )
  
  #Add link for s1
	Link( s1, s3 )
	Link( s1, s4 )
	Link( s1, s5 )
	Link( s1, s6 )

	#Add link for s2
	Link( s2, s3 )
	Link( s2, s4 )
	Link( s2, s5 )
	Link( s2, s6 )
	
	#Add link for s3
	Link( s3, s7 )
	Link( s3, s8 )

	#Add link for s4
	Link( s4, s7 )
	Link( s4, s8 )

	#Add link for s5
	Link( s5, s9 )
	Link( s5, s10 )

	#Add link for s6
	Link( s6, s9 )
	Link( s6, s10 )

	#Add link for s7
	Link( h1, s7 )
	Link( h2, s7 )

	#Add link for s8
	Link( h3, s8 )

	#Add link for s9
	Link( h4, s9 )

	#Add link for s10
	Link( h5, s10 )

  net.build()

  h1.cmd("ifconfig h1-eth0 0")

  h2.cmd("ifconfig h2-eth0 0")

  h3.cmd("ifconfig h3-eth0 0")

  h4.cmd("ifconfig h4-eth0 0")
  
  h5.cmd("ifconfig h5-eth0 0")

  s7.cmd("ifconfig s7-eth0 0")

  s7.cmd("ifconfig s75-eth1 0")

  s7.cmd("ifconfig s7-eth2 0")

  s8.cmd("ifconfig s8-eth0 0")

  s8.cmd("ifconfig s8-eth1 0")

  s8.cmd("ifconfig s8-eth2 0")

  s7.cmd("vconfig add s7-eth2 10")

  s7.cmd("vconfig add s7-eth2 20")

  s8.cmd("vconfig add s8-eth2 10")

  s8.cmd("vconfig add s8-eth2 20")

  s7.cmd("ifconfig s7-eth2.10 up")

  s7.cmd("ifconfig s7-eth2.20 up")

  s8.cmd("ifconfig s8-eth2.10 up")

  s8.cmd("ifconfig s8-eth2.20 up")

  s7.cmd("brctl addbr brvlan10")

  s7.cmd("brctl addbr brvlan20")

  s7.cmd("brctl addif brvlan10 s7-eth0")

  s7.cmd("brctl addif brvlan10 s7-eth2.10")

  s7.cmd("brctl addif brvlan20 s7-eth1")

  s7.cmd("brctl addif brvlan20 s7-eth2.20")

  s7.cmd("ifconfig brvlan10 up")

  s7.cmd("ifconfig brvlan20 up")

  s8.cmd("brctl addbr brvlan10")

  s8.cmd("brctl addbr brvlan20")

  s8.cmd("brctl addif brvlan10 s8-eth0")

  s8.cmd("brctl addif brvlan10 s8-eth2.10")

  s8.cmd("brctl addif brvlan20 s8-eth1")

  s8.cmd("brctl addif brvlan20 s8-eth2.20")

  s8.cmd("ifconfig brvlan10 up")

  s8.cmd("ifconfig brvlan20 up")

  h1.cmd("ifconfig h1-eth0 10.0.10.1 netmask 255.255.255.0")

  h2.cmd("ifconfig h2-eth0 10.0.10.2 netmask 255.255.255.0")

  h3.cmd("ifconfig h3-eth0 10.0.10.3 netmask 255.255.255.0")

  h4.cmd("ifconfig h4-eth0 10.0.10.4 netmask 255.255.255.0")
  
  h5.cmd("ifconfig h4-eth0 10.0.10.5 netmask 255.255.255.0")

  CLI(net)

  net.stop()
