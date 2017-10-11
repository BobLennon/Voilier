import socket
#IPDEST="192.168.0.228" #IP Raspi
IPDEST="127.0.0.1"
PORT=5005
lat=0
longi=0
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto(bytearray([88,2,30,90]),(IPDEST,PORT))


while True:
        data,addr=sock.recvfrom(15)
        print "id : ",ord(data[0])
        print "longeur : ",ord(data[1])
        print "v.vent : ",ord(data[2])
        print "d.vent : ",ord(data[3])
        print "test : ",ord(data[4])
        lat=(float)(ord(data[5])<<24)
        lat=lat+(ord(data[6])<<16)
        lat=lat+(ord(data[7])<<8)
        lat=lat+ord(data[8])
        lat=lat/1000000
        print "Latitude = ",lat
        
        longi=(float)(ord(data[9])<<24)
        longi=longi+(ord(data[10])<<16)
        longi=longi+(ord(data[11])<<8)
        longi=longi+ord(data[12])
        if longi > 127
                longi=(~longi)&0xFFFFFFFF
                longi=longi+1
                longi=longi*-1
        longi=longi/1000000
        print "Longitude = ",longi
