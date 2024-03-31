from base.abstract_socket import AbstractSocket
from utils import ip_comma
import time
import os

def do_ls(socket: AbstractSocket, log_to, remote_dir, is_Ls=False, data_port=20):
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
            return -1
        
        write_to = os.path.join(os.getcwd(), log_to)
        print(write_to, os.path.isdir(os.getcwd()))
        if log_to != "" and not os.path.isdir(log_to):
            print(f"Error opening local file {log_to}.")
            raise Exception("> .:No Such file or directory")
        
        if (is_Ls):
            socket.send(f"LIST {remote_dir}\r\n")
        else:
            socket.send(f"NLST {remote_dir}\r\n")
        
        res = socket.receive()
        print(res, end="")
        if (res.startswith("5")):
            return -1
        
        if (res.startswith("1")):
            start = float(time.time())
            data = socket.receive_data(data_socket)
            print(data, end="")
        
        print(socket.receive(4096), end="")
        if (res.startswith("1")):
            end = float(time.time())
            time_diff = (end - start) + 0.001
            print(f"ftp: {len(data)} bytes received in {time_diff:.2f}Seconds {len(data)/(time_diff*1000):.2f}Kbytes/sec.")
            
            # if (log_to != ""):
            #     with os.open(f"{write_to}", "a+") as fptr:
            #         fptr.write(data)
            #         fptr.close()
        
        return 0
    except Exception as e:
        print(e.__str__())