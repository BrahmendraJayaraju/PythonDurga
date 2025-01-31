
#interface, abstract  and concrete class combination
from abc import *
class collegeautomation(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

    @abstractmethod
    def m3(self):
        pass


class absclas(collegeautomation) :
    def m1(self):
       print('m1 method implemented')


    def m2(self):
        print('m2 method implemented')


class con( absclas):

    def m3(self):
        print('m3 method implemented')

d=con()
d.m1()
d.m2()
d.m3()