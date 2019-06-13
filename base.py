#from selenium import webdriver
class base():
    def __init__(self,driver):
        self.driver=driver
    #by id
    def by_id(self,element):
        return self.driver.find_element_by_id(element)
    #by name
    def by_name(self,element):
        return self.driver.find_element_by_name(element)
    #by xpath
    def by_xpath(self,element):
        return self.driver.find_element_by_xpath(element)
    #by css
    def by_css(self,element):
        return self.driver.find_element_by_css_selector(element)
    #find current url
    def dr_url(self):
        return self.driver.current_url

