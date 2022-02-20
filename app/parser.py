import logging
import requests
from bs4 import BeautifulSoup


class CarParser(object):

    def __init__(self):

        self.root_url = "https://auto.mail.ru/catalog/"
        self.html = ""
        self.status_code = 0

    def get_page_html(self, url: str):

        req = requests.get(url)
        logging.debug(url)
        self.status_code = req.status_code
        if self.status_code == 200:
            self.html = BeautifulSoup(req.text, 'html.parser')
        else:
            logging.error("Ошибка при подключению к каталогу")

    def get_data_dict(self):
        pass


