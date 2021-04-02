from PyQt5.QtWidgets import QWidget
from Ui.Ui_Member import Ui_FormMember
from SanHelp import SanHelp
from Models import *

class FormMember(QWidget,Ui_FormMember):
    def __init__(self, withinView) -> None:
        super(FormMember,self).__init__(withinView)
        self.setupUi(self)
        self.labelHeroName.setType(SanHelp.HeroType)
        self.labelMagic2.setType(SanHelp.MagicType)
        self.labelMagic3.setType(SanHelp.MagicType)

    def setPosition(self,position):
        self.labelMemberPosition.setText(position)

    def setAddress(self, addr):
        self.address = addr
        self.labelHeroName.setAddress('{}.{}'.format(addr,'hero'))
        self.labelMagic2.setAddress('{}.{}'.format(addr,2))
        self.labelMagic3.setAddress('{}.{}'.format(addr,3))

    def setMember(self, member:Member): 
        if member.hero:
            self.labelHeroName.setText(member.hero.name)
            self.labelMagic1.setText(member.hero.magicSelf.name)
        else:
            self.labelHeroName.setText('')
            self.labelMagic1.setText('')
        if member.magic2:
            self.labelMagic2.setText(member.magic2.name)
        else:
            self.labelMagic2.setText('')
        if member.magic3:
            self.labelMagic3.setText(member.magic3.name)
        else:
            self.labelMagic3.setText('')

        