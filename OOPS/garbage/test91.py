class test91:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')


t=test91()
t=None
print('end of application')
print(t)
