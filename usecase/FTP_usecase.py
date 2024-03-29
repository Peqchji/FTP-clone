from base.abstract_FTP_usecase import AbstractFTPUsecase
from base.abstract_socket import AbstractSocket

from usecase.FTP import *

class FTPUsercase(AbstractFTPUsecase):
    __socket: AbstractSocket = None
    
    def __init__(self, socket: AbstractSocket = None):
        self.__socket = socket
    
    def ascii():
        pass

    def binary():
        pass

    def bye(self):
        return quit.do_quit(self.__socket)

    def cd():
        pass

    def close(self):
        return close.do_close(self.__socket)

    def delete():
        pass

    def disconnect(self):
        return close.do_close(self.__socket)

    def get():
        pass
    
    def ls():
        pass
    
    def open(self, server_ip, server_port = 21):
        return open.do_open(self.__socket, server_ip, server_port)
    
    def is_connected(self):
        return self.__socket.is_connected()
    
    def put():
        pass
    
    def pwd():
        pass
    
    def quit(self):
        return quit.do_quit(self.__socket)
    
    def rename():
        pass
    
    def user():
        pass