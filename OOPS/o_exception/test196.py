from scipy.constants import value

try:
    print('stat 1')
    print('stat 2')
    print('stat 3')
    try:
       print('stat 4')
       print('stat 5')
       print('stat 6')

    except ZeroDivisionError:
        print('stat 7')

    finally:
        print('statement 8')

    print('statement 9')
except ValueError:
    print('stat 10')

finally:
    print('stat 11')

print('stat 12')
