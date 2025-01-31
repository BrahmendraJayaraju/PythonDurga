try:
    try:
        print('inner try')
    except:
        print('inner except')
    finally:
        print('inner finally')

except ZeroDivisionError:
    print('outer except')
