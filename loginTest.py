import sys
import io
def setup_io():
    sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)
setup_io()
import time,unittest
import HTMLTestRunner
from selenium import webdriver
from search import search
class loginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://trains.ctrip.com/TrainBooking/SearchTrain.aspx')
        self.driver.maximize_window()
    def test_01(self): 
        se=search(self.driver)
        s=se.city('上海','杭州')

    def tearDown(self):
        time.sleep(6)
        self.driver.quit()

if __name__ == '__main__':
    suiteTest=unittest.TestSuite()
    suiteTest.addTest(loginTest("test_01"))
    filepath="po/re.html"
    fp=open(filepath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="report")
    runner.run(suiteTest)
    fp.close()
    