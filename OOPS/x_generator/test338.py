def mygen():
    yield 'A'
    yield 'b'
    yield 'c'

g=mygen()

print(type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))