#exception


print('statement 1')
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
    print('statement 3')
