from scipy.cluster.hierarchy import average


class test61:
    @staticmethod
    def average(list1):
        result=sum(list1)/len(list1)  # result is local variable 
        print('average is :', result)

list1=[1,2,3,4,5]
test61.average(list1)