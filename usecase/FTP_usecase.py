from base.FTP_usecase_abstract import FTPUsecaseAbstract
from base.socket_abstract import SocketAbstract

class FTPUsercase():
    __socket: SocketAbstract = None
    
    def __init__(self, socket: SocketAbstract = None):
        self.__socket = socket
    
    def ascii():
        pass

    def binary():
        pass

    def bye():
        pass

    def cd():
        pass

    def close():
        pass

    def delete():
        pass

    def disconnect():
        pass

    def get():
        pass
    
    def ls():
        pass
    
    def open():
        pass
    
    def put():
        pass
    
    def pwd():
        pass
    
    def quit():
        pass
    
    def rename():
        pass
    
    def user():
        pass