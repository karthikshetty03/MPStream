#!/usr/bin/env python

# Necessary Imports
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.link import Link, TCLink, Intf
from subprocess import Popen, PIPE
from mininet.log import setLogLevel

if __name__ == "__main__":
    setLogLevel('info')
    
    # Initialise the Mininet
    net = Mininet(link=TCLink)

    # To run commands in the terminal
    p = Popen("sysctl -w net.mptcp.mptcp_enabled=1", shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    print("Enabling MPTCP Protocol ....")
    print("stdout : ", stdout)
    print("stderr : ", stderr)

    # Set topology of the virtual network
    client = net.addHost('client')
    server = net.addHost('server')
    router = net.addHost('router')

    # Set link properties
    linkopt = {'bw' : 10}
    linkopt2 = {'bw' : 100}

    # Add links to the network
    net.addLink(router, client, cls=TCLink,**linkopt)
    net.addLink(router, client, cls=TCLink, **linkopt)
    net.addLink(router, server, cls=TCLink, **linkopt2)

    # Build the net
    net.build()

    # Set properties of the network configuration
    
    # Clear the IP addresses
    router.cmd("ifconfig router-eth0 0")
    router.cmd("ifconfig router-eth1 0")
    router.cmd("ifconfig router-eth2 0")
    client.cmd("ifconfig client-eth0 0")
    client.cmd("ifconfig client-eth1 0")
    server.cmd("ifconfig server-eth0 0")

    # Enable IP forwarding
    router.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")

    # Set the interfaces IP of router
    router.cmd("ifconfig router-eth0 10.0.0.1 netmask 255.255.255.0")
    router.cmd("ifconfig router-eth1 10.0.1.1 netmask 255.255.255.0")
    router.cmd("ifconfig router-eth2 10.0.2.1 netmask 255.255.255.0")

    # Set the interfaces IP of client
    client.cmd("ifconfig client-eth0 10.0.0.2 netmask 255.255.255.0")
    client.cmd("ifconfig client-eth1 10.0.1.2 netmask 255.255.255.0")

    # Set the interfaces IP of server
    server.cmd("ifconfig server-eth0 10.0.2.2 netmask 255.255.255.0")

    # Routing configuration for the client
    client.cmd("ip rule add from 10.0.0.2 table 1")
    client.cmd("ip rule add from 10.0.1.2 table 2")
    client.cmd("ip route add 10.0.0.0/24 dev client-eth0 scope link table 1")
    client.cmd("ip route default via 10.0.0.1 dev client-eth0 table 1")
    client.cmd("ip route add 10.0.1.0/24 dev client-eth1 scope link table 2")
    client.cmd("ip route default via 10.0.1.1 dev client-eth1 table 2")
    client.cmd("ip route add default scope global nexthop via 10.0.0.1 dev client-eth0")

    # Routing configuration for the server
    server.cmd("ip rule add from 10.0.2.2 table 1")
    server.cmd("ip route add 10.0.2.0/24 dev server-eth0 scope link table 1")
    server.cmd("ip route add default via 10.0.2.1 dev server-eth0 table 1")
    server.cmd("ip route add default scope global nexthop via 10.0.2.1 dev server-eth0")

    CLI(net)
    net.stop()