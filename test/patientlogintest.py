from selenium import webdriver
import HtmlTestRunner
import time
import unittest

class login(unittest.TestCase):

    def test_validloginp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/patient-login") 
        time.sleep(1)
        userid=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[1]/input')
        userid.send_keys("520cbc11-77ff-4eef-bb14-27aa05a68f08")
        time.sleep(1)
        signin=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[2]/button')
        signin.click()
        time.sleep(2)
  
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:3000/patient-dashboard/520cbc11-77ff-4eef-bb14-27aa05a68f08")
   
    def test_invalidloginp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:3000/patient-login") 
        time.sleep(1)
        userid=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[1]/input')
        userid.send_keys("renu")
        time.sleep(1)
        signin=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[2]/button')
        signin.click()
        time.sleep(2)
  
        self.assertEqual(self.driver.current_url, "http://127.0.0.1:3000/patient-dashboard/")

          
       
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())