class test82:
    def m1(self):
        def calc(a,b):
            print('the sum:',a+b)
            print('the sum:', a * b)
            print('the sum:', a - b)
            print('the sum:', a + b/2)
            print()
        calc(10,2)
        calc(10, 200)
        calc(5, 200)

k=test82()
k.m1()
