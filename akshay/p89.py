def pattern12(n):
    for j in range(1,n+1):
        k=ord('A')+j-1
        for i in range(1,n+1):
            if i<=j:
                print(chr(k),end=' ')
            else:
                print(' ',end=' ')
        print()        
pattern12(5)