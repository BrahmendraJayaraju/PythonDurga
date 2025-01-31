class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):
        return book(self.pages+other.pages)

b1=book(100)
b2=book(200)
b3=book(300)

#we get object
print(b1+b2)

#object +object
print(b1+b2+b3)