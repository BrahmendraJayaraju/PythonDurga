#exception raised and handled
#case 2
try:
    print('try block')
    print(10/0)

except ZeroDivisionError:
    print('except block ')

finally:
    print('finally block ')
