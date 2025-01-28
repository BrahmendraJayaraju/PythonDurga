class test62:
    @staticmethod
    def average(list1):
        result = sum(list1) / len(list1)  # result is local variable
        print('average is :', result)

    @staticmethod
    def wish(name):
        for i in range(4):      # i is local variable
            print('your',name)

list1 = [1, 2, 3, 4, 5]
test62.average(list1)
test62.wish('brahmendra')