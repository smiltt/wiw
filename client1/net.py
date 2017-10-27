import socket, pickle


class Net:
    server = None

    def listen(self):
        while True:
            data = server.recv(1024)
            data = pickle.loads(data)

            print data

    def send_data(self, data):
        data = pickle.dumps(data)
        self.server.send(data)


    def open_connection(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(('127.0.0.', 4000))te a

    def close_connection(self):
        self.server.close()




