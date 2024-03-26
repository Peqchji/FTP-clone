from base.FTP_usecase_abstract import FTPUsecaseAbstract
from base.socket_abstract import SocketAbstract

class FTPUsercase():
    __socket: SocketAbstract = None
    
    def __init__(self, socket: SocketAbstract = None):
        self.__socket = socket