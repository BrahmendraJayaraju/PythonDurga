#operator overloading

class book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self,other):
        totalpages=self.pages+other.pages
        return totalpages

b1=book(100)
b2=book(200)
print(b1+b2)

#b1->self
#b2->other