class test89:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')


t=test89()
del t
print('end of app ')