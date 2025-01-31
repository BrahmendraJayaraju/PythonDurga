#data hiding


class account:
    def __init__(self,initialbalance):
        self.__balance=initialbalance  #data hiding

a=account(10000)
print(a.__balance)  #error