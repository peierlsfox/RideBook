import xlrd
import xlwt
from Models import Hero, Member, Magic, Book
import threading
from DataBase import DataBase

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
    
    def change(self, fromAddr,fromContent, toAddr,toContent):
        print('server got command: from {}:{} to {}:{}'.format(fromAddr,fromContent,toAddr,toContent))
        # if fromAddr == 'lib':
        #     if toHasItem():
        #         itemOutLib()
        #         teamChange(to)
        #         itemInLib()
        #     else:
        #         itemOutLib()
        #         teamAdd
        # else:
        #     if toAddr is Team:
        #         teamExchange(from,to)
        #     else:
        #         teamRemove(from)
        #         itemInLib()


