def palcheck(str):
    n=len(str)
    print(n)
    end=round(n//2)
    print(end)

    for i in range(0,end):

        if str[i]==str[len(str)-1-i]:
            print(i,str[i])
        else:
            return False
    return True

if palcheck('madam'):
    print('palindeome')
else:
    print('not palindeome')
