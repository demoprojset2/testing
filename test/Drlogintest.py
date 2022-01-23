from selenium import webdriver
import HtmlTestRunner
import time
import unittest

class login(unittest.TestCase):

    def test_drvalidlogin(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/sign-in") 
        time.sleep(1)
        userid=self.driver.find_element_by_xpath('//*[@id="name"]')
        userid.send_keys("gawande@gmail.com")
        time.sleep(1)
        password=self.driver.find_element_by_xpath('//*[@id="password"]')
        password.send_keys("Aishwarya")
        time.sleep(1)
        signin=self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/form/div[3]/button')
        signin.click()
        time.sleep(2)
  
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:3000/docdash")
   
    def test_drinvalidlogin(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/sign-in") 
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
  
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:3000/docdash")

          
       
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())