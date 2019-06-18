import time
from base import base
class search(base):
    def leave(self):
        return self.by_id('notice01')
    def arrive(self):
        return self.by_id('notice08')
    def city(self,leave,arrive):
        self.leave().send_keys(leave)
        self.arrive().send_keys(arrive)