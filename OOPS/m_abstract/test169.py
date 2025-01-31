#class can contain both abstract and non  abstract methods
from abc import *
class test(ABC):

    def m1(self):
        print('non abstract  method of  test')

    @abstractmethod
    def m2(self):
        pass


class subtest(test):


    def m2(self):
        print('m2 method of subtest')

a=subtest()
a.m1()
a.m2()