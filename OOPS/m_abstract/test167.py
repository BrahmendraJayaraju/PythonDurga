from abc import *
#cant create object bse m2 is not implemented 
class test(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class subtest(test):

    def m1(self):
        print('m1 method of subtest')

a=subtest()
a.m1()