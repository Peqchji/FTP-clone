from base.abstract_socket import AbstractSocket

def do_user(socket: AbstractSocket, type: str):
    try:
        if not socket.is_connected():
            print("Not connected.")
            return -1
        
        socket.send(f"TYPE {type}\r\n")
        print(socket.receive(), end="")
    except Exception as e:
        print(e.__str__())