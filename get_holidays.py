import requests
from bs4 import BeautifulSoup

def get_holidays():
    url = "https://www.calend.ru/"

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        element = soup.find('li', class_='one-two').find('span', class_='title')

        text = element.text

        return text


def check_keyboard():

    url = "https://www.bug.co.il/"

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')

        element = soup.find()

        text = element.text

        return text