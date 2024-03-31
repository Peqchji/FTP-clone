from base.abstract_socket import AbstractSocket

def do_pwd(socket: AbstractSocket):
    try:
        if not socket.is_connected():
            print("Not connected.")
            return -1
        
        socket.send(f"XPWD\r\n")
        print(socket.receive(), end="")
        return 0
    except Exception as e:
        print(e.__str__())