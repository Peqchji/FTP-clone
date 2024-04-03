from base.abstract_FTP_usecase import AbstractFTPUsecase


class App:

    _instance = None
    __ftp_usecase: AbstractFTPUsecase = None
    __server_data_port: int = 20

    def set_server_data_port(self, port: int = 20):
        self.__server_data_port = port
        return self.__server_data_port

    def __init__(self) -> None:
        raise RuntimeError("This is a Singleton class, use build() instead.")

    @classmethod
    def build(cls, ftp_usecase: AbstractFTPUsecase):
        if (cls._instance is None):
            cls._instance = cls.__new__(cls)

        if (cls.__ftp_usecase is None):
            cls.__ftp_usecase = ftp_usecase

        return cls._instance

    def run(self):

        while True:
            inp = str(input("ftp> ")).strip().split()
            cmd = inp[0].lower()

            if (cmd == "open"):
                is_connected = self.__ftp_usecase.is_connected()
                if (is_connected):
                    print(is_connected)
                    continue
                port = 21
                if (len(inp) > 3):
                    print("Usage: open host name [port]")
                    continue

                if (len(inp) == 1):
                    host = str(input("To ")).strip().split()
                    if (len(host) >= 3 or (len(host) == 1 and host[0] == "")):
                        print("Usage: open host name [port]")
                        continue

                    ip = host[0]
                    if (len(host) == 2):
                        port = int(host[1])
                elif (len(inp) >= 2):
                    ip = inp[1]
                    if (len(inp) == 3):
                        port = int(inp[2])

                peername = self.__ftp_usecase.open(ip, port)
                continue
            elif (cmd == "user"):
                username = ""
                password = ""
                is_connected = self.__ftp_usecase.is_connected()
                if (not is_connected):
                    print("Not connected.")
                    continue

                if (len(inp) > 4):
                    print("Usage: user username [password] [account]")
                    continue

                if (len(inp) == 1):
                    credential = str(input("Username ")).strip().split()
                    if (len(credential) > 3 or (len(credential) == 1 and credential[0] == "")):
                        print("Usage: user username [password] [account]")
                        continue

                    username = credential[0]
                    if (len(credential) == 2):
                        password = credential[1]
                elif (len(inp) >= 2):
                    username = inp[1]
                    if (len(inp) == 3):
                        password = inp[2]

                self.__ftp_usecase.user(username, password)
                continue
            elif (cmd == "disconnect" or cmd == "close"):
                self.__ftp_usecase.disconnect()
                continue
            elif (cmd == "bye" or cmd == "quit"):
                self.__ftp_usecase.bye()
                print()
                break
            elif (cmd == "ascii"):
                self.__ftp_usecase.ascii()
                continue
            elif (cmd == "binary"):
                self.__ftp_usecase.binary()
                continue
            elif (cmd == "ls"):
                write_to = ""
                is_Ls = False
                if inp[0].startswith("L"):
                    is_Ls = True

                if len(inp) == 1:
                    remote_dir = "."
                elif len(inp) == 2:
                    remote_dir = inp[1]
                elif len(inp) == 3:
                    remote_dir = inp[1]
                    write_to = inp[2]
                else:
                    print("Usage: ls remote directory local file.")
                    continue

                self.__ftp_usecase.ls(
                    is_Ls, write_to, remote_dir, self.__server_data_port)
                continue
            elif (cmd == "get"):
                write_to = ""
                if len(inp) == 1:
                    remote_file = input("Remote file ").strip().split()[0]
                    if remote_file == "":
                        print("Remote file get [ local-file ].")
                        continue
                    write_to = input("Local file ").strip().split()[0]
                elif len(inp) == 2:
                    remote_file = inp[1]
                elif len(inp) >= 3:
                    remote_file = inp[1]
                    write_to = inp[2]

                if write_to == "":
                    write_to = remote_file.split("/")[-1]

                self.__ftp_usecase.get(
                    write_to, remote_file, self.__server_data_port)
                continue
            elif (cmd == "put"):
                from_path = ""
                remote_file = ""
                if len(inp) == 1:
                    from_path = input("Local file ").strip().split()[0]
                    if from_path == "":
                        print("Local file put: remote file.")
                        continue
                    remote_file = input("Remote file ").strip().split()[0]
                elif len(inp) == 2:
                    from_path = inp[1]
                elif len(inp) >= 3:
                    from_path = inp[1]
                    remote_file = inp[2]

                if remote_file == "":
                    remote_file = from_path.split("/")[-1]

                self.__ftp_usecase.put(
                    from_path, remote_file, self.__server_data_port)
                continue
                continue
            elif (cmd == "cd"):
                change_to = "."
                is_connected = self.__ftp_usecase.is_connected()
                if (not is_connected):
                    print("Not connected.")
                    continue

                if len(inp) == 1:
                    change_to = input("Remote directory ").strip().split()[0]
                    if change_to == "":
                        print("cd remote directory.")
                        continue
                else:
                    change_to = inp[1]

                self.__ftp_usecase.cd(change_to)
                continue
            elif (cmd == "delete"):
                is_connected = self.__ftp_usecase.is_connected()
                if (not is_connected):
                    print("Not connected.")
                    continue

                if len(inp) == 1:
                    filename = input("Remote file ").strip().split()[0]
                    if filename == "":
                        print("delete remote file.")
                        continue
                else:
                    filename = inp[1]

                self.__ftp_usecase.delete(filename)
                continue
            elif (cmd == "pwd"):
                self.__ftp_usecase.pwd()
                continue
            elif (cmd == "rename"):
                from_name = ""
                to_name = ""
                is_connected = self.__ftp_usecase.is_connected()
                if (not is_connected):
                    print("Not connected.")
                    continue

                if len(inp) == 1:
                    from_name = input("From name ").strip().split()[0]
                    if from_name == "":
                        print("rename from-name to-name.")
                        continue

                if len(inp) in [1, 2]:
                    to_name = input("To name ").strip().split()[0]
                    if to_name == "":
                        print("rename from-name to-name.")
                        continue

                if len(inp) in [2, 3]:
                    from_name = inp[1]

                if len(inp) == 3:
                    to_name = inp[2]

                self.__ftp_usecase.rename(from_name, to_name)
                continue
            elif (cmd in ["a", "b", "c", "d", "g"]):
                print("Ambiguous command.")
            elif (cmd == ""):
                continue
            else:
                print("Invalid command.")

        return 0
