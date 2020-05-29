import time
from bs4 import BeautifulSoup
import requests,pprint,json
from selenium import webdriver
import getpass


insta_dic = {}
username = getpass.getpass(prompt='----  \n \n')
password = getpass.getpass(prompt='----  \n \n')
driver = webdriver.Chrome()
driver.get('https://www.instagram.com')
driver.maximize_window()
time.sleep(4)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button').click()
time.sleep(10)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/a').click()
time.sleep(6)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
time.sleep(4)
# from here onwords. I'm starting to scroll 
value=0.1
# Get scroll height
last_height=driver.execute_script('return document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight')  
while 1: # starting scrolling slowly so the suggesions will disappear from the page
    driver.execute_script('document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollTo(0,document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP > ul > div > li:nth-child(12)").scrollHeight/{});'.format(value)) # scroll the page upto some value	
    # Wait to load page 
    time.sleep(5)
    #Get new scroll height after loading 
    new_height=driver.execute_script('return document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight')
    if last_height==new_height:
        break
    last_height=new_height
    value+=0.1 

while 1: # starting scrolling fastly to load all the data we want 
    last_height=driver.execute_script('return document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight')# Get scroll height
    driver.execute_script('document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollTo(0,document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight)')# scroll down the page to it's height 
    time.sleep(5)# Wait to load page 
    new_height=driver.execute_script('return document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight')
    if new_height==last_height:
        break 
driver1 = driver.execute_script('return document.documentElement.outerHTML')
soup = BeautifulSoup(driver1,'html.parser').find('div',class_='PZuss').find_all('li')
followers = soup
followerslist = []
for i in range(len(followers)): 
    followerslist.append(followers[i].find('a',class_='FPmhX notranslate _0imsa').text)

time.sleep(3)

# driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button/svg').click()
driver.execute_script("window.history.go(-1)")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
time.sleep(4)

value = 0.1

last_height = driver.execute_script('return document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight')  

while True:
    driver.execute_script("document.querySelector('body > div.RnEpo.Yx5HN > div > div.isgrP').scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    value+=0.1
while 1: # starting scrolling fastly to load all the data we want 
    last_height=driver.execute_script('return document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight')# Get scroll height
    driver.execute_script('document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollTo(0,document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight)')# scroll down the page to it's height 
    time.sleep(5)# Wait to load page 
    new_height=driver.execute_script('return document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP").scrollHeight')
    if new_height==last_height:
        break 

driver2 = driver.execute_script('return document.documentElement.outerHTML')
soup2 = BeautifulSoup(driver2,'html.parser').find('div',class_='PZuss').find_all('li')
folowings = soup2
following_list = []
for j in range(len(folowings)):
    following_list.append(folowings[j].find('a',class_='FPmhX notranslate _0imsa').text)

time.sleep(3)


unwanted = []

for i in following_list:
    if i not in followerslist:
        unwanted.append(i)



insta_dic["followers"] = followerslist
insta_dic["followings"] = following_list
insta_dic["unwanted peoples"] = unwanted

print(followerslist)
print("_______________________________________")

print(following_list)
print("_______________________________________")
print(unwanted)
print("_______________________________________")

#with open('insta_data.json','w') as f:
#    json.dump(insta_dic,f)

driver.quit()
