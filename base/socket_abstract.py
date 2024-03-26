from abc import ABC, abstractmethod

class SocketAbstract(ABC):
    
    @abstractmethod
    def send():
        raise NotImplementedError
    
    @abstractmethod
    def revceive():
        raise NotImplementedError
    
    @abstractmethod
    def connect():
        raise NotImplementedError
    
    @abstractmethod
    def close():
        raise NotImplementedError