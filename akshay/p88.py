def pattern11(n):
    for j in range(1,n+1):
        k=j
        for i in range(1,n+1):
            if i<=j:
                print(k,end=' ')
            else:
                print(' ',end=' ')
        print()        


pattern11(5)