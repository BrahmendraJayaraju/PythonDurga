value=13
if value%2==0:
    if value%6==0:
        print("value is divisible by 6")
        value=value-5
    else:
        print("value is not divisible by 6")
        value=value+5
print(value)        
