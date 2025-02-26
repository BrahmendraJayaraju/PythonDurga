def count(name,key,start=0,end=0):
    if end==0:
        end=len(name)
    count=0
    for i in range(start,end):
        if name[i]==key:
            count=count+1
    return count

c1=count('hello world','ld')
print(c1)
