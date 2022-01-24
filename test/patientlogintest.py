from selenium import webdriver
import HtmlTestRunner
import time
import unittest

class login(unittest.TestCase):

    def test_validloginp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://xenodochial-gates-c9614f.netlify.app/patient-login") 
        time.sleep(1)
        userid=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[1]/input')
        userid.send_keys("459b8fe2-b922-433f-a598-3a7aa9ce48d4")
        time.sleep(1)
        signin=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[2]/button')
        signin.click()
        time.sleep(2)
  
        self.assertEqual(self.driver.current_url, "https://xenodochial-gates-c9614f.netlify.app/patient-dashboard/459b8fe2-b922-433f-a598-3a7aa9ce48d4")
   
    def test_invalidloginp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://xenodochial-gates-c9614f.netlify.app/patient-login") 
        time.sleep(1)
        userid=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[1]/input')
        userid.send_keys("renu")
        time.sleep(1)
        signin=self.driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[2]/button')
        signin.click()
        time.sleep(2)
  
        self.assertEqual(self.driver.current_url, "https://xenodochial-gates-c9614f.netlify.app/patient-dashboard/")

          
       
    
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner())