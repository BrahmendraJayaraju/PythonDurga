def komugi(n):
    for j in range(1,n+1):
        k=ord('A')+n-j
        for i in range(1,n+1):
            if i>=j:
                print(chr(k),end=' ')
                k=k-1
            else:
                print(' ',end=' ')
        print()            
                
komugi(5)