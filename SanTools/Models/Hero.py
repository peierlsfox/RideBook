from Models.Magic import Magic

class Hero():
    def __init__(self, name):
        self.name = name

    def setProperties(self,group:str,force:float, forceRate:float,command:float, commandRate:float,intelligence:float, intelligenceRate:float,speed:float,speedRate:float,charm:float,charmRate: float,politics:float,politicsRate:float, grade:str, cavalry:str, bowman:str, pikeman:str,mauler:str,siege:str,growUp:bool,magicSelf:Magic,magicTrans:Magic,level:int = 50):
        #阵营
        self.group = group 
        #武力及成长率
        self.force = force 
        self.forceRate = forceRate
        #统率及成长率
        self.command = command 
        self.commandRate = commandRate
        #智力及成长率
        self.intelligence = intelligence 
        self.intelligenceRate = intelligenceRate
        #速度及成长率
        self.speed = speed 
        self.speedRate = speedRate
        #魅力及成长率
        self.charm = charm
        self.charmRate = charmRate
        # 政治及成长率
        self.politics = politics
        self.politicsRate = politicsRate
        #武将品阶 S A B C
        self.grade = grade        
        #兵种适性 骑兵 弓兵 枪兵 盾兵 攻城车
        self.cavalry = cavalry
        self.bowman = bowman
        self.pikeman = pikeman
        self.mauler = mauler
        self.siege = siege
        #觉醒
        self.growUp = growUp
        #自带战法
        self.magicSelf = magicSelf
        #传承战法
        self.magicTrans = magicTrans

        #等级 1-50
        self.level = level