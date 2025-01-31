from abc import ABC,abstractmethod


class vehicle(ABC):
    @abstractmethod
    def getnowheels(self):
        pass

class bus(vehicle):
    def getnowheels(self):
        return 8

class auto(vehicle):
    def getnowheels(self):
        return 3


b=bus()
print(b.getnowheels())
a=auto()
print(a.getnowheels())

