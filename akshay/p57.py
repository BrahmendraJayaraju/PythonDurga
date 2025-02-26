def count_digits(num,key):
    count=0
    while num!=0:
        r=num%10
        num=num//10
        if r==key:
         count=count+1
    return count    
