#to avoid error in 338

def mygen():
    yield 'A'
    yield 'b'
    yield 'c'

g=mygen()


for i in g:
    print(i)