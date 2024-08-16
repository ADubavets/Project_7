import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from abc import ABC, abstractmethod


def get_connection():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres", password="253692472839", host="127.0.0.1", port="5432")
        return connection
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    # finally:
    #     if connection:
    #         connection.close()
    #         print("Соединение с PostgreSQL закрыто")


def create_computerisation_technical_table(conn):
    cursor_object = conn.cursor()
    cursor_object.execute(
        """
            CREATE TABLE IF NOT EXISTS app_1_computerisationtechnical
            (
                id serial PRIMARY KEY, 
                link text, 
                price integer, 
                description text
            )
        """
    )
    conn.commit()


def get_items(conn, price_from=0, price_to=100000):
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM app_1_computerisationtechnical WHERE price >= {price_from} and price <= {price_to}')
    return cursor.fetchall()


def insert(conn, link, price, description):
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO app_1_computerisationtechnical (link, price, description) "
        f"VALUES ('{link}', '{price}', '{description}')")
    conn.commit()


def postgres_test():
    conn = get_connection()
    create_computerisation_technical_table(conn)
    items = get_items(conn, 1, 1000)
    for item in items:
        print(item)
    conn.close()


postgres_test()
