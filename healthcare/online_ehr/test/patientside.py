from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import datetime 
driver = webdriver.Firefox()


driver.get("http://127.0.0.1:3000/")
patientbtn = driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/a[2]/button').click()
time.sleep(3)
patientid = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[1]/input')
patientid.send_keys('7097be37-1f2b-4fa9-944d-18c2d8d0a441')
time.sleep(3)
signinbtn = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div[2]/form/div[2]/button').click()
time.sleep(3)

gend = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[2]/section/div/div[1]/div[1]/button')
gend.click()
time.sleep(3)
vitald = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[2]/section/div/div[2]/div[1]/button')
vitald.click()
time.sleep(3)
sociald =driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[2]/section/div/div[3]/div[1]/button')
sociald.click()
time.sleep(3)
allegies = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[2]/section/div/div[4]/div[1]/button')
allegies.click()
time.sleep(3)
problemd = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[2]/section/div/div[5]/div[1]/button')
problemd.click()
time.sleep(3)
msg = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[2]/section/form/div/textarea')
msg.send_keys("Please Tell me my next Appointment Date")
time.sleep(2)
send = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[2]/section/form/div/div')
send.click()
pres = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div[1]/nav/ul/li[2]/button')
pres.click()
time.sleep(3)
logout = driver.find_element_by_xpath('/html/body/div/div/div/div/div[1]/nav/div/ul/li/a')
logout.click()

