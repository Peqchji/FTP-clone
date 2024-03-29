from app import App
from usecase.FTP_usecase import FTPUsercase
from adapter.socket_adapter import SocketAdapter

if __name__ == "__main__":
    socket = SocketAdapter()
    FTP_usecase = FTPUsercase(socket)
    
    app = App.build(FTP_usecase)
    app.run()