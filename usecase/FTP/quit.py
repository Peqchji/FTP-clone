from base.abstract_socket import AbstractSocket

def do_quit(socket: AbstractSocket):
    try:
        if socket.is_connected():
            socket.send("QUIT\r\n")
            print(socket.receive(), end="")
            socket.close()
        return 0
    except Exception as e:
        socket.close()