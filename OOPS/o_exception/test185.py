#check the  exception diagram

try:
     print(10/0)

    #top to bottom
except ArithmeticError as msg:  #this line imp 
      print('description 1:',msg)

except ZeroDivisionError as msg:
      print('description 2:',msg)
