#to execute java file and clear the screen
#not working 
import os,time

print('execute java program: first compile ')
os.system('Javac /Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/apple.java')
print('java program executed')
os.system('Java /Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/apple')


print('clear screen after 7 seconds ')
time.sleep(7)
os.system('clear')
print('cleared by brahmendra')