import socket
PORT=5005
#IPSERV="192.168.0.228" #IP Raspi
IPSERV="127.0.0.1"
lat=48.409484
longi=-4.487820
longi1=0b11111111111111111111111111111111
longi2=0b00000000000000000000000000000001
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((IPSERV,PORT))
while True:
        data,addr=sock.recvfrom(15)
        print "id : ",ord(data[0])
        print "leng : ",ord(data[1])
        print "gv : ",ord(data[2])
        print "safran : ",ord(data[3])
        lat=(int)(lat*1000000)
        a=(lat>>24)&0XFF
        b=(lat>>16)&0xFF
        c=(lat>>8)&0XFF
        d=lat&0xFF
        longi=(int)(longi*1000000)
        longi=longi+longi1
        longi=longi+longi2
        e=(longi>>24)&0XFF
        f=(longi>>16)&0xFF
        g=(longi>>8)&0XFF
        h=longi&0xFF
        sock.sendto(bytearray([88,4,10,180,001,a,b,c,d,e,f,g,h]),addr)

#48.409484,-4.487820
