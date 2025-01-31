#data hiding


class account:
    def __init__(self,initialbalance):
        self.balance=initialbalance


#we are accessing directly not good 
a=account(10000)
print(a.balance)