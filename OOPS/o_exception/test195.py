

try:
    print('outer try block')
    print(10 / 0)

    try:
        print('inner try block')


    except ZeroDivisionError:
        print('inner except block')

    finally:
        print('inner finally block')

except:
    print('outer except block')

finally:
    print('outer finally block')