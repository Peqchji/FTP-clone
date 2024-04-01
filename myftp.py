from app import App
from usecase.FTP_usecase import FTPUsercase
from adapter.socket_adapter import SocketAdapter

if __name__ == "__main__":
    socket = SocketAdapter()
    FTP_usecase = FTPUsercase(socket)
    
    app = App.build(FTP_usecase)
    app.set_server_data_port(14148) # change to FTP server data port. leave blank for port 20
    app.run()