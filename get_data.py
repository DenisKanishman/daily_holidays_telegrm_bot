from selenium import webdriver
from selenium.webdriver.common.by import By


def get_text():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=chrome_options)

    driver.get('https://www.calend.ru/')

    text = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[9]/div[1]/ul/li[1]/div[2]').text

    driver.close()

    return text