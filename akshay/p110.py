def vowelandcons(s):
    s=s.lower()
    vc=0
    cc=0
    for i in s:
        if ord(i) in range(ord('a'),ord('z')+1):
            if i in 'aeiou':
                vc=vc+1
            else:
                cc=cc+1
    return vc,cc
