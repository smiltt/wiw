import socket, pickle


def open_connection(server, TCP_IP):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, 4000))

    return server

class Net:
    server = None

    def __init__(self, TCP_IP):
        server = open_connection(self.server, TCP_IP)


    def listen(self):
        while True:
            data = self.server.recv(1024)
            data = pickle.loads(data)

            print data

    def send_data(self, data):
        data = pickle.dumps(data)
        self.server.send(data)

    def close_connection(self):
        self.server.close()




