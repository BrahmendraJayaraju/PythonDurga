class professor:
    pass

class department1:
    def __init__(self,prof):
        self.prof=prof

p=professor()
csdept=department1(p)
ecdept=department1(p)