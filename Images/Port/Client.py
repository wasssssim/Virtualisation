import socket
import subprocess
ip_dest = "172.23.189.53" 
port_dest = 3000
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# Création du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip_dest, port_dest))


query=  ['netsh' 'advfirewall' 'firewall' 'add' 'rule' 'name="Ouvrir Port 3000 Sortant"' 'dir=out' 'action=allow' 'protocol=TCP' 'localport=3000']
subprocess.run(query, shell=True)
message = f"Mon ip c'est {local_ip}"
client_socket.sendall(message.encode())
print("Message envoyé :", message)

# Réception de la réponse (jusqu'à 1024 octets)
data = client_socket.recv(1024)
print("Réception de :", data.decode())

client_socket.close()
