from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

email = 'yourmailid'
password = 'yourspotifypassword'

driver = webdriver.Chrome(executable_path=r'yourpath\chromedriver.exe')  #give your path to chromedriver
driver.get("https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2F")
time.sleep(2)


element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[1]/div/input")

element.send_keys(email)

element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/div/input")

element.send_keys(password)

element.send_keys(Keys.RETURN)


