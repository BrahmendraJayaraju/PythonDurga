class movie:
    def __init__(self,moviename,hero,heroine):
        self.movie=moviename
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print('movie name is ',self.movie)
        print('movie hero is:',self.hero)
        print('movie heroine is:',self.heroine)


listmovie=[]


while True:
    moviename=input('enter the movie name;')
    hero=input('enter the hero name:')
    heroine=input('enter the heroine name: ')
    m=movie(moviename,hero,heroine)
    listmovie.append(m)
    print('movie added successfully')
    option=input('do you want to continue :')
    if option.lower()=='no':
        break
print('print all the movie details \n')
for m in listmovie:
    m.info()
    print()
