def remove(s):
    temp=""
    for i in s:
        if i not in temp:
           temp=temp+i
    return temp    
