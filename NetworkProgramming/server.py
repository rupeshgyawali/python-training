import socket
import threading

class Server:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.clients = []
        self.nicknames = []

    def run(self):
        self.socket.listen()
        while True:
            client, addr = self.socket.accept()
            print(f'Connenction from {addr}')

            client.send(b'NICKNAME')
            nickname = client.recv(1024).decode()
            self.nicknames.append(nickname)
            self.clients.append(client)

            print(f'Nickname of the client is {nickname}')
            client.send(b'Connected to the server')
            self.broadcast(f'{nickname} joined the room!'.encode())

            thread = threading.Thread(target=self.handel, args=(client,))
            thread.start()

    def broadcast(self, message):
        for client in self.clients:
            client.send(message)

    def handel(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.broadcast(message)
            except:
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                nickname = self.nicknames[index]
                self.broadcast(f'{nickname} left the room'.encode())
                self.nicknames.remove(nickname)
                break


if __name__ == '__main__':
    server = Server(socket.gethostname(), 1234)
    server.run()


