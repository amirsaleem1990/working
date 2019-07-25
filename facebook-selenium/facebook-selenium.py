from selenium import webdriver
import numpy as np
import time
from selenium.webdriver.common.keys import Keys
#in the string/Quotation marks enter the path to where you downloaded the chromedriver.
usrname = input("Enter your user name: ")
pas = input("Enter your password: ")

browser = webdriver.Firefox(executable_path="./geckodriver")
#navigates you to the facebook page.
browser.get('https://www.facebook.com/')

#find the username field and enter the email example@yahoo.com.
time.sleep(np.random.randint(3, 6))
username = browser.find_elements_by_css_selector("input[name=email]")
username[0].send_keys(usrname)


#find the password field and enter the password password.
time.sleep(np.random.randint(3, 6))
password = browser.find_elements_by_css_selector("input[name=pass]")
password[0].send_keys(pas)


#find the login button and click it.
time.sleep(np.random.randint(3, 6))
loginButton = browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()

f1 = "zahid.mughal.5895"
time.sleep(np.random.randint(3, 6))
Query = browser.find_elements_by_css_selector("input[name=q]")
Query[0].send_keys(f1)
Query_search_button = browser.find_elements_by_css_selector("button[type=submit]")
Query_search_button[0].click()