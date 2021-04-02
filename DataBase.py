import xlrd
import xlwt
from Models import Hero, Member, Magic, Book, Team
import threading

class DataBase():
    #创建单例时用的线程锁
    _instance_lock = threading.Lock()

    def __init__(self, file='data.xlsx') -> None:
        self.heros = []
        self.members = []
        self.magics = []
        self.books = []
        self.teams = []
        self.dataFile = xlrd.open_workbook(file)
        self.heroSheet = self.dataFile.sheet_by_name('武将数据')
        self.magicSheet = self.dataFile.sheet_by_name('战法数据')
        self.teamSheet = self.dataFile.sheet_by_name('队伍数据')
        self.prepareDB()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with DataBase._instance_lock:
                if not hasattr(cls, '_instance'):
                    DataBase._instance = super().__new__(cls)
        return DataBase._instance

    def prepareDB(self):
        #读取战法数据
        for i in range(2,self.magicSheet.nrows):
            magic = self.loadMagic(i)
            self.magics.append(magic)
        
        #读取武将数
        for i in range(2,self.heroSheet.nrows):
            hero = self.loadHero(i)
            self.heros.append(hero)

        for i in range(2,self.teamSheet.nrows):
            team = self.loadTeam(i)
            self.teams.append(team)

    def loadHero(self, index) -> Hero:
        name = self.heroSheet.cell(index,2).value
        grade = self.heroSheet.cell(index,20).value
        level = 50
        group = self.heroSheet.cell(index,1).value
        force = self.heroSheet.cell(index,3).value
        forceRate = self.heroSheet.cell(index,4).value
        command = self.heroSheet.cell(index,5).value
        commandRate = self.heroSheet.cell(index,6).value
        intelligence = self.heroSheet.cell(index,7).value
        intelligenceRate = self.heroSheet.cell(index,8).value
        speed = self.heroSheet.cell(index,9).value
        speedRate = self.heroSheet.cell(index,10).value
        charm = self.heroSheet.cell(index,11).value
        charmRate = self.heroSheet.cell(index,12).value
        politics = self.heroSheet.cell(index,13).value
        politicsRate = self.heroSheet.cell(index,14).value
        cavalry = self.heroSheet.cell(index,15).value
        bowman = self.heroSheet.cell(index,16).value
        pikeman = self.heroSheet.cell(index,17).value
        mauler = self.heroSheet.cell(index,18).value
        siege = self.heroSheet.cell(index,19).value
        growUp = self.heroSheet.cell(index,22).value
        magicNameSelf = self.heroSheet.cell(index,23).value
        magicSelf = self.getMagicByName(magicNameSelf)
        magicNameTrans = self.heroSheet.cell(index,21).value
        magicTrans = self.getMagicByName(magicNameTrans)
        hero = Hero(name)
        hero.setPropertys(name,grade,level,group,force,forceRate,command,commandRate,intelligence,intelligenceRate,speed,speedRate,charm,charmRate,politics,politicsRate,cavalry,bowman,pikeman,mauler,siege,growUp,magicSelf, magicTrans)
        return hero

    #读取战法的数据，并创建战法
    def loadMagic(self, index):
        name = self.magicSheet.cell(index,4).value
        grade = self.magicSheet.cell(index,3).value
        desc = self.magicSheet.cell(index,6).value
        type = self.magicSheet.cell(index,1).value
        sourceType = self.magicSheet.cell(index,9).value
        sourceHero = self.magicSheet.cell(index,5).value
        learnCount = self.magicSheet.cell(index,8).value
        magic = Magic()
        magic.setPropertys(name,grade,desc,type,sourceType,sourceHero,learnCount)
        return magic

    def loadTeam(self, index):
        member1 = self.loadMember(index,1)
        member2 = self.loadMember(index,2)
        member3 = self.loadMember(index,3)
        type = self.teamSheet.cell(index,1).value
        team = Team(index-1,type,member1,member2,member3)
        return team

    def loadMember(self, index, position) -> Member:
        offset = (position-1)*6
        heroName = self.teamSheet.cell(index,offset+2).value
        hero = self.getHeroByName(heroName)
        magic2Name = self.teamSheet.cell(index,offset+3).value
        magic2 = self.getMagicByName(magic2Name)
        magic3Name = self.teamSheet.cell(index,offset+4).value
        magic3 = self.getMagicByName(magic3Name)
        member = Member('{}.{}'.format(index-1,position),position)
        member.setProperties(hero,magic2,magic3)
        return member

    def getMagicByName(self,name) -> Magic:
        for magic in self.magics:
            if magic.name == name:
                return magic
        return None

    def getHeroByName(self,name) -> Hero:
        for hero in self.heros:
            if hero.name == name:
                return hero
        return None
    
    def getTeamById(self, id) -> Team:
        for team in self.teams:
            if team.id == id:
                return team
        return None
    
    def exportMagicsToTable(self):
        datas = []
        for magic in self.magics:
            dataRow = magic.exportRow()
            datas.append(dataRow)
        return Magic.exportHeader,datas

    def exportHerosToTable(self):
        datas = []
        for hero in self.heros:
            dataRow = hero.exportRow()
            datas.append(dataRow)
        return Hero.exportHeader,datas

def createDB(arg):
    obj = DataBase()
    print(obj)

if __name__=='__main__':
    db = DataBase()
    db.prepareDB()
    for i in range(10):
        t = threading.Thread(target=createDB,args=[i,])
        t.start()

