from selenium import webdriver
import HtmlTestRunner 
import time
import unittest

class login(unittest.TestCase):

    def test_drvalidlogin(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://onlineehrproj.netlify.app/sign-in") 
        time.sleep(1)
        userid=self.driver.find_element_by_xpath('//*[@id="name"]')
        userid.send_keys("demo2@gmail.com")
        time.sleep(1)
        password=self.driver.find_element_by_xpath('//*[@id="password"]')
        password.send_keys("sparshgoyal")
        time.sleep(1)
        signin=self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/form/div[3]/button')
        signin.click()
        time.sleep(2)
  
        self.assertEqual(self.driver.current_url, "https://onlineehrproj.netlify.app/docdash")
   
    def test_drinvalidlogin(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://onlineehrproj.netlify.app/sign-in") 
        time.sleep(1)
        userid=self.driver.find_element_by_xpath('//*[@id="name"]')
        userid.send_keys("aishwarya@gmail.com")
        time.sleep(1)
        password=self.driver.find_element_by_xpath('//*[@id="password"]')
        password.send_keys("123123123")
        time.sleep(1)
        signin=self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/form/div[3]/button')
        signin.click()
        time.sleep(2)
  
        self.assertEqual(self.driver.current_url, "https://onlineehrproj.netlify.app/docdash")

          
       
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())