# -*- coding: utf-8 -*-
import socket
IPDEST="192.168.0.202"                                                  #adresse destination
PORT=5005                                                               #port a utiliser
cinema="cinema"                                                         #message a envoyer

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                    #Internet,UDP
sock.sendto(cinema,(IPDEST,PORT))                                       #envoi de de cinema a telle adresse a telle port

while True:                                                             #tant que 1
    trameReponse,addr=sock.recvfrom(1024)                               #trameReponse est la trame reçu de telle adresse en écoutant les 1024 premier octet
    code=(int)(ord(trameReponse[3])<<24)                                #la variable code est égale en entier au quatrième octet décaler de 24 zero vers la gauche
    code=code+(ord(trameReponse[2])<<16)                                #la variable code est égale a code + au troisième octet décaler de 16 zero vers la gauche
    code=code+(ord(trameReponse[1])<<8)                                 #la variable code est égale a code + au deuxième octet décaler de 8 zero vers la gauche
    code=code+ord(trameReponse[0])                                      #la variable code est égale a code + au premier octet
    print "Réception de la trame de réponse", trameReponse.encode("hex")#affiche le contenu de trameReponse encodé en hexadécimal
    print "le code =",code                                              #affiche le contenu de code


#le code est 4158522552
