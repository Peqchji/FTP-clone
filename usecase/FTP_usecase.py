from base.abstract_FTP_usecase import AbstractFTPUsecase
from base.abstract_socket import AbstractSocket

from usecase.FTP import *


class FTPUsercase(AbstractFTPUsecase):
    __socket: AbstractSocket = None

    def __init__(self, socket: AbstractSocket = None):
        self.__socket = socket

    def ascii(self):
        return transfer_type.set_type(self.__socket, "A")

    def binary(self):
        return transfer_type.set_type(self.__socket, "I")

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

    def ls(self, is_Ls, data_port):
        return ls.do_ls(self.__socket, is_Ls, data_port)

    def open(self, server_ip, server_port=21):
        return open.do_open(self.__socket, server_ip, server_port)

    def put():
        pass

    def pwd():
        pass

    def quit(self):
        return quit.do_quit(self.__socket)

    def rename():
        pass

    def user(self, username, password):
        return user.do_user(self.__socket, username, password)

    def is_connected(self):
        return self.__socket.is_connected()
