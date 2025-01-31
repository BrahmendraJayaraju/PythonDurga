try:
    print('try')
except:
    print('except')

else:
    try:
        print('inner try')
    finally:
        print('inner except')