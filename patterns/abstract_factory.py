from abc import ABC, abstractmethod


class Sneaker(ABC):
    color: str   

class RedSneaker(Sneaker):
    color: str = 'red'

class GreenSneaker(Sneaker):
    color: str = 'green'

class Sock(ABC):
    color: str

class RedSock(Sock):
    color: str = 'red'

class GreenSock(Sock):
    color: str = 'green'

class Factory(ABC):
    @abstractmethod
    def create_sock(self) -> Sock:
        pass

    @abstractmethod
    def create_sneaker(self) -> Sneaker:
        pass

class GreenFactory(Factory):
    def create_sock(self) -> Sock:
        return GreenSock()
    
    def create_sneaker(self) -> Sneaker:
        return GreenSneaker()
    
class RedFactory(Factory):
    def create_sock(self) -> Sock:
        return RedSock()
    
    def create_sneaker(self) -> Sneaker:
        return RedSneaker()