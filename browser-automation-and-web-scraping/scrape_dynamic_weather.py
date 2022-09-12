from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import date, datetime

def get_driver():
  service = Service(os.environ.get('PATH_TO_CHROME_DRIVER'))

  options = webdriver.ChromeOptions()

  # set option to make browsing easier
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])


  driver = webdriver.Chrome(service=service, options=options)
  
  driver.get(os.environ.get('WEBSITE_ADDRESS'))
  
  return driver

def main():
  driver = get_driver()
  goToLoginPage(driver)
  loginThroughForm(driver)
  scrapeData(driver)

def goToLoginPage(driver):
  element = driver.find_element(By.ID ,"loginLink")
  element.click()
  time.sleep(3)
  
def loginThroughForm(driver):
  driver.find_element(By.ID ,"id_username").send_keys("admin")
  driver.find_element(By.ID ,"id_password").send_keys("1Password" + Keys.RETURN)
  time.sleep(3)
  
def scrapeData(driver):
  while True:
    temperature = getTempareture(driver)
    saveTemperatureToFile(temperature)
    time.sleep(3)
  
def getTempareture(driver):
  element = driver.find_element(By.ID ,"unit")
  return element.text

def saveTemperatureToFile(temperature):
  today = date.today()
  storagePath = os.path.join(os.path.dirname(__file__), 'data')

  filename = today.strftime("%d-%m-%Y") + ".txt"
  filepath = os.path.join(storagePath, filename)
  f = open(filepath, "a")
  now = datetime.now()
  dt_string = now.strftime("%H:%M:%S")
  
  f.write(dt_string + " - " + temperature + " degrees Celsius\n")
  f.close()


main()
