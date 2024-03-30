import getpass
from base.abstract_socket import AbstractSocket


def do_user(socket: AbstractSocket, username: str = "", password: str = ""):
    try:
        if not socket.is_connected():
            print("Not connected.")
            return -1

        if (username == ""):
            username = str(
                input(f"User ({socket.get_peername()[0]}:(none)): ")).strip()
        socket.send(f"USER {username}\r\n")
        res = socket.receive()
        print(res, end="")

        if (res.startswith("5")):
            print("Login failed.")
            return -1

        if (password == ""):
            password = getpass.getpass("Password: ")
        socket.send(f"PASS {password}\r\n")
        res = socket.receive()
        print(res, end="")

        if (res.startswith("5")):
            print("Login failed.")

        return 0
    except Exception as e:
        print(e.__str__())
