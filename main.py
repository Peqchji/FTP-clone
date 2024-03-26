from app import App
from usecase.FTP_usecase import FTPUsercase

if __name__ == "__main__":
    FTP_usecase = FTPUsercase()
    app = App.build(FTP_usecase)
    app_2 = App.build(FTP_usecase)
    print(app._ftp_usecase)
    app.run()