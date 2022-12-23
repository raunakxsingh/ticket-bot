from selenium import webdriver
import selenium
from selenium.webdriver.chrome.webdriver import WebDriver
selenium.webdriver.remote.webelement.WebElement
import time

PATH = "/home/ricky/Webdriver/chromedriver"
wd = webdriver.Chrome(PATH)
wd.implicitly_wait(5)
# HOME PAGE
wd.get("https://www.irctc.co.in/nget/train-search")
covid_popup = wd.find_element_by_xpath('/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button')
covid_popup.click()
dropdown_menu = wd.find_element_by_xpath('/html/body/app-root/app-home/div[1]/app-header/div[1]/div[2]')
dropdown_menu.click()
# LOGIN
login_button = wd.find_element_by_xpath('//*[@id="slide-menu"]/p-sidebar/div/nav/div/label/button')
login_button.click()
time.sleep(2)
username = wd.find_element_by_xpath('//*[@id="userId"]')
username.send_keys("raghuvanshi2021")
password = wd.find_element_by_xpath('//*[@id="pwd"]')
password.send_keys("Hariom2021")
capcha_text = wd.find_element_by_xpath('//*[@id="nlpAnswer"]')
capcha_text.click()
time.sleep(30)
# Train Search
from_text = wd.find_element_by_xpath('//*[@id="origin"]/span/input')
from_text.send_keys('LTT')
from_station = wd.find_element_by_id('pr_id_1_list')
from_station.click()

