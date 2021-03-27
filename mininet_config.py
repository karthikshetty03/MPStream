from mininet.net import Mininet
from mininet.node import Host
from mininet.node import OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def myNetwork():

    net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')
    info('*** Adding controller\n')
    info('*** Adding switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')

    info('*** Adding hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)

    info('*** Adding links\n')
    net.addLink(h1, s1)
    net.addLink(s1, h2)

    info('*** Starting network\n')
    net.build()
    info('*** Starting controllers\n')

    info('*** Starting switches\n')
    net.get('s1').start([])

    info('*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()