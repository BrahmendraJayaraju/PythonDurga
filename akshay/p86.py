def pattern9(n):
    for j in range(1,n+1):
        k=1
        for i in range(1,n+1):
            if i>=j:
                print(k,end=' ')
                k=k+1
            else:
                print(' ',end=' ')
        print()
        
                
