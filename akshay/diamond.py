def pattern(n):

    for j in range(1,n+1):
        k = j



        for i in range(1,n+1):
            if i>j and i+j>n+1:
                print(k,end=' ')
            else:
                print(' ',end=' ')



        k=j
        for i in range(1,n+1):
            if i<=j and i+j<=n+1:
                print(k,end=' ')
            else:
                print(' ',end=' ')

        print()


pattern(9)