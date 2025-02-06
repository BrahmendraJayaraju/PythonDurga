#to execute java file and clear the screen
#not working 
import os,time

print('execute java program: first compile ')
c='Javac apple.java'
os.system(c)
print('java program executed')
os.system('Java apple')


print('clear screen after 7 seconds ')
time.sleep(7)
os.system('clear')
print('cleared by brahmendra')