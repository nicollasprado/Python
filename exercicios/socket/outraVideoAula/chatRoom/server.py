import threading
# Thread é uma sequência de instruções dentro de um programa
# Rodar várias threads é como rodar vários programas diferentes
import socket

host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
aliases = []

# Função para enviar as mensagens
def broadcast(message):
    for client in clients:
        client.send(message)

# Função para gerenciar as conexões dos clients
def handleClient(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f"{alias} se desconectou do chat".encode('utf-8'))
            aliases.remove(alias)
            break

# Função para receber as conexões dos clients
def receive():
    while True:
        print("O servidor está funcionando e recebendo conexões!")
        client, address = server.accept()
        print(f"Conexão estabelecida com {str(address)}")
        client.send('alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print(f"O apelido do client {client} é {alias}".encode('utf-8'))
        broadcast(f"{alias} se conectou ao chat".encode('utf-8'))
        client.send("Você se conectou ao chat!".encode('utf-8'))
        thread = threading.Thread(target= handleClient, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()