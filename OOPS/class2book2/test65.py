from scipy.fft import ifft2


class  cutomer:
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('your deposit balance:',self.balance)

    def withdraw(self,amount):
        if amount>self.balance:
            print('you dont have enough balance to withdraw')
        else:
            self.balance=self.balance-amount
            print('after withdraw balance:', self.balance)

print('welcome to axis bank')
name=input('enter your name:')
c=cutomer(name)
while True:
    print('for deposit d and for withdraw w and for exist e')
    option=input('choose your option')
    if option.lower()=='d':
        amount=float(input('enter the amount you want to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount = float(input('enter the amount you want to withdraw:'))
        c.withdraw(amount)

    elif option.lower()=='e':
        print('thanks for banking')
        break
    else:
        print('please enter valid option')
