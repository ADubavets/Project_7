# pip install beautifulsoup4
# pip install pandas


import requests
from bs4 import BeautifulSoup
import postgres_data_sql_client
from datetime import datetime


class Parser:
    links_to_parse = [
        'https://www.kufar.by/l/kompyuternaya-tehnika',
        'https://www.kufar.by/l/kompyuternaya-tehnika?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MiwicGl0IjoiMjg3MDYwMzUifQ'
        '%3D%3D',
        'https://www.kufar.by/l/kompyuternaya-tehnika?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MywicGl0IjoiMjg3MDYwMzUifQ'
        '%3D%3D',
        'https://www.kufar.by/l/kompyuternaya-tehnika?cursor=eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6NCwicGl0IjoiMjg3MDYwMzUifQ'
        '%3D%3D'
    ]

    @staticmethod
    def get_computerisation_technical_by_link(link):
        response = requests.get(link)
        computerisation_technical_data = response.text

        computerisation_technical_items = []
        to_parse = BeautifulSoup(computerisation_technical_data, 'html.parser')
        for elem in to_parse.find_all('a', class_='styles_wrapper__5FoK7'):
            try:
                price, decription = elem.text.split('р.')
                computerisation_technical_items.append((
                    elem['href'],
                    int(price.replace(' ', '')),
                    decription
                ))
            except Exception:
                print(f'Цена не была указана. {elem.text}')
        return computerisation_technical_items

    # @staticmethod
    # def save_to_csv(computerisation_technical_items):
    #     pandas.DataFrame(computerisation_technical_items).to_csv('computerisation_technical.csv', index=False)

    # @staticmethod
    # def save_to_sqlite(computerisation_technical_items):
    #     connection = data_sql_client.get_connection()
    #     for item in computerisation_technical_items:
    #         data_sql_client.insert(connection, item[0], item[1], item[2])

    @staticmethod
    def save_to_postgres(computerisation_technical_items):
        connection = postgres_data_sql_client.get_connection()
        postgres_data_sql_client.create_computerisation_technical_table(connection)
        for item in computerisation_technical_items:
            item_parse_time = datetime.now()
            postgres_data_sql_client.insert(connection, item[0], item[1], item[2])

    def run(self):
        computerisation_technical_items = []
        for link in Parser.links_to_parse:
            computerisation_technical_items.extend(self.get_computerisation_technical_by_link(link))
        # self.save_to_csv(computerisation_technical_items)
        # self.save_to_sqlite(computerisation_technical_items)
        self.save_to_postgres(computerisation_technical_items)


Parser().run()
