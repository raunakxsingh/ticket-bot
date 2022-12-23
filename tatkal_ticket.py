from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/home/ricky/Webdriver/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.irctc.co.in/nget/train-search")
covid_popup = driver.find_element_by_xpath("/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button").click()     
covid_popup.click()

# HOME PAGE 
login_button = driver.find_elements_by_xpath("/html/body/app-root/app-home/div/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button").click()
login_button.click()
