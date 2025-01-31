class sportsnews:
    def sportsinfo1(self):
        print('sports info 1')
        print('sports info 2')
        print('sports info 3')
        print('sports info 4')

class movienews:
    def movieinfo1(self):
        print('movie info 1')
        print('movie info 2')
        print('movie info 3')
        print('movie info 4')

class politicsnews:
    def politicsinfo1(self):
        print('politics info 1')
        print('politics info 2')
        print('politics info 3')
        print('politics info 4')


class newschannel:

    def __init__(self,sportsnews,movienews,politicsnews):
        self.sports=sportsnews
        self.movies=movienews
        self.politics=politicsnews

    def gettotalnews1(self):
        print('welcome to my news channel')
        self.sports.sportsinfo1()
        self.movies.movieinfo1()
        self.politics.politicsinfo1()


n=newschannel(sportsnews(),movienews(),politicsnews())  #sending ref variables 
n.gettotalnews1()