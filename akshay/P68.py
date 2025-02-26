def title(s):
    temp=""
    for i in range(len(s)):
        if i==0 and ord(s[i] in range(ord('a'),ord('z')+1)):
                       temp=temp+chr(ord(s[i])-32)

        elif i!=0 and s[i-1]==" "and ord(s[i]) in range(ord('a'),ord('z')+1):
                     temp=temp+chr(ord(s[i])-32)
                                         
        elif i!=0 and s[i-1]!=" "and ord(s[i]) in range(ord('a'),ord('z')+1):
                     temp=temp+chr(ord(s[i])-32)

        else:
            temp=temp+s[i]
        return temp




s=input("enter the string")
titlestring=title(s)
print("title string is ",titlestring)
                                         
                                         
                                         
