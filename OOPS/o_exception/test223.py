class tooyoungexception(Exception):

    def __init__(self,msg):
        self.msg=msg


raise  tooyoungexception('plz wait some more time')