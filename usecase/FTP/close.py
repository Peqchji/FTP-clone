from base.abstract_socket import AbstractSocket

def do_close(socket: AbstractSocket):
    try:
        if not socket.is_connected():
            print("Not connected.")
            return -1
        socket.send("QUIT\r\n")
        print(socket.receive(), end="")
        socket.close()
        return 0
    except Exception as e:
        socket.close()