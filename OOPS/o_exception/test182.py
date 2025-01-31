
#take user input

try:
    x=int(input('print the 1st number:'))
    y=int(input('print the 2nd number:'))
    print('the result is:',x/y)
except ZeroDivisionError as msg:
    print('exception type:',type(msg))
    print('exception  type:',msg.__class__)
    print('exception class name:',msg.__class__.__name__)
    print('exception message:',msg)