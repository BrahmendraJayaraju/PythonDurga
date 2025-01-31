#except block at the end always
#it handles all exceptions

try:
    x = int(input('enter the first number:'))
    y = int(input('enter the second  number:'))
    print('the result:', x / y)

except ZeroDivisionError:
    print('zer division error')

#this should be always at end , it can handle anything 
except:
    print('it will handle any kind of exception ')