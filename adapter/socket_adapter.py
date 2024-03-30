import socket
from base.abstract_socket import AbstractSocket


class SocketAdapter(AbstractSocket):
    client_socket = None
    
    def send(self, data: str):
        try:
            stream = data.encode()
            self.client_socket.send(stream)
            return 0
        except ConnectionAbortedError or ConnectionResetError:
            raise Exception("Connection closed by remote host.")
    
    def receive(self, recieve: int = 1024):
        try:
            res = self.client_socket.recv(recieve)
            return res.decode()
        except ConnectionAbortedError or ConnectionResetError:
            raise Exception("Connection closed by remote host.")
    
    def connect(self, IP, port):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((IP, port))
            return 0
        except ConnectionRefusedError:
            raise Exception("> ftp: connect :Connection refused")

    def close(self):
        try:
            self.client_socket.close()
            self.client_socket = None
            return 0
        except:
            return None
    
    def is_connected(self):
        if self.client_socket is not None:
            return f"Already connected to {self.client_socket.getpeername()[0]}, use disconnect first."
        return False