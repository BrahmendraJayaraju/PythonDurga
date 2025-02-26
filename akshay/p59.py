def countnosubch(name,key):
    count=0
    for i in name:
        if i==key:
            count=count+1
    return count

c1=count('hello world','w')
print(c1)


