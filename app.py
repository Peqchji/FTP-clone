from base.abstract_FTP_usecase import AbstractFTPUsecase

class App:

    _instance = None
    __ftp_usecase: AbstractFTPUsecase = None
    
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
            inp = str(input("ftp> ")).strip().split(" ")
            cmd = inp[0]
            
            if (cmd == "open"):
                is_connected = self.__ftp_usecase.is_connected()
                if (is_connected):
                    print(is_connected)
                    continue
                port = 21
                if (len(inp) >= 3):
                    print("Usage: open host name [port]")
                    continue
                
                if (len(inp) == 1):
                    host = str(input("To ")).strip().split(" ")
                    if (len(host) >= 3 or len(host) < 0):
                        print("Usage: open host name [port]")
                        continue
                    
                    ip = host[0]
                    if (len(host) == 2):
                        port = int(host[1])
                elif (len(inp) >= 2):
                    ip = inp[1]
                    if (len(inp) == 3):
                        port = int(inp[2])
                
                self.__ftp_usecase.open(ip, port)
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
            
            elif (cmd in ["a"]):
                print("Ambiguous command.")
            
            elif (cmd == ""):
                continue
            
            else:
                print("Invalid command.")
            
        return 0