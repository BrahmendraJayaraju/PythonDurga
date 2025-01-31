from abc import *
# we cant create object subtest bse we have not implemented m1 method 
class test(ABC):
    @abstractmethod
    def m1(self):
        pass

class subtest(test):
      pass
a=subtest()
