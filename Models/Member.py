
from Models.Hero import Hero
from Models.Magic import Magic
from Models.Team import Team

class Member():
    #member name is team.name
    def __init__(self, name):
        self.name = name

    def setProperties(self,hero:Hero,magic2:Magic,magic3:Magic):
        self.hero = hero
        self.magic2 = magic2
        self.magic3 = magic3
        