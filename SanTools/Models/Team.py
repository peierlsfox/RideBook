
class Team():
    def __init__(self, name):
        self.name = name
        self.members = []

    def setProperties(self, type = '骑', desc = '无描述', members = []):
        self.type = type
        self.description = desc
        self.members.extend(members)
