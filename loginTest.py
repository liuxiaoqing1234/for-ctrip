import sys
import io
def setup_io():
    sys.stdout = sys.__stdout__ = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8', line_buffering=True)
    sys.stderr = sys.__stderr__ = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8', line_buffering=True)
setup_io()
import time,unittest
import HTMLTestRunner
from selenium import webdriver
from loginPage import loginPage
class loginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://passport.ctrip.com/user/login?')
        self.driver.maximize_window()
    def test_01(self):
        lo=loginPage(self.driver)
        l=lo.LoginIn("1010269241@qq.com","aA19908112404")
#        time.sleep(9)
        print(l)
        self.assertIn('myinfo',l)
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
    