def returnduplicate(s):
    temp=""
    dup=""
    for i in s:
        if i not in temp:
            temp=temp+i
        else:
            dup=dup+i
    return dup
    
