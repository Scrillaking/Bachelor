
from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
from mininet.node import OVSSwitch, RemoteController
import time 

def main():

   lg.setLogLevel('info')

   #Create the network
   net = Mininet(controller=RemoteController)
 
   #Connect to the floodlight controller
   net.addController('c0' , controller=RemoteController,ip="0.0.0.0",port=6633)
 
   #Add hosts
   h1 = net.addHost('h1')
   h2 = net.addHost('h2')
   h3 = net.addHost('h3')
 
   #Add switches
   s1 = net.addSwitch('s1')
   s2 = net.addSwitch('s2')
   s3 = net.addSwitch('s3')
 
   #Add links
   net.addLink(h1,s1)
   net.addLink(h2,s2)
   net.addLink(h3,s3)
   net.addLink(s1,s2)
   net.addLink(s2,s3)

   s1.setIP('10.0.0.20',intf = 's1-eth1')
   s2.setIP('10.0.0.30',intf = 's2-eth1')
   s3.setIP('10.0.0.40',intf = 's3-eth1')

   net.start()

   p_s1 = s1.popen('python newSwitch.py s1 10.0.0.20 3000')
   time.sleep(1)

   p_s2 = s2.popen('python newSwitch.py s2 10.0.0.30 3100')
   time.sleep(1)

   p_s3 = s3.popen('python newSwitch.py s3 10.0.0.40 3200')
   time.sleep(1)

   p_h1 = h1.popen('python newHost.py h1 10.0.0.1 2000')
   time.sleep(1)

   #p_h2 = h2.popen('python newHost.py h2 10.0.0.2 2100')
   #time.sleep(1)

   #p_h3 = h3.popen('python newHost.py h3 10.0.0.3 2200')
   #time.sleep(1)
   
   CLI( net )

   p_s1.terminate()
   p_s2.terminate()
   p_s3.terminate()
   
   p_h1.terminate()
   #p_h2.terminate()
   #p_h3.terminate()

   net.stop()

if __name__ == '__main__':
    main()
