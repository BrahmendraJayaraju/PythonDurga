from abc import *
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

    def m2(self):
        print('m2 method of subtest')

a=subtest()
a.m1()
a.m2()