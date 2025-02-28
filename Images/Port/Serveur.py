import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adresse = ('localhost', 3000)
server_socket.bind(server_adresse)
server_socket.listen(10)
print("Serveur en attente de connexion sur le port 3000...")

while True:
    conn, addr = server_socket.accept()
    print("Connexion établie avec :", addr)
    
    data = conn.recv(1024)
    if not data:
        break
    print("Message reçu :", data.decode())
    
    # Renvoyer le message au client (echo)
    conn.sendall(data)
    conn.close()
