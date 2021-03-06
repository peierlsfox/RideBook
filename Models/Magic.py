class Magic():
    def __init__(self, name):
        self.name = name

    def setProperties(self, type,grade,desc,func,sourceHero,sourceType,learnAmount,learnHeros):
        self.type = type
        self.grade = grade
        self.description = desc
        self.func = func
        self.sourceHero = sourceHero
        self.sourceType = sourceType
        self.learnAmount = learnAmount
        self.learnHeros = learnHeros