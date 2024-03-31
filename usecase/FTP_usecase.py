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

    def cd(self, change_to: str):
        return change_dir.do_cd(self.__socket, change_to)

    def close(self):
        return close.do_close(self.__socket)

    def delete(self, filename):
        return delete.do_delete(self.__socket, filename)

    def disconnect(self):
        return close.do_close(self.__socket)

    def get(self, to_path, remote_file, data_port):
        return get.do_get(self.__socket, to_path, remote_file, data_port)

    def ls(self, is_Ls, log_to, remote_dir, data_port):
        return ls.do_ls(
            self.__socket, 
            log_to, 
            remote_dir, 
            is_Ls, 
            data_port
        )

    def open(self, server_ip, server_port=21):
        return open.do_open(self.__socket, server_ip, server_port)

    def put():
        pass

    def pwd(self):
        return pwd.do_pwd(self.__socket)

    def quit(self):
        return quit.do_quit(self.__socket)

    def rename(self, from_name, to_name):
        return rename.do_rename(self.__socket, from_name, to_name)

    def user(self, username, password):
        return user.do_user(self.__socket, username, password)

    def is_connected(self):
        return self.__socket.is_connected()
