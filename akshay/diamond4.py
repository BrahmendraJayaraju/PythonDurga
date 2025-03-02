def pattern(n):
    mid = (n // 2) + 1
    print(mid)
    for j in range(1, n + 1):

        if j <= mid:
            k = ord('A')+j-1
        else:
            k =  ord('A')+(n - j)



        for i in range(1, n + 1):
            if i > j and i + j > n + 1:
                print(chr(k), end=' ')
            else:
                print(' ', end=' ')


        for i in range(1, n + 1):
            if i <= j and i + j <= n + 1:
                print(chr(k), end=' ')
            else:
                print(' ', end=' ')

        print()


pattern(9)
