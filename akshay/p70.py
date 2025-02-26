def startswith(name,sub):
    for i in range(len(sub)):
        if name[i]!=sub[i]:
            return False
    return True
