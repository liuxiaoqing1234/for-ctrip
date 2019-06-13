import time
from base import base
class loginPage(base):
    def username(self):
        return self.by_id('nloginname')
    def psd(self):
        return self.by_id('npwd')
    def verify(self):
        print('ttt')
    def btn(self):
        return self.by_id('nsubmit')
    def LoginIn(self,username,psd):
        self.username().send_keys(username)
        self.psd().send_keys(psd)
        self.btn().click()
        time.sleep(6)
        return self.dr_url()