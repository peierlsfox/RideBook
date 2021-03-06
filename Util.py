class Util():
    def warpDragData(self, type='', team = '', memberSlot = '', magicSlot = '',name=''):
        result = '{}|{}|{}|{}|{}'.format(type,team,memberSlot,magicSlot,name)
        return result

    def unwarpDragData(self, data):
        return data.split('|')
