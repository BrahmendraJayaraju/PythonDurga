def pattern8(n):
    for j in range(1,n+1):
        k=ord('A')
        for i in range(1,n+1):
            if i<=j:
                print(chr(k),end=' ')
                k=k+1
            else:
                print(' ',end=' ')
        print()
        
                
