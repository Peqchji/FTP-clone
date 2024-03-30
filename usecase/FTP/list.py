from base.abstract_socket import AbstractSocket
from utils import ip_comma
import time

def do_ls(socket: AbstractSocket, is_Ls=False, data_port=20):
    try:
        if not socket.is_connected():
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
        
        if(is_Ls):
            socket.send("LIST\r\n")
        else:
            socket.send("NLST\r\n")
        
        res = socket.receive()
        print(res, end="")
        if(res.startswith("5")):
            return -1
        
        if res.startswith("1"):
            start = time.time()
            data = socket.receive_data(data_socket)
            print(data, end="")
        
        print(socket.receive(4096), end="")
        if res.startswith("1"):
            end = time.time()
            time_diff = end - start
            print(f"ftp: {len(data)} bytes received in {time_diff:.2f}Seconds {len(data)/(time_diff*1000):.2f}Kbytes/sec.")
        
        return 0
    except Exception as e:
        print(e.__str__())