from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

count = 5

driver = webdriver.Chrome("C:\Users\Akul Chhillar\Downloads\c\chromedriver.exe")
wait = WebDriverWait(driver, 10)

driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
driver.implicitly_wait(10)

wait.until(EC.element_to_be_clickable((By.NAME, 'username'))).send_keys("USERNAME")
wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys("PASSWORD")
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'HmktE'))).submit()


wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.aOOlW.HoLwm'))).click()

driver.get("https://www.instagram.com/explore/")




while count >0:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'v1Nh3.kIKUG._bz0w'))).click()

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'oW_lN._0mzm-.sqdOP.yWX7d'))).click()
    driver.get("https://www.instagram.com/explore/")
    count = count - 1


