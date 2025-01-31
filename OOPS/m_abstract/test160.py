#abstract class

from abc import ABC,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def getnowheels(self):
        pass

