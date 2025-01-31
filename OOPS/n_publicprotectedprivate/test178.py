#data hiding


class account:
    def __init__(self,initialbalance):
        self.__balance=initialbalance  #data hiding

    def getbalance(self):
        #validation and authentication
        return self.__balance


#data hiding and accessing
a=account(10000)
print(a.getbalance())
