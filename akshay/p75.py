def upper(s):
    temp=""
    for i in s:
      if  ord(i) in range(ord('a'),ord('z')+1):
            temp=temp+chr(ord(i)-32)
      else:
          temp=temp+i
    return temp
