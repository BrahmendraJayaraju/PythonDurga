class human:
    def __init__(self,name):
        self.name=name
        self.head=self.head() # creating object of head ,it calss head class constructor

    def info(self):
        print('helo myself',self.name)
        print('i am still busy with ')
        self.head.talk()
        self.head.brain.thinking()

    class head:
        def __init__(self):
            self.brain=self.brain()

        def talk(self):
            print('talking')

        class brain:
            def thinking(self):
                print('thinking')

a=human('brahmendra')
a.info()
