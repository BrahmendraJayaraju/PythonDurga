#example of encapsulation
#data hiding +abstraction


class account:

    #data hiding
    def __init__(self,initialbalance):
        self.__balance=initialbalance

    #abstraction all below 3
    def getbalance(self):
        #authentication
        return self.__balance

    def deposit(self,amount):
        #authentication
        self.__balance=self.__balance+amount

    def withdraw(self, amount):
        # authentication
        self.__balance = self.__balance-amount




