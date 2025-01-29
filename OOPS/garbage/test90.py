class test90:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')


t=test90()
del t
print('end of app ')
print(t)