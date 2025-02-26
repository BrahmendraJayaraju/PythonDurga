def may(n):
    print(n,end=" ")
    if n==0:
        return
    may(n-1)
    print(n,end=" ")
