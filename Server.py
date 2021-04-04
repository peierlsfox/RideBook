import xlrd
import xlwt
from Models import Hero, Member, Magic, Book
import threading
from DataBase import DataBase
from SanHelp import SanHelp

class Server():
    #创建单例时用的线程锁
    _instance_lock = threading.Lock()

    def __init__(self):
        self.DB = DataBase()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with Server._instance_lock:
                if not hasattr(cls, '_instance'):
                    Server._instance = super().__new__(cls)
        return Server._instance
    
    def change(self, type, fromAddr,fromContent, toAddr,toContent):
        print('server got command: from {}:{} to {}:{}'.format(fromAddr,fromContent,toAddr,toContent))

        if SanHelp.LibAddress in fromAddr:
            if toContent:
                if type == SanHelp.HeroType: #用库里的武将替代队伍中的武将
                    hero = self.DB.getHeroByName(fromContent)
                    teamId, memberId, position = toAddr.split('.')
                    team = self.DB.getTeamById(teamId)
                    member = team.getMember(memberId)

                    member.toLib()

                    newMember = Member(teamId,memberId)
                    newMember.setHero(hero)
                    member = newMember
                if type == SanHelp.MagicType:
                    magic = self.DB.getMagicByName(fromContent)
                    teamId, memberId, position = toAddr.split('.')
                    team = self.DB.getTeamById(teamId)
                    member = team.getMember(memberId)

                    if position == '2':
                        if member.magic2:
                            member.magic2.setIsAttached(False)
                        member.setMagic2(magic)
                        magic.setIsAttached(True)
                    if position == '3':
                        if member.magic3:
                            member.magic3.setIsAttached(False)
                        member.setMagic3(magic)
                        magic.setIsAttached((True))
            # else:
        #         itemOutLib()
        #         teamAdd
        # else:
        #     if toAddr is Team:
        #         teamExchange(from,to)
        #     else:
        #         teamRemove(from)
        #         itemInLib()


