#to generate first n numbers

def first_n_numbers(n):
    i=1
    while i<=n:
        yield i
        i=i+1

g=first_n_numbers(10)

for x in g:
    print(x)