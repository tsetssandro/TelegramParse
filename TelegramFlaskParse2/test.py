from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://web.telegram.org/z/#/login')

driver.implicitly_wait(10)
login_button = driver.find_element(By.XPATH, '//button')
print(login_button.get_attribute("outerHTML"))
login_button.click()

try:
    inputNumber = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='sign-in-phone-number']"))
    )
    # print(inputNumber.get_attribute("outerHTML"))
    PhoneNumber = input("Enter Phone Number : ")
    inputNumber.send_keys(PhoneNumber)

    LoginButton = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//button"))
    )
    
    # print(LoginButton.get_attribute("outerHTML"))

    LoginButton.click()

    CodeInput = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//input"))
    )

    print(CodeInput.get_attribute("outerHTML"))


    inputCode = input("Please Enter Your Code That you received in your Telegram : ")

    CodeInput.send_keys(inputCode)




    # GroupNameInput = WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.XPATH, "//input"))
    # )

    # print(CodeInput.get_attribute("outerHTML"))


    time.sleep(20)

finally:
    driver.quit()


