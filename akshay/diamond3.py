def pattern(n):

    for j in range(1,n+1):
        k =ord('A')+j-1



        for i in range(1,n+1):
            if i>j and i+j>n+1:
                print(chr(k),end=' ')
            else:
                print(' ',end=' ')



        k=ord('A')+j-1
        for i in range(1,n+1):
            if i<=j and i+j<=n+1:
                print(chr(k),end=' ')
            else:
                print(' ',end=' ')

        print()


pattern(9)