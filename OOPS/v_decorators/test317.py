#to prove function is also object and address is same
def wish(name):
    print('hello',name)



greeting=wish

print(id(wish))
print(id(greeting))


wish('brahmendra')
greeting('brahmendra')

del wish
greeting('brahmendra')