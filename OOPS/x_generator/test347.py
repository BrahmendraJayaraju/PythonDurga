#convert generator object to list

def firstnnumbers(n):
    i=1
    while i<=n:
        yield i
        i=i+1


g=firstnnumbers(5)

l=list(g)

print(l)