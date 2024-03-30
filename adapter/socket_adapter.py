import socket
from base.abstract_socket import AbstractSocket
import sys

class SocketAdapter(AbstractSocket):
    client_socket = None

    def send(self, data: str, socket=None):
        try:
            if socket is None:
                socket = self.client_socket

            stream = data.encode()
            socket.send(stream)
            return 0
        except ConnectionAbortedError or ConnectionResetError:
            raise Exception("Connection closed by remote host.")

    def receive(self, recieve: int = 1024, socket=None):
        try:
            if socket is None:
                socket = self.client_socket

            res = socket.recv(recieve)
            return res.decode()
        except ConnectionAbortedError or ConnectionResetError:
            raise Exception("Connection closed by remote host.")

    def connect(self, IP, port):
        try:
            self.client_socket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((IP, port))
            return 0
        except ConnectionRefusedError:
            raise Exception("> ftp: connect :Connection refused")

    def open(self, to_port=20):
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.bind(
            (
                self.get_hostname()[0],
                0
            )
        )
        new_socket.listen(1)
        
        return new_socket
    
    def receive_data(self, socket: socket.socket):
        conn, _ = socket.accept()
        res = ""
        while True:
            temp = self.receive(4096, conn)
            if not temp:
                break
            
            res += temp
        conn.close()
        socket.close()
        return res

    def close(self, socket=None):
        try:
            if socket is not None:
                socket = self.client_socket
                socket.close()
            else:
                self.client_socket.close()
                self.client_socket = None
            
            return 0
        except:
            return None

    def get_hostname(self, socket=None):
        if socket is not None:
            return socket.getsockname()

        return self.client_socket.getsockname()

    def get_peername(self, socket=None):
        if socket is not None:
            return socket.getpeername()

        return self.client_socket.getpeername()

    def is_connected(self, socket=None):
        if socket is None:
            socket = self.client_socket
        if socket is not None and socket.fileno():
            return f"Already connected to {socket.getpeername()[0]}, use disconnect first."
        return False
