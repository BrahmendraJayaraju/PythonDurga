def vowelscount(s):
    s=s.lower()
    count=0
    for i in s:
        if i in 'aeiou':
            count=count+1
    return count


def conscount(s):
    s=s.lower()
    count=0
    for i in s:
        if i.isalpha() and i not in 'aeiou':
            count=count+1
    return count




    

