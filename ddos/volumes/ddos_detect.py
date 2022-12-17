import socket
import struct
from datetime import datetime

IP_REQUEST_LIMIT = 25
detectSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
ipDict = {}
while True:
    packetData = detectSocket.recvfrom(2048)
    ipPacketHeader = packetData[0][14:34]
    unpackedHeader = struct.unpack("!8sB3s4s4s", ipPacketHeader)
    srcIP = socket.inet_ntoa(unpackedHeader[4])
    toIP = socket.inet_ntoa(unpackedHeader[3])
    if srcIP in ipDict:
        ipDict[srcIP]=ipDict[srcIP]+1
        if(ipDict[srcIP] > IP_REQUEST_LIMIT) :
            print("DDoS attack detected from Source IP: ", srcIP, " to Target IP: ", toIP, " with Count: ", ipDict[srcIP])
    else:
        ipDict[srcIP] = 1
