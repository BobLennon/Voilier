import socket
PORT=5005
#IPSERV="192.168.0.228" #IP Raspi
IPSERV="127.0.0.1"
lat=5749743
a=0
b=0
c=0
d=0

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IPSERV,PORT))
while True:
        data,addr=sock.recvfrom(10)
        print "id : ",ord(data[0])
        print "leng : ",ord(data[1])
        print "gv : ",ord(data[2])
        print "safran : ",ord(data[3])
        a=(bit32tobit24)delat
        b=(bit23tobit16)delat
        c=(bit15tobit8)delat
        d=(bit7tobit0)delat
        
        sock.sendto(bytearray([88,4,10,180,001,a,b,c,d]),addr)

