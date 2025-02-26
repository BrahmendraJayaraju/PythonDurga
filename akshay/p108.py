n=5
k=1
for j in range(1,n+1):
    L=k+j-1
    for i in range(1,n+1):
        if i<=j:
            if j%2!=0:
               print(k,end=' ') 
            else:
               print(L,end=' ')
               L=L-1
            k=k+1
        else:
            print(' ',end=' ')
    print()        
