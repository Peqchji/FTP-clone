from base.abstract_socket import AbstractSocket

def do_rename(socket: AbstractSocket, from_name: str, to_name: str):
    try:
        if not socket.is_connected():
            print("Not connected.")
            return -1
        
        socket.send(f"RNFR {from_name}\r\n")
        res = socket.receive()
        print(res, end="")
        
        if res.startswith("5"):
            return -1
        
        if res.startswith("350"):
            socket.send(f"RNTO {to_name}\r\n")
            print(socket.receive(), end="")
        
        return 0
    except Exception as e:
        print(e.__str__())