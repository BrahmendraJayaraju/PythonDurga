def lower(s):
    temp=""
    for i in s:
      if  ord(i) in range(ord('A'),ord('Z')+1):
            temp=temp+chr(ord(i)+32)
      else:
           temp=temp+i
    return temp


