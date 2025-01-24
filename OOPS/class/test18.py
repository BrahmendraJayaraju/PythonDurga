class student18:

    @classmethod
    def m1(cls):
        print('address of the cls is :',id(cls))

#both cls and student18 address is same 
print('address of the object :',id(student18()))