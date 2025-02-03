import inspect


def getinfo():
    #print(inspect.stack()[1])
    #print(inspect.stack()[1][1])  #gives  caller module name
    #print(inspect.stack()[1][2])   #caller function name  #getinfo is in line 5
    print(inspect.stack()[1][3])  #gives function name