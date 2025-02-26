def great(a,b,c,d,e):
    if a>b and a>c and a>d and a>e:
        return a
    elif b>c and b>d and b>e:
        return b
    elif c>d and c>e:
        return c
    elif d>e:
        return d
    else:
        return e

def main():
    
    a,b,c,d,e=12,13,17,16,9
    greatest=great(a,b,c,d,e)
    if greatest==a:
        sec_great=great(b,c,d,e)
    elif greatest==b:
        sec_great=great(a,c,d,e)
    elif greatest==c:
        sec_great=great(a,b,d,e)
    elif greatest==d:
        sec_great=great(a,b,c,e)
    else:
        sec_great=great(a,b,c,d)
    return sec_great


print("second greatest number is=",sec_great)        
        
