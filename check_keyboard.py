from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def check_keyboards():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.bug.co.il/')

    search = driver.find_element(By.TAG_NAME, 'input')

    search.send_keys('deathstalker')
    search.send_keys(Keys.ENTER)

    time.sleep(1)

    container = driver.find_element(By.CLASS_NAME, 'products-cubes-container').find_element(By.CLASS_NAME, 'section')
    elements = container.find_elements(By.TAG_NAME, 'h4')

    keyboards = []

    for element in elements:
        keyboards.append(element.text)

    driver.close()

    return keyboards
