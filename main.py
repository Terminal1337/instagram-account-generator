from concurrent.futures import ThreadPoolExecutor
import threading
import pyfiglet,os
import emailAPI
from colorama import Fore,init
init(convert=True)
import random,json
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import string
import time
def getMail():
    domains = ["@1secmail.net","@1secmail.org",'@1secmail.com'] 
    domain = random.choice(domains)
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = 7))
    mail = str(res+domain)
    return mail
def getFullName():
    r = requests.get('https://apis.kahoot.it/namerator').text
    user = json.loads(r)
    return str(user['name'])

def username():
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = 8))
    return str(res)


def Gen():
    global req
    global email_val
    global email_id
    req = emailAPI.getMail()
    email_val = req['mail']
    email_id = req['id']
    driver = webdriver.Firefox() 
    driver.get('https://www.instagram.com/accounts/emailsignup/')
    time.sleep(5)
    # cookiemonster = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[2]')
    # cookiemonster.click()
    # time.sleep(3)
    email = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[3]/div/label/input')
    email.send_keys(email_val)
    full_name = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[4]/div/label/input')
    full_name.send_keys(getFullName())
    username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[5]/div/label/input')
    username.send_keys(extraUser())
    password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input')
    password.send_keys("Imblacklol123")
    time.sleep(1)
    sign_up = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[7]/div/button').click()
    time.sleep(5)
# select = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select')
    month = Select(driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select'))
    month.select_by_value('3')
    date_val = Select(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select'))
    date_val.select_by_index('8')
    # time.sleep(500)
    year_val = Select(driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select'))
    year_val.select_by_value('2002')
    nextx = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[6]/button')
    nextx.click()
    time.sleep(3) 
    codex = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/input')
    time.sleep(15)
    codex.send_keys(emailAPI.getLetterx(email_id))
    nex_sign = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div/div[2]/button')
    nex_sign.click()
    file = open('output.txt','w')
    file.write(f'{email_val}:Imblacklol123')
    file.close()
    time.sleep(2)

banner = """
                                                                                                       
_/_/_/_/_/                                    _/                      _/    _/_/_/                     
   _/      _/_/    _/  _/_/  _/_/_/  _/_/        _/_/_/      _/_/_/  _/  _/          _/_/    _/_/_/    
  _/    _/_/_/_/  _/_/      _/    _/    _/  _/  _/    _/  _/    _/  _/  _/  _/_/  _/_/_/_/  _/    _/   
 _/    _/        _/        _/    _/    _/  _/  _/    _/  _/    _/  _/  _/    _/  _/        _/    _/    
_/      _/_/_/  _/        _/    _/    _/  _/  _/    _/    _/_/_/  _/    _/_/_/    _/_/_/  _/    _/     
                                                                                                       
                                                                                                       
"""
print(Fore.LIGHTMAGENTA_EX+banner+Fore.RESET)
os.system("title [TerminalGen] Support: Terminal#1337")
threadCount = int(input(Fore.LIGHTGREEN_EX+"Enter The Number of Threads [>] "+Fore.RESET))

threads = []
for i in range(threadCount):
     t = threading.Thread(target=Gen)
     t.start()
     threads.append(t)
for i in range(threadCount):
    threads[i].join()