# -*-coding:Latin-1 -*

import socket
import subprocess
import sys
import datetime
import errno

# Exécution de la commande clear dans le terminal
subprocess.call('clear',shell=True)

remote_server = raw_input('Entrez le nom de domaine :')
remote_server_IP = socket.gethostbyname(remote_server)

#Affichage de l'addresse IPv4 de la cible

print'IPv4 : ', remote_server_IP 

print "."*60
print 'Veuillez patienter pendant le scan de', remote_server_IP
print "."*60


try :
    for port in range (1,65535):
                connexion = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                resultat = connexion.connect_ex((remote_server_IP,port))

                #Afficher les port et si ils sont ouverts 
                if resultat == 0 :
                    print 'Port {} : ouvert'.format(port)

                
#Arreter l'éxécution du script
except KeyboardInterrupt:
        print'Tu as fait Ctrl+C !'
        sys.exit()
        
t2=datetime.now()

Ttotal = t2-t1
print'-'*60
print 'Scan terminer en ',Ttotal,'second'

