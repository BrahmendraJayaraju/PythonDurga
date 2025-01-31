#take user input @,&,*

try:
    x=int(input('print the 1st number:'))
    y=int(input('print the 2nd number:'))
    print('the result is:',x/y)
except ZeroDivisionError as msg:
      print('description:',msg)

except ValueError as msg:
      print('description:',msg)