from abc import ABC, abstractmethod

class FTPUsecaseAbstract(ABC):
    
    @abstractmethod
    def ascii():
        raise NotImplementedError

    @abstractmethod
    def binary():
        raise NotImplementedError

    @abstractmethod
    def bye():
        raise NotImplementedError

    @abstractmethod
    def cd():
        raise NotImplementedError

    @abstractmethod
    def close():
        raise NotImplementedError

    @abstractmethod
    def delete():
        raise NotImplementedError

    @abstractmethod
    def disconnect():
        raise NotImplementedError

    @abstractmethod
    def get():
        raise NotImplementedError
    
    @abstractmethod
    def ls():
        raise NotImplementedError
    
    @abstractmethod
    def open():
        raise NotImplementedError
    
    @abstractmethod
    def put():
        raise NotImplementedError
    
    @abstractmethod
    def pwd():
        raise NotImplementedError
    
    @abstractmethod
    def quit():
        raise NotImplementedError
    
    @abstractmethod
    def rename():
        raise NotImplementedError
    
    @abstractmethod
    def user():
        raise NotImplementedError