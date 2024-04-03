import getpass
from base.abstract_socket import AbstractSocket

def do_open(socket: AbstractSocket, server_ip, server_port = 21):
    try:
        socket.connect(server_ip, server_port)
        print(f"Connected to {server_ip}.")
        print(socket.receive(), end="")
        
        socket.send("OPTS UTF8 ON\r\n")
        print(socket.receive(), end="")
        
        username = str(input(f"User ({server_ip}:(none)): ")).strip()
        socket.send(f"USER {username}\r\n")
        res = socket.receive()
        print(res, end="")
        
        if (res.startswith("5")):
            print("Login failed.")
            return -1
        
        password = getpass.getpass("Password: ")
        socket.send(f"PASS {password}\r\n")
        res = socket.receive()
        print(res, end="")
        
        if (res.startswith("5")):
            print("Login failed.")
        
        return socket.get_peername()
    except Exception as e:
        print(e.__str__())