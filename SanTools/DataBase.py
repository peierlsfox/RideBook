import xlrd
from Models.Hero import Hero
from Models.Magic import Magic
from Models.Team import Team
from Models.Member import Member

class DataBase():
    def __init__(self, dataFile = 'sandata.xls'):
        self.heros = []
        self.magics = []
        self.teams = []
        self.workbook = xlrd.open_workbook(dataFile)
        self.heroSheet = self.workbook.sheet_by_name('武将数据')
        self.magicSheet = self.workbook.sheet_by_name('战法数据')
        self.teamSheet = self.workbook.sheet_by_name('队伍数据')
        
        self.loadMagics()
        self.loadHeros()
        self.loadTeams()
        
    def loadHeros(self):
        for i in range(2,self.heroSheet.nrows):
            name = self.heroSheet.cell(i,2).value
            group = self.heroSheet.cell(i,1).value
            force = self.heroSheet.cell(i,3).value
            forceRate = self.heroSheet.cell(i,4).value
            command = self.heroSheet.cell(i,5).value
            commandRate = self.heroSheet.cell(i,6).value
            intelligence = self.heroSheet.cell(i,7).value
            intelligenceRate = self.heroSheet.cell(i,8).value
            speed = self.heroSheet.cell(i,9).value
            speedRate = self.heroSheet.cell(i,10).value
            charm = self.heroSheet.cell(i,11).value
            charmRate = self.heroSheet.cell(i,12).value
            politics = self.heroSheet.cell(i,13).value
            politicsRate = self.heroSheet.cell(i,14).value
            grade = self.heroSheet.cell(i,20).value
            cavalry = self.heroSheet.cell(i,15).value
            bowman = self.heroSheet.cell(i,16).value
            pikeman = self.heroSheet.cell(i,17).value
            mauler = self.heroSheet.cell(i,18).value
            siege = self.heroSheet.cell(i,19).value
            growUp = self.heroSheet.cell(i,22).value
            magicNameSelf = self.heroSheet.cell(i,21).value
            magicSelf = self.getMagicByName(magicNameSelf)
            magicNameTrans = self.heroSheet.cell(i,23).value
            magicTrans = self.getMagicByName(magicNameTrans)
            level = self.heroSheet.cell(i,39).value
            hero = Hero(name)
            hero.setProperties(group,force, forceRate,command, commandRate,intelligence,intelligenceRate,speed,speedRate,charm,charmRate,politics,politicsRate, grade, cavalry, bowman, pikeman,mauler,siege,growUp,magicSelf,magicTrans,level)
            self.heros.append(hero)
    
    def loadMagics(self):
        for i in range(2,self.magicSheet.nrows):
            name = self.magicSheet.cell(i,4).value
            type = self.magicSheet.cell(i,1).value
            grade = self.magicSheet.cell(i,3).value
            desc = self.magicSheet.cell(i,6).value
            func = self.magicSheet.cell(i,2).value
            sourceHero = self.magicSheet.cell(i,5).value
            sourceType = self.magicSheet.cell(i,9).value
            learnAmount = self.magicSheet.cell(i,8).value
            learnHeros = self.magicSheet.cell(i,7).value

            magic = Magic(name)
            magic.setProperties(type,grade,desc,func,sourceHero,sourceType,learnAmount,learnHeros)
            self.magics.append(magic)

    def loadTeams(self):
        for i in range(2,self.teamSheet.nrows):
            name = self.teamSheet.cell(i,1).value
            type = self.teamSheet.cell(i,1).value
            desc = self.teamSheet.cell(i,1).value
            team = Team(name)
            self.teams.append(team)

    def getMagicByName(self, name):
        for magic in self.magics:
            if name == magic.name:
                return magic
        print('战法清单中未找到\"{}\"！'.format(name))
        return None

    def getHeroByName(self, name):
        for hero in self.heros:
            if name == hero.name:
                return hero
        print('武将清单中未找到\"{}\"！'.format(name))
        return None