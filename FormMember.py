from PyQt5.QtWidgets import QWidget
from Ui.Ui_Member import Ui_FormMember
from Models.Hero import Hero
from Models.Magic import Magic
from Models.Team import Team
from Models.Member import Member

class FormMember(QWidget,Ui_FormMember):
    def __init__(self, parent = None, member:Member = None, address = 1):
        super().__init__(parent)
        super().setupUi(self)

        self.setMember(member)
        self.setAddress(address)

    def updateUi(self):
        if self.member:
            if self.member.hero:
                self.labelHeroName.setText(self.member.hero.name)
                self.labelMagic1.setText(self.member.hero.magicSelf.name)
            if self.member.magic2:
                self.labelMagic2.setText(self.member.magic2.name)
            if self.member.magic3:
                self.labelMagic3.setText(self.member.magic3.name)
                
                
    def setMember(self, member:Member):
        self.member = member
        self.labelHeroName.setType('hero')
        self.labelMagic2.setType('magic')
        self.labelMagic3.setType('magic')
        self.updateUi()

    def setAddress(self,addr):
        self.address = addr
        self.labelHeroName.setAddress('{}.{}'.format(self.address,'h'))
        self.labelMagic2.setAddress('{}.{}'.format(self.address,2))
        self.labelMagic3.setAddress('{}.{}'.format(self.address,3))