class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        print('add method executed')
        return book(self.pages+other.pages)


    def __str__(self):
        print('string method executed')
        return 'the total pages is:{}'.format(self.pages)

    def __mul__(self,other):
        print('mul is executed')
        return book(self.pages*other.pages)

b1=book(1)
b2=book(2)
b3=book(5)
b4=book(6)

#print(b1+b2*b3+b4)
print(b1*b2+b3*b4)
