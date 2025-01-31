#how to print exception information on console

try:
    print(10/0)
except ZeroDivisionError as msg:
    print('exception type:',type(msg))
    print('exception  type:',msg.__class__)
    print('exception class name:',msg.__class__.__name__)
    print('exception message:',msg)