from abc import ABC,abstractmethod


class vehicle(ABC):
    @abstractmethod
    def getnowheels(self):
        pass

class bus(vehicle):
     pass
#cant create object bse not implemented in child class
b=bus()