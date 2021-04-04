class Magic():
    exportHeader =  ['战法','品级','类型','描述']
    def __init__(self,name = '新战法'):
        self.name = name #名称
        self.grade = '' #品阶 S/A/B/C
        self.description = '' #描述
        self.type = '' #类型 被动、主动、指挥、兵种、突击、阵法
        self.sourceType = '' #来源 自带、传承、事件
        self.sourceHero = [] #源武将
        self.learnCount = 0 #学习次数
        
        self.isAttached = False #是否配置给武将

    def setPropertys(self,name,grade,desc,type,sourceType,sourceHero,learnCount):
        self.name = name
        self.grade = grade
        self.description=desc
        self.type =type
        self.sourceType = sourceType
        self.sourceHero = sourceHero
        self.learnCount = learnCount

    def setIsAttached(self, isAttached):
        self.isAttached = isAttached

    def exportRow(self): #['战法','品级','类型','描述']
        return [self.name,self.grade,self.type,self.description]
    

# 武将
class Hero():
    exportHeader = ['武将','品级','国家','骑','盾','弓','枪','械','战法']
    def __init__(self, name = '新武将'):
        self.name = '' #姓名
        self.grade = '' #武将品阶 S/A/B/C
        self.level = 0 #等级 1-50
        self.group = '' #阵营
        self.force = 0.0
        self.forceRate = 0.0 #武力及成长率
        self.command = 0.0
        self.commandRate = 0.0 #统率及成长率
        self.intelligence = 0.0
        self.intelligenceRate = 0.0 #智力及成长率
        self.speed = 0.0
        self.speedRate = 0.0 #速度及成长率
        self.charm = 0.0
        self.charmRate = 0.0 #魅力及成长率
        self.politics = 0.0
        self.politicsRate = 0.0 #政治及成长率
        self.cavalry = '' #骑兵
        self.bowman = '' #弓兵
        self.pikeman = '' #枪兵
        self.mauler = '' #盾兵
        self.siege = '' #攻城车
        self.growUp = True #觉醒
        self.magicSelf = Magic() #自带战法
        self.magicTrans = Magic() #传承战法

        self.inTeam = False #是否配置到队伍中

    def setPropertys(self,name,grade,level,group,force = 0.0,forceRate = 0.0,command = 0.0,commandRate = 0.0,intelligence = 0.0,intelligenceRate = 0.0,speed = 0.0,speedRate = 0.0,charm = 0.0,charmRate = 0.0,politics = 0.0,politicsRate = 0.0,cavalry = '',bowman = '',pikeman = '',mauler = '',siege = '',growUp = True,magicSelf = None, magicTrans = None):
        self.name = name
        self.grade = grade #武将品阶 S/A/B/C
        self.level = level #等级 1-50
        self.group = group #阵营
        self.force = force
        self.forceRate = forceRate #武力及成长率
        self.command = command
        self.commandRate = commandRate #统率及成长率
        self.intelligence = intelligence
        self.intelligenceRate = intelligenceRate #智力及成长率
        self.speed = speed
        self.speedRate = speedRate #速度及成长率
        self.charm = charm
        self.charmRate = charmRate #魅力及成长率
        self.politics = politics
        self.politicsRate = politicsRate#政治及成长率
        self.cavalry = cavalry #骑兵
        self.bowman = bowman #弓兵
        self.pikeman = pikeman #枪兵
        self.mauler = mauler #盾兵
        self.siege = siege #攻城车
        self.growUp = growUp #觉醒
        self.magicSelf = magicSelf #自带战法
        self.magicTrans = magicTrans #传承战法

    def setInTeam(self, inTeam):
        self.inTeam = inTeam

    def exportRow(self): #['武将','品级','国家','骑','盾','弓','枪','械','战法']
        return [self.name,self.grade,self.group,self.cavalry,self.mauler,self.bowman,self.pikeman,self.siege,self.magicSelf.name]

class Book():
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Member():
    def __init__(self, id, position):
        self.id = id
        self.position = position #1/2/3
        self.hero = None
        self.magic1 = None
        self.magic2 = None
        self.magic3 = None
        self.book1 = None
        self.book2 = None
        self.book3 = None

    def setProperties(self,hero:Hero, magic2 = None , magic3 = None, book1 = None, book2 = None, book3 = None):
        self.hero = hero
        if hero:
            self.magic1 = hero.magicSelf
        self.magic2 = magic2
        self.magic3 = magic3
        self.book1 = book1
        self.book2 = book2
        self.book3 = book3

    def setHero(self, hero):
        self.hero = hero
        if hero:
            self.magic1 = hero.magicSelf

    def setMagic2(self, magic):
        self.magic2 = magic

    def setMagic3(self, magic):
        self.magic3 = magic

    def toLib(self):
        if self.magic2:
            self.magic2.setIsAttached(False)
            self.magic2 = None

        if self.magic3:
            self.magic3.setIsAttached(False)
            self.magic3 = None

        if self.hero:
            self.magic1 = None
            self.hero.setInTeam(False)
            self.hero = None

class Team():
    def __init__(self, id, type = '骑', member1 = None, member2 = None, member3 = None) -> None:
        self.id = id
        self.type = type #骑、弓、枪、盾、械
        self.member1 = member1
        self.member2 = member2
        self.member3 = member3

    def getMember(self, id) -> Member :
        if id == '1':
            return self.member1
        if id == '2':
            return self.member2
        if id == '3':
            return self.member3
        return None
