from base.abstract_socket import AbstractSocket
from utils import ip_comma
import time
import os


def do_put(socket: AbstractSocket, from_path: str = "", to_path: str = "", data_port=20):
    try:
        if (not socket.is_connected()):
            print("Not connected.")
            return -1
        data_socket = socket.open(data_port)

        new_host = socket.get_hostname(data_socket)
        new_ip = new_host[0]
        new_port = new_host[1]
        host_comma = ip_comma.to_ip_comma(new_ip, new_port)
        
        relative_path = os.path.join(os.getcwd(), from_path)
        if from_path != "" and not os.path.exists(relative_path):
            print(f"{from_path}: File not found")
            return -1

        socket.send(f"PORT {host_comma}\r\n")
        res = socket.receive()
        print(res, end="")

        if not res.startswith("200"):
            socket.close(data_socket)
            return -1

        socket.send(f"STOR {to_path}\r\n")
        res = socket.receive()
        print(res.rstrip("\r\n"), end="\r\n")

        if (res.startswith("5")):
            socket.close(data_socket)
            return -1

        if (res.startswith("1")):
            start = float(time.time())
            with open(relative_path, 'rb') as fptr:
                socket.send_data(data_socket, fptr)
                file_size = os.path.getsize(relative_path)
                fptr.close()

        print(socket.receive(4096), end="")
        if (res.startswith("1")):
            end = float(time.time())
            time_diff = (end - start) + 1e-10
            if file_size:
                print(f"ftp: {file_size} bytes received in {time_diff:.2f}Seconds {file_size/(time_diff*1000):.2f}Kbytes/sec.")


        return 0
    except Exception as e:
        raise e
