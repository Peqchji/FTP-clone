from abc import ABC, abstractmethod

class AbstractSocket(ABC):
    
    @abstractmethod
    def send():
        raise NotImplementedError
    
    @abstractmethod
    def receive():
        raise NotImplementedError
    
    @abstractmethod
    def connect():
        raise NotImplementedError
    
    @abstractmethod
    def close():
        raise NotImplementedError