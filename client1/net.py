import socket, pickle
import client


def open_connection(server, TCP_IP):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, 4000))

    return server

def updateVars(data):
    

    client.x = # some x val


class Net:
    server = None

    def __init__(self, TCP_IP):
        server = open_connection(self.server, TCP_IP)


    def listen(self):
        while True:
            data = self.server.recv(1024)
            data = pickle.loads(data)

            updateVars(data)


    def send_data(self, data):
        data = pickle.dumps(data)
        self.server.send(data)

    def close_connection(self):
        self.server.close()




