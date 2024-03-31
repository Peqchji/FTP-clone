from base.abstract_socket import AbstractSocket
from utils import ip_comma
import time
import os

def do_get(socket: AbstractSocket, to_path: str, remote_file: str, data_port=20):
    try:
        if (not socket.is_connected()):
            print("Not connected.")
            return -1
        data_socket = socket.open(data_port)
        
        new_host = socket.get_hostname(data_socket)
        new_ip = new_host[0]
        new_port = new_host[1]
        host_comma = ip_comma.to_ip_comma(new_ip, new_port)
        
        socket.send(f"PORT {host_comma}\r\n")
        res = socket.receive()
        print(res, end="")
        
        if not res.startswith("200"):
            socket.close(data_socket)
            return -1
        
        new_file = to_path.split("/")[-1]
        to_dir = to_path.removesuffix(new_file)
        write_to = os.path.join(os.getcwd(), to_dir)
        
        socket.send(f"RETR {remote_file}\r\n")
        res = socket.receive()
        print(res.rstrip("\r\n"), end="\r\n")
        
        if (res.startswith("5")):
            socket.close(data_socket)
            return -1
        
        if to_path != "" and not os.path.isdir(write_to):
            print(f"> R:No such process")
            to_path = ""
        
        if (res.startswith("1")):
            start = float(time.time())
            data = socket.receive_data(data_socket)
        
        print(socket.receive(4096), end="")
        if (res.startswith("1")):
            end = float(time.time())
            time_diff = (end - start) + 1e-10
            print(f"ftp: {len(data)} bytes received in {time_diff:.2f}Seconds {len(data)/(time_diff*1000):.2f}Kbytes/sec.")
            
            if (to_path != ""):
                with open(os.path.join(write_to, new_file), 'w+') as file:
                    file.write(data)
                    file.seek(0)
                    file.close()
        
        return 0
    except Exception as e:
        raise e