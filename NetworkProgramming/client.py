import socket
import threading

class Client:
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def run(self):
        self.socket.connect((self.hostname, self.port))
        nickname = input('Choose your nickname: ')
        self.nickname = nickname
        
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

    def receive(self):
        while True:
            try:
                message = self.socket.recv(1024).decode()
                if message == 'NICKNAME':
                    self.socket.send(self.nickname.encode())
                else:
                    print(message)
            except:
                print('An error occured!')
                self.socket.close()
                break

    def write(self):
        while True:
            message = input()
            self.socket.send(f'{self.nickname}: {message}'.encode())

if __name__ == '__main__':
    client = Client(socket.gethostname(), 1234)
    client.run()