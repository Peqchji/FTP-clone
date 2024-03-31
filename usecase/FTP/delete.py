from base.abstract_socket import AbstractSocket

def do_delete(socket: AbstractSocket, filename):
    try:
        if not socket.is_connected():
            print("Not connected.")
            return -1
        
        socket.send(f"DELE {filename}\r\n")
        print(socket.receive(), end="")
        return 0
    except Exception as e:
        print(e.__str__())