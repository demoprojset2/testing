from socket import ALG_OP_VERIFY
from this import d
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import datetime 

driver = webdriver.Firefox()

# driver.get('http://127.0.0.1:3000/sign-in/')
driver.get("https://xenodochial-gates-c9614f.netlify.app")

doctorsbtn = driver.find_element_by_xpath('//*[@id="header"]/div/a[1]/button')
doctorsbtn.click()
time.sleep(1)

#register
user = driver.find_element_by_id('name')
user.send_keys("Sparsh")
time.sleep(0.5)

firstname = driver.find_element_by_id('firstname')
time.sleep(1)
firstname.send_keys("sparsh")
time.sleep(0.5)

lastname= driver.find_element_by_id('lastname')
lastname.send_keys("goyal")
time.sleep(1)


speciality= driver.find_element_by_id('speciality')
speciality.send_keys("cardio")
time.sleep(1)

password = driver.find_element_by_id('password')
password.send_keys("sparshgoyal")
time.sleep(1)


conpassword = driver.find_element_by_xpath('/html/body/div/div/div/div[3]/div/form/div[6]/input')
conpassword.send_keys("sparshgoyal")
time.sleep(1)

email = driver.find_element_by_id('email')
email.send_keys("demo2@gmail.com")
time.sleep(1)


time.sleep(1)
gender = driver.find_element_by_xpath('//*[@id="validationCustom04"]/option[3]').click()

time.sleep(2)
submitbtn = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/form/div[9]/button')
submitbtn.click()
time.sleep(2)

#login
name=driver.find_element_by_id("name")
name.send_keys("demo2@gmail.com")

passw=driver.find_element_by_id("password")
passw.send_keys("sparshgoyal")

driver.find_element_by_css_selector('#root > div > div > div.appForm > div > form > div:nth-child(3) > button').click()
time.sleep(1)

#add patient
driver.find_element_by_xpath('/html/body/div/div/div/div[1]/nav/div/ul/li[1]/a/button').click()
time.sleep(1)


name = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[1]/div/div[1]/input')
name.send_keys("yash")
time.sleep(1)

phoneNumber = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[1]/div/div[2]/input')
phoneNumber.send_keys("9503506363")
time.sleep(1)


gender = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[1]/div/div[3]/select/option[3]').click()


email = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[1]/div/div[4]/div/input') 
email.send_keys("sparshgoyal9@gmail.com")



address = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[1]/div/div[5]/input')
address.send_keys("Mohanpura, Idgha, Agra")


dob = driver.find_element_by_name('dob')
dob.send_keys("1999-03-12")
dob.click()
time.sleep(1)

weight = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[1]/input')
weight.send_keys("60")
time.sleep(1)

height = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[2]/input')
height.send_keys("152")


BPs = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[3]/input')
BPs.send_keys("120")
time.sleep(1)

BPa = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[4]/input')
BPa.send_keys("80")



temperatue = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[5]/input')
temperatue.send_keys("98")
time.sleep(1)

pulse = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[6]/input')
pulse.send_keys("80")
time.sleep(1)

smokingstatus = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[7]/select/option[2]').click()
time.sleep(1)

drinkingstatus = driver.find_element_by_xpath('/html/body/div/div/div/form/div[1]/div[2]/div/div[8]/select/option[2]').click()
time.sleep(1)


addpatientbtn = driver.find_element_by_xpath('/html/body/div/div/div/form/div[2]/div/button')
addpatientbtn.click()
time.sleep(5)

next_tbn=driver.find_element_by_xpath("/html/body/div/div/div/form/div[2]/div[2]/a/button").click()
time.sleep(5)



#allergy details
alg_sub=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[1]/form/div[1]/div/div[1]/input").send_keys("pollution")
time.sleep(2)
alg_ver=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[1]/form/div[1]/div/div[2]/select/option[2]").click()
time.sleep(2)
alg_crit=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[1]/form/div[1]/div/div[3]/select/option[2]").click()
time.sleep(2)
alg_type=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[1]/form/div[1]/div/div[4]/select/option[2]").click()
time.sleep(2)
alg_comm=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[1]/form/div[1]/div/div[5]/input").send_keys("all well")
time.sleep(2)
alg_save=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[1]/form/div[2]/button").click()
time.sleep(10)

#problem details
prb=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/nav/div/a[2]").click()
time.sleep(2)
prb_name=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[2]/form/div[1]/div/div[1]/input").send_keys("headache")
time.sleep(2)
prb_sev=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[2]/form/div[1]/div/div[2]/select/option[2]").click()
time.sleep(2)
prb_status=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[2]/form/div[1]/div/div[3]/select/option[2]").click()
time.sleep(2)
prb_date=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[2]/form/div[1]/div/div[4]/input").send_keys("2022-01-01")
time.sleep(2)
prb_btn=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[2]/form/div[2]/button").click()
time.sleep(5)

#medication details
med=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/nav/div/a[3]").click()
time.sleep(2)
med_name=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[3]/form/div[1]/div/div[1]/input").send_keys("dolo")
time.sleep(2)
med_manu=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[3]/form/div[1]/div/div[2]/input").send_keys("cipla")
time.sleep(2)
med_dose=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[3]/form/div[1]/div/div[3]/input").send_keys("2")
time.sleep(2)
med_freq=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[3]/form/div[1]/div/div[4]/select/option[2]").click()
time.sleep(2)
med_desc=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[3]/form/div[1]/div/div[5]/input").send_keys("all weell")
time.sleep(2)
med_btn=driver.find_element_by_xpath("/html/body/div/div/div/section/div/div/div/div/div[3]/form/div[2]/button").click()
time.sleep(5)

#view details
view_btn=driver.find_element_by_xpath("/html/body/div/div/div/div[3]/a ").click()
time.sleep(4)

#problem details
see_prb=driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[2]/button").click()
time.sleep(3)
           
#allergies
all = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[3]/button').click()
time.sleep(2) 
addall = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div/div/button').click()
time.sleep(2)                          
sub = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[1]/input').send_keys("Dust")
time.sleep(2)                    
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[2]/select/option[4]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[3]/select/option[3]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[4]/select/option[2]').click()
time.sleep(2)
com = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[5]/input').send_keys("Stay Happy")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[2]/button[2]').click()
time.sleep(2)

#allergies update
driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[3]/button').click()
time.sleep(2)  
up = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div/div[1]/div[1]/div/button[1]').click()
time.sleep(2)  
driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div/div[1]/div[2]/div/form/div[1]/div[2]/select/option[3]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div/div[1]/div[2]/div/form/div[2]/button').click()
time.sleep(2)

#prescription update
pre = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[4]/button').click()
time.sleep(2)
add = driver.find_element_by_xpath('/html/body/div/div/div/div/section/div/div/div/div[2]/div/button').click()
time.sleep(2)
medn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div[2]/div/div/div/div/form/div[1]/div/div[1]/input').send_keys("alpha alpha")
time.sleep(2)
medf = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div[2]/div/div/div/div/form/div[1]/div/div[2]/input').send_keys("McNeil")
time.sleep(2)
medd = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div[2]/div/div/div/div/form/div[1]/div/div[3]/input').send_keys("2")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div[2]/div/div/div/div/form/div[1]/div/div[4]/select/option[2]').click()
time.sleep(2)
medde = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div[2]/div/div/div/div/form/div[1]/div/div[5]/input').send_keys("take it properly")
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/section/div/div/div/div[2]/div/div/div/div/form/div[2]/button[2]').click()
time.sleep(2)

#messages 
driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[5]/button").click()
time.sleep(2)


#reversing
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)
driver.back()
time.sleep(2)

#searchbar
searchbar = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div[1]/form/div/div/input')
searchbar.send_keys("sparsh")
time.sleep(1)

#problem
pat=driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div/i").click()
problem_det=driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[2]/button").click()
time.sleep(2)
add_btn=driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/div/div/button").click()
prb_name=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[1]/input").send_keys("headache")
prb_sev=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[2]/select/option[2]").click()
prb_status=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[3]/select/option[2]").click()
prb_date=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[1]/div/div[4]/input").send_keys("2022-01-12")
time.sleep(2)
save_btn=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div/div/div/div/form/div[2]/button[2]").click()

#allergy
# allergy=driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[3]/button").click()
# alg_add=driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/div/div[4]/button").click()
# alg_sub=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[4]/div/div/div/form/div[1]/div/div[1]/input").send_keys("pollution")
# alg_ver=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[4]/div/div/div/form/div[1]/div/div[2]/select/option[2]").click()
# alg_cric=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[4]/div/div/div/form/div[1]/div/div[3]/select/option[2]").click()
# alg_type=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[4]/div/div/div/form/div[1]/div/div[4]/select/option[2]").click()
# alg_comment=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[4]/div/div/div/form/div[1]/div/div[5]/input").send_keys("will get soon recovery")
# time.sleep(2)
# alg_save=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[4]/div/div/div/form/div[2]/button[2]").click()
# time.sleep(2)

# prescription
# prescription=driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[4]/button").click()
# add_pres=driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/div/div[3]/div/button").click()                                  
# med_name=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[3]/div/div/div/div/form/div[1]/div/div[1]/input").send_keys("dolo6550")
# manuf=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[3]/div/div/div/div/form/div[1]/div/div[2]/input").send_keys("cipla")
# dose_amt=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[3]/div/div/div/div/form/div[1]/div/div[3]/input").send_keys("2")
# freq=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[3]/div/div/div/div/form/div[1]/div/div[4]/select/option[2]").click()
# desc=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[3]/div/div/div/div/form/div[1]/div/div[5]/input").send_keys("you will be perfect")
# time.sleep(2)
# pres_save=driver.find_element_by_xpath("/html/body/div[1]/div/div/div/section/div/div/div/div[3]/div/div/div/div/form/div[2]/button[2]").click()

# time.sleep(2)
# driver.find_element_by_xpath("/html/body/div/div/div/div/section/div/div/nav/div/div/ul/li[5]/button").click()
# time.sleep(2)


driver.find_element_by_css_selector("#navbarNav > ul > li:nth-child(2) > button").click()
