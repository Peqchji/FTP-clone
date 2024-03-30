import getpass
from base.abstract_socket import AbstractSocket

def do_open(socket: AbstractSocket, server_ip, server_port = 21):
    try:
        socket.connect(server_ip, server_port)
        print(socket.receive(), end="")
        
        socket.send("OPTS UTF8 ON\r\n")
        print(socket.receive(), end="")
        
        username = str(input(f"User ({server_ip}:(none)): ")).strip()
        socket.send(f"USER {username}\r\n")
        res = socket.receive()
        print(res, end="")
        
        if (res.startswith("501")):
            print("Login failed.")
            return -1
        
        password = getpass.getpass("Password: ")
        socket.send(f"PASS {password}\r\n")
        print(socket.receive(), end="")
        
        return 0
    except Exception as e:
        print(e.__str__())