import socket, pickle
from client1 import player_data


conn = None

def open_connection(TCP_IP):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((TCP_IP, 8000))
    return server


def update_vars(data):
    player_data.x, player_data.y = pickle.loads(data)

def init(TCP_IP):
    server = open_connection(TCP_IP)
    conn = server
    return conn

def listen():
    while True:
        data = conn.recv(1024)
        data = pickle.loads(data)

        update_vars(data)

def send_keypress(keyval):
    data = pickle.dumps(keyval)
    conn.send(data)

def close_connection():
    conn.close()
