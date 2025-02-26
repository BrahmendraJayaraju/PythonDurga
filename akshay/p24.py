for i in "hello world":
    if i==' ':
        break
    print(i)
print("#"*30)



i=0
while i<20:
    if i==10:
        break
    print(i)
    i=i+1
print("#"*30)




key='c'
flag=0
for i in {'a':1,'b':2,'c':3,'d':4}:
    if i==key:
        flag=1
        break
    
if flag==1:
     print("element found")
else:
     print("element not found")

print("#"*30)






i=0
while True:
    if i==10:
        break
    print(i)
    i=i+1

print("#"*30)




s="hello world"
key="w"
for i in range(len(s)):
    if s[i]==key:
        print(key,"found at position",i)
        break


    
    
