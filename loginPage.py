import time
from base import base
class loginPage(base):
    #查找登录名位置
    def username(self):
        return self.by_id('nloginname')
    #查找密码位置
    def psd(self):
        return self.by_id('npwd')
    #查找登录按钮位置
    def btn(self):
        return self.by_id('nsubmit')
    #登录
    def LoginIn(self,username,psd):
        self.username().send_keys(username)
        self.psd().send_keys(psd)
        self.btn().click()
        time.sleep(3)
        return self.dr_url()


'''        
        lo=loginPage(self.driver)
        l=lo.LoginIn("1010269241@qq.com","aA19908112404")
        time.sleep(3)
        print(l)
        self.assertIn('myinfo',l)
'''
