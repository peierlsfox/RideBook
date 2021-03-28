import threading

class CommandServer():

    _instance_lock = threading.Lock()

    def __new__(cls):
        if not hasattr(CommandServer, '_instance'):
            with CommandServer._instance_lock:
                if not hasattr(CommandServer,'_instance'):
                    CommandServer._instance = object.__new__(cls)
        return CommandServer._instance

    def __init__(self):
        pass

    def paser(self, argv):
        pass

    def changeTeamMember(self, team,position,member):
        pass
    def changeTeamAttr(self, team, attrs):
        pass
    def addTeamMember(self, team,position,member):
        pass
    def removeTeamMember(self,team,position):
        pass
    
    def changeMemberMagic(self,member,position,magic):
        pass
    def addMemberMagic(self,member,position,magic):
        pass
    def removeMemberMagic(self,member,position):
        pass
    