def pattern(n):
    mid = (n // 2) + 1
    print(mid)
    for j in range(1, n + 1):

        if j <= mid:
            k = j
        else:
            k = n - j + 1



        for i in range(1, n + 1):
            if i > j and i + j > n + 1:
                print(k, end=' ')
            else:
                print(' ', end=' ')


        for i in range(1, n + 1):
            if i <= j and i + j <= n + 1:
                print(k, end=' ')
            else:
                print(' ', end=' ')

        print()


pattern(9)
