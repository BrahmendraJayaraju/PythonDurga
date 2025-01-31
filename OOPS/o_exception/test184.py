
try:
     print(10/0)

     #top to bottom
except ZeroDivisionError as msg:
      print('description 1:',msg)

except ArithmeticError as msg:
      print('description 2:',msg)