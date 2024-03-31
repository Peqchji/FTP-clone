from base.abstract_socket import AbstractSocket

def do_cd(socket: AbstractSocket, change_to="./"):
    try:
        if not socket.is_connected():
            print("Not connected.")
            return -1
        
        if (change_to == "./"):
            return 0
        
        socket.send(f"CWD {change_to}\r\n")
        print(socket.receive(), end="")
        return 0
    except Exception as e:
        print(e.__str__())