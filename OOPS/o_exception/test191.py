#case 3
#if exception raised but not handled

try:
    print('try block')
    print(10/0)

except ValueError:
    print('except block ')

finally:
    print('finally block ')