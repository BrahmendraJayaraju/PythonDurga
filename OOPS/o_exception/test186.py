#single except to handle multiple exceptions

try:
    x=int(input('enter the first number:'))
    y=int(input('enter the second  number:'))
    print('the result:',x/y)
except(ZeroDivisionError,ValueError) as a:  # vimp msg
    #(ZeroDivisionError,ValueError) we can use only this also 
    print('exception type:', type(a))
    print('exception  type:', a.__class__)
    print('exception class name:', a.__class__.__name__)
    print('exception message:', a)



