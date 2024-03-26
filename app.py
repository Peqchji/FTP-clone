from base.FTP_usecase_abstract import FTPUsecaseAbstract

class App:

    _instance = None
    __ftp_usecase: FTPUsecaseAbstract = None
    
    def __init__(self) -> None:
        raise RuntimeError("This is a Singleton class, use build() instead.")
    
    @classmethod
    def build(cls, ftp_usecase: FTPUsecaseAbstract):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.__ftp_usecase = ftp_usecase
        return cls._instance
    
    def run(self):
        while True:
            cmd = input("FTP/ ")
            break
        return True