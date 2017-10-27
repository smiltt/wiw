import socket, pickle



def listen():
    while True:
        send_msg("Hello")

def send():
    pass





def send_msg(msg):


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(('127.0.0.1', 4000))

    data = "I'm logged"
    data = pickle.dumps(data)
    server.send(data)
    data = server.recv(1024)
    data = pickle.loads(data)
    print(data)

    server.close()