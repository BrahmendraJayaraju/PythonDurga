class sportsnews:
    def sportsinfo(self):
        print('sports info 1')
        print('sports info 2')
        print('sports info 3')
        print('sports info 4')

class movienews:
    def movieinfo(self):
        print('movie info 1')
        print('movie info 2')
        print('movie info 3')
        print('movie info 4')

class politicsnews:
    def politicsinfo(self):
        print('politics info 1')
        print('politics info 2')
        print('politics info 3')
        print('politics info 4')


class news:
    def __init__(self):
        self.sports=sportsnews()
        self.movies=movienews()
        self.politics=politicsnews()

    def gettotalnews(self):
        print('welcome to my news channel')
        self.sports.sportsinfo()
        self.movies.movieinfo()
        self.politics.politicsinfo()


n=news()
n.gettotalnews()

