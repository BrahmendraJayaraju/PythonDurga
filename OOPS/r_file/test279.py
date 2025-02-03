#seek and tell 
f=open('/Users/brahmendrajayaraju/PycharmProjects/PythonDurga/files/test279.txt', 'r')


print(f.tell())   #0 index
f.seek(3)  #now curson moves to 3rd index

print(f.tell())  #now cursor is at  3

print(f.read(3))  #from index 3 , read next 3 char  (it includes \n also)

f.seek(20)  #move to 20 position

print(f.tell())   #20
print(f.read())  #after going to 20 read

f.seek(0)  #come back to 0 position
print('...................')
print(f.read())