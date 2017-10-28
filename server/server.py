import socket, select, pickle, threading, time


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 8000))
server.listen(5)

clients = []
client_threads = []
connections = []
id = 0

def main():
    connection_listener = threading.Thread(listen_for_connections())

    while(True):
        update_clients()
        time.sleep(0.01)


def update_clients():
    for client in clients:
        client.send_data(client.get_pos())


def listen_for_connections():
    while 1:
        conn, addr = server.accept()
        clients.append(Client(conn, addr, id))
        increment_id()
        time.sleep(0.05)

def increment_id():
    global id
    id += 1

def calc_delta_pos(keychar):
    if keychar == 1:
        return (0,0.1)
    elif keychar == 2:
        return (0,-0.1)
    elif keychar == 3:
        return (0.1, 0)
    elif keychar == 4:
        return (-0.1,0)

class Client:
    conn = None
    addr = None
    id = None
    pos = None

    def get_pos(self):
        return self.pos

    def __init__(self, conn, addr, id):
        self.conn = conn
        print (addr)
        self.addr = addr
        self.id = id
        self.pos = (0,0)

        print("Connection received from address ")
        print(addr)
        self.listen_for_updates()

    def send_data(self, data):
        data = pickle.dumps(data)
        self.conn.send(data)

    def close(self):
        self.conn.close()

    def shutdown(self):
        self.conn.shutdown(1)

    def listen_for_updates(self):
        while 1:
            data = self.conn.recv(1024)
            pos = (self.pos) + calc_delta_pos(data)
            print (pos)


main()
server.close()
